import sys
sys.stdout.reconfigure(encoding='utf-8')
import asyncio
import httpx
from backend.main import app
from backend.translator import translation_service
from backend.models import Glossary

async def test_all():
    print("[-] Starting comprehensive test suite...")

    async with app.router.lifespan_context(app):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            # 1. Test GET /manifest.json and PWA setup
            r = await client.get("/manifest.json")
            assert r.status_code == 200, f"Manifest status: {r.status_code}"
            assert r.json().get("short_name") == "NovelAI"
            print("[OK] PWA manifest.json is valid.")

            # 2. Test GET /sw.js
            r = await client.get("/sw.js")
            assert r.status_code == 200, f"SW status: {r.status_code}"
            print("[OK] PWA Service Worker is reachable.")

            # 3. Test GET / (SPA index)
            r = await client.get("/")
            assert r.status_code == 200
            assert "Novel AI" in r.text
            print("[OK] Frontend SPA index.html rendered successfully.")

            # 4. Test GET /api/settings
            r = await client.get("/api/settings")
            assert r.status_code == 200
            data = r.json()
            assert "api_base_url" in data
            assert "model_name" in data
            print(f"[OK] Settings API: Base URL={data['api_base_url']}, Model={data['model_name']}")

            # 5. Test GET /api/scraper-rules
            r = await client.get("/api/scraper-rules")
            assert r.status_code == 200
            rules = r.json()
            assert len(rules) >= 4
            print(f"[OK] Scraper rules seeded: {len(rules)} default domain rules found.")

            # 5b. Test Discover API
            r = await client.get("/api/discover/categories")
            assert r.status_code == 200
            cats = r.json()
            assert len(cats) >= 8
            print(f"[OK] Discover categories: {len(cats)} genres available.")

            r = await client.get("/api/discover/novels?category=he_thong&time_range=week&sort_by=views")
            assert r.status_code == 200
            disc_data = r.json()
            disc_novels = disc_data.get("items", disc_data)
            assert len(disc_novels) >= 1
            print(f"[OK] Discover novels by time_range=week & sort_by=views: {len(disc_novels)} found.")

            # Test Reading Synopsis/Detail without downloading
            sample_cat_id = disc_novels[0]["id"]
            r = await client.get(f"/api/discover/novel/{sample_cat_id}")
            assert r.status_code == 200
            novel_preview = r.json()
            assert "description_vi" in novel_preview
            assert "views_week_fmt" in novel_preview
            assert "hot_month_fmt" in novel_preview
            print(f"[OK] Preview novel without downloading: Title='{novel_preview['title_vi']}', Views/Week={novel_preview['views_week_fmt']}, Hot/Month={novel_preview['hot_month_fmt']}")

            # Test Translation Queue Request
            r = await client.post("/api/queue/request", json={
                "novel_id": 2,
                "novel_title": "Toàn Cầu Băng Phong",
                "chapter_index": 14,
                "chapter_count": 1,
                "notes": "Test queue request"
            })
            assert r.status_code == 200
            queue_task = r.json()
            assert queue_task["chapter_index"] == 14
            task_id = queue_task["id"]
            print(f"[OK] Translation task queued successfully: Task ID={task_id}")

            # Test GET /api/queue
            r = await client.get("/api/queue")
            assert r.status_code == 200
            pending_tasks = r.json()
            assert any(t["id"] == task_id for t in pending_tasks)
            print(f"[OK] Active tasks in queue: {len(pending_tasks)} pending.")

            # Test complete task
            r = await client.post(f"/api/queue/{task_id}/complete")
            assert r.status_code == 200
            print(f"[OK] Completed task {task_id}.")

            # Test Clone from Discover
            r = await client.post("/api/discover/clone", json={
                "catalog_id": disc_novels[0]["id"],
                "auto_translate_first": 2
            })
            assert r.status_code == 200
            clone_res = r.json()
            cloned_id = clone_res["novel_id"]
            print(f"[OK] Clone from Discover Catalog successful: ID={cloned_id}, Title='{clone_res['novel_title']}'")

            # Cleanup cloned novel
            await client.delete(f"/api/novels/{cloned_id}")

            # 6. Test Novel creation from Raw Text (with regex chapter splitting)
            sample_raw_chinese = """
第1章 遮天伊始
九龙拉棺，星空古路。叶凡立于泰山之巅，俯瞰苍茫大地。
荒古圣体，天地难容，然而叶凡眸光坚定，誓要逆天而行。
青云宗的长老冷笑：“一介废体，也妄想修仙？”

第2章 荒古禁地
深渊无底，寒气逼人。叶凡与姬紫月并肩而行，踏入传说中的生命禁区。
在此地，圣药绽放瑞彩，太古凶兽咆哮震天。
“叶凡，小心！”姬紫月惊呼道。

第3章 逆天崛起
苦海初开，金色神芒冲宵而起。
叶凡一拳轰出，震碎苍穹，万法皆破！
"""
            r = await client.post("/api/novels/raw", json={
                "title": "Già Thiên Chi Lộ (Test)",
                "author": "Thần Đông",
                "description": "Tiểu thuyết tiên hiệp kinh điển về Cửu Long Kéo Quan và Hoang Cổ Thánh Thể.",
                "raw_text": sample_raw_chinese
            })
            assert r.status_code == 200, f"Create raw novel error: {r.text}"
            novel = r.json()
            novel_id = novel["id"]
            assert novel["total_chapters"] == 3
            print(f"[OK] Created novel from raw text: ID={novel_id}, Total chapters={novel['total_chapters']}.")

            # 7. Test listing chapters
            r = await client.get(f"/api/novels/{novel_id}/chapters")
            assert r.status_code == 200
            ch_list = r.json()
            assert len(ch_list) == 3
            print(f"[OK] Chapters listed: {[c['title'] for c in ch_list]}")

            ch1_id = ch_list[0]["id"]
            ch2_id = ch_list[1]["id"]

            # 8. Test reading chapter 1 details
            r = await client.get(f"/api/chapters/{ch1_id}")
            assert r.status_code == 200
            ch1 = r.json()
            assert "九龙拉棺" in ch1["raw_content"]
            assert ch1["next_id"] == ch2_id
            print(f"[OK] Chapter 1 detail validated, correctly linked to Chapter 2 (next_id={ch1['next_id']}).")

            # 9. Test adding Glossary items for this novel
            r = await client.post(f"/api/novels/{novel_id}/glossary", json={
                "source_term": "叶凡",
                "target_term": "Diệp Phàm",
                "category": "nhan_vat",
                "notes": "Nhân vật chính"
            })
            assert r.status_code == 200

            r = await client.post(f"/api/novels/{novel_id}/glossary", json={
                "source_term": "荒古圣体",
                "target_term": "Hoang Cổ Thánh Thể",
                "category": "canh_gioi",
                "notes": "Thể chất vô thượng"
            })
            assert r.status_code == 200

            r = await client.post(f"/api/novels/{novel_id}/glossary", json={
                "source_term": "青云宗",
                "target_term": "Thanh Vân Tông",
                "category": "dia_danh",
                "notes": "Môn phái"
            })
            assert r.status_code == 200

            # Query glossary
            r = await client.get(f"/api/novels/{novel_id}/glossary")
            assert r.status_code == 200
            gloss_items = r.json()
            assert len(gloss_items) == 3
            print(f"[OK] Glossary items created and verified ({len(gloss_items)} items).")

            # 10. Test Glossary Prompt Injection
            fake_gloss = [
                Glossary(source_term="叶凡", target_term="Diệp Phàm", category="nhan_vat"),
                Glossary(source_term="荒古圣体", target_term="Hoang Cổ Thánh Thể", category="canh_gioi"),
                Glossary(source_term="青云宗", target_term="Thanh Vân Tông", category="dia_danh"),
                Glossary(source_term="不相关的词", target_term="Từ không xuất hiện", category="khac")
            ]
            prompt_injection = translation_service.build_glossary_prompt(ch1["raw_content"], fake_gloss)
            assert "Diệp Phàm" in prompt_injection
            assert "Hoang Cổ Thánh Thể" in prompt_injection
            assert "Thanh Vân Tông" in prompt_injection
            assert "Từ không xuất hiện" not in prompt_injection
            print("[OK] Glossary prompt injection correctly filtered terms present in chapter text!")

            # 11. Test Reading Progress update and cross-device sync
            r = await client.put(f"/api/novels/{novel_id}/progress", json={
                "last_read_chapter_id": ch2_id,
                "last_read_index": 2,
                "scroll_position": 45.5
            })
            assert r.status_code == 200

            r = await client.get(f"/api/novels/{novel_id}")
            assert r.status_code == 200
            updated_novel = r.json()
            assert updated_novel["last_read_chapter_id"] == ch2_id
            assert updated_novel["last_read_index"] == 2
            assert updated_novel["scroll_position"] == 45.5
            print(f"[OK] Cross-device sync verified: last_read_index={updated_novel['last_read_index']}, scroll_pos={updated_novel['scroll_position']}%")

            # 12. Test deleting novel
            r = await client.delete(f"/api/novels/{novel_id}")
            assert r.status_code == 200
            print("[OK] Novel deletion verified.")

    print("\n==================================================")
    print("ALL TESTS PASSED! FULL SYSTEM IS WORKING 100%!")
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(test_all())
