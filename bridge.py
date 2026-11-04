"""Antigravity Bridge: Module kết nối trực tiếp giữa Antigravity AI và Cơ sở dữ liệu Web Novel.

Cho phép Antigravity đọc trực tiếp các chương chưa dịch từ SQLite,
dịch bằng model Gemini 3.8 Flash đang chạy trong Antigravity,
và ghi thẳng bản dịch vào cơ sở dữ liệu để xem trên PC và Điện thoại.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import argparse
import asyncio
import json
from pathlib import Path
from sqlalchemy import select, func
from backend.database import AsyncSessionLocal, init_db
from backend.models import Novel, Chapter, Glossary, TranslationTask
from backend.translator import translation_service

async def cmd_list():
    """Liệt kê các bộ truyện trong hệ thống"""
    await init_db()
    async with AsyncSessionLocal() as session:
        res = await session.execute(select(Novel).order_by(Novel.id.asc()))
        novels = res.scalars().all()
        if not novels:
            print("Chưa có truyện nào trong thư viện.")
            return

        print(f"\n{'ID':<5} | {'Tên truyện':<35} | {'Tổng chương':<12} | {'Đã dịch':<10} | {'Đang đọc':<10}")
        print("-" * 80)
        for n in novels:
            trans_res = await session.execute(
                select(func.count(Chapter.id)).where(
                    Chapter.novel_id == n.id,
                    Chapter.translation_status == "completed"
                )
            )
            trans_count = trans_res.scalar() or 0
            print(f"{n.id:<5} | {n.title[:32]:<35} | {n.total_chapters:<12} | {trans_count:<10} | Ch. {n.last_read_index}")
        print()

async def cmd_get_pending(novel_id: int, count: int = 5, start_index: int = None):
    """Lấy danh sách các chương chưa dịch kèm nội dung gốc và glossary để Antigravity dịch"""
    await init_db()
    async with AsyncSessionLocal() as session:
        novel = await session.get(Novel, novel_id)
        if not novel:
            print(f"Error: Không tìm thấy truyện có ID = {novel_id}")
            return

        # Load glossary
        gloss_res = await session.execute(
            select(Glossary).where(Glossary.novel_id == novel_id)
        )
        glossary_items = gloss_res.scalars().all()

        query = select(Chapter).where(
            Chapter.novel_id == novel_id,
            Chapter.translation_status != "completed"
        )
        if start_index:
            query = query.where(Chapter.chapter_index >= start_index)
        query = query.order_by(Chapter.chapter_index.asc()).limit(count)

        res = await session.execute(query)
        chapters = res.scalars().all()

        if not chapters:
            print(f"Truyện '{novel.title}' không còn chương nào chưa dịch (hoặc không tìm thấy theo điều kiện).")
            return

        result_data = {
            "novel_id": novel.id,
            "novel_title": novel.title,
            "chapters": []
        }

        for ch in chapters:
            glossary_text = translation_service.build_glossary_prompt(
                f"{ch.title}\n{ch.raw_content}", glossary_items
            )
            result_data["chapters"].append({
                "chapter_id": ch.id,
                "chapter_index": ch.chapter_index,
                "title_zh": ch.title,
                "raw_content": ch.raw_content,
                "glossary_prompt": glossary_text
            })

        output_file = Path("data") / f"pending_novel_{novel_id}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result_data, f, ensure_ascii=False, indent=2)

        print(f"[OK] Đã xuất {len(chapters)} chương cần dịch ra file: {output_file.as_posix()}")
        print(f"Chi tiết: Từ chương {chapters[0].chapter_index} đến chương {chapters[-1].chapter_index}")

async def cmd_save(chapter_id: int, title_translated: str, translated_content: str):
    """Cập nhật bản dịch của 1 chương vào database"""
    await init_db()
    async with AsyncSessionLocal() as session:
        ch = await session.get(Chapter, chapter_id)
        if not ch:
            print(f"Error: Không tìm thấy chapter ID = {chapter_id}")
            return

        ch.title_translated = title_translated.strip()
        ch.translated_content = translated_content.strip()
        ch.translation_status = "completed"
        ch.error_message = None
        await session.commit()
        print(f"[OK] Đã cập nhật bản dịch thành công cho Chương {ch.chapter_index}: '{ch.title_translated}'")

async def cmd_save_batch(batch_file_path: str):
    """Cập nhật hàng loạt bản dịch từ file JSON do Antigravity xuất ra"""
    await init_db()
    path = Path(batch_file_path)
    if not path.exists():
        print(f"Error: Không tìm thấy file {batch_file_path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chapters_to_save = data if isinstance(data, list) else data.get("chapters", [])

    async with AsyncSessionLocal() as session:
        updated = 0
        for item in chapters_to_save:
            ch_id = item.get("chapter_id") or item.get("id")
            title_tr = item.get("title_translated", "")
            content_tr = item.get("translated_content", "")
            if not ch_id or not content_tr:
                continue

            ch = await session.get(Chapter, ch_id)
            if ch:
                ch.title_translated = title_tr
                ch.translated_content = content_tr
                ch.translation_status = "completed"
                ch.error_message = None
                updated += 1

        await session.commit()
        print(f"[OK] Đã cập nhật thành công {updated} chương vào cơ sở dữ liệu!")

async def cmd_check_queue():
    """Kiểm tra các yêu cầu dịch đang chờ từ Web UI"""
    await init_db()
    async with AsyncSessionLocal() as session:
        res = await session.execute(
            select(TranslationTask).where(TranslationTask.status == "pending").order_by(TranslationTask.created_at.asc())
        )
        tasks = res.scalars().all()
        if not tasks:
            print("Không có yêu cầu dịch nào đang chờ trong hàng đợi.")
            return []
        print(f"\n[+] Có {len(tasks)} yêu cầu dịch đang chờ từ Web UI:")
        print(f"{'Task ID':<8} | {'Novel ID':<9} | {'Tên truyện':<30} | {'Từ Ch.':<8} | {'Số Ch.':<7} | {'Thời gian':<15}")
        print("-" * 85)
        for t in tasks:
            print(f"{t.id:<8} | {t.novel_id:<9} | {t.novel_title[:28]:<30} | {t.chapter_index:<8} | {t.chapter_count:<7} | {t.created_at.strftime('%H:%M:%S')}")
        print()
        return tasks

def main():
    parser = argparse.ArgumentParser(description="Antigravity Novel Translation Bridge")
    subparsers = parser.add_subparsers(dest="subcommand")

    # list
    subparsers.add_parser("list", help="Liệt kê danh sách truyện")

    # check-queue
    subparsers.add_parser("check-queue", help="Kiểm tra hàng đợi yêu cầu dịch từ Web")

    # get-pending
    p_get = subparsers.add_parser("get-pending", help="Lấy các chương chưa dịch để Antigravity dịch")
    p_get.add_argument("--novel-id", type=int, required=True, help="ID của truyện")
    p_get.add_argument("--count", type=int, default=5, help="Số lượng chương cần lấy (mặc định 5)")
    p_get.add_argument("--start", type=int, default=None, help="Bắt đầu từ chương số mấy")

    # save
    p_save = subparsers.add_parser("save", help="Lưu 1 chương đã dịch")
    p_save.add_argument("--chapter-id", type=int, required=True)
    p_save.add_argument("--title", type=str, required=True)
    p_save.add_argument("--file", type=str, required=True, help="Đường dẫn file text bản dịch")

    # save-batch
    p_batch = subparsers.add_parser("save-batch", help="Lưu nhiều chương đã dịch từ file JSON")
    p_batch.add_argument("--file", type=str, required=True, help="Đường dẫn file JSON chứa các bản dịch")

    args = parser.parse_args()

    if args.subcommand == "list":
        asyncio.run(cmd_list())
    elif args.subcommand == "check-queue":
        asyncio.run(cmd_check_queue())
    elif args.subcommand == "get-pending":
        asyncio.run(cmd_pending_wrap(args.novel_id, args.count, args.start))
    elif args.subcommand == "save":
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        asyncio.run(cmd_save(args.chapter_id, args.title, content))
    elif args.subcommand == "save-batch":
        asyncio.run(cmd_save_batch(args.file))
    else:
        parser.print_help()

async def cmd_pending_wrap(novel_id, count, start):
    await cmd_get_pending(novel_id, count, start)

if __name__ == "__main__":
    main()
