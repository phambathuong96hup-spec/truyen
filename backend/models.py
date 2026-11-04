import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from backend.database import Base

class Novel(Base):
    __tablename__ = "novels"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), default="Chưa rõ")
    cover_url = Column(String(1024), default="")
    source_url = Column(String(1024), default="")
    description = Column(Text, default="")
    genre = Column(String(100), default="Tiểu thuyết")
    total_chapters = Column(Integer, default=0)
    last_read_chapter_id = Column(Integer, nullable=True)
    last_read_index = Column(Integer, default=1)
    scroll_position = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    chapters = relationship("Chapter", back_populates="novel", cascade="all, delete-orphan", order_by="Chapter.chapter_index")
    glossaries = relationship("Glossary", back_populates="novel", cascade="all, delete-orphan")

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    novel_id = Column(Integer, ForeignKey("novels.id", ondelete="CASCADE"), nullable=False, index=True)
    chapter_index = Column(Integer, nullable=False, index=True)
    title = Column(String(500), nullable=False)
    title_translated = Column(String(500), default="")
    source_url = Column(String(1024), default="")
    raw_content = Column(Text, default="")
    translated_content = Column(Text, default="")
    translation_status = Column(String(50), default="pending", index=True) # pending, translating, completed, failed
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    novel = relationship("Novel", back_populates="chapters")

    __table_args__ = (
        Index("idx_novel_chapter_index", "novel_id", "chapter_index", unique=True),
    )

class Glossary(Base):
    __tablename__ = "glossaries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    novel_id = Column(Integer, ForeignKey("novels.id", ondelete="CASCADE"), nullable=False, index=True)
    source_term = Column(String(255), nullable=False)
    target_term = Column(String(255), nullable=False)
    category = Column(String(50), default="khac") # nhan_vat, canh_gioi, dia_danh, cong_phap, vat_pham, khac
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    novel = relationship("Novel", back_populates="glossaries")

    __table_args__ = (
        Index("idx_novel_source_term", "novel_id", "source_term"),
    )

class ScraperRule(Base):
    __tablename__ = "scraper_rules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    domain = Column(String(255), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    novel_title_selector = Column(String(255), default="")
    novel_author_selector = Column(String(255), default="")
    novel_cover_selector = Column(String(255), default="")
    novel_desc_selector = Column(String(255), default="")
    chapter_list_selector = Column(String(255), default="")
    chapter_link_selector = Column(String(255), default="")
    chapter_title_selector = Column(String(255), default="")
    chapter_content_selector = Column(String(255), default="")
    content_remove_selectors = Column(String(500), default="script,style,ins,ads,.ads,#ads,.advertisement")
    encoding = Column(String(50), default="auto") # auto, utf-8, gbk, gb18030

class AppSetting(Base):
    __tablename__ = "app_settings"

    key = Column(String(100), primary_key=True)
    value = Column(Text, default="")

class TranslationTask(Base):
    __tablename__ = "translation_tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    novel_id = Column(Integer, nullable=False, index=True)
    novel_title = Column(String(500), default="")
    chapter_index = Column(Integer, nullable=False)
    chapter_count = Column(Integer, default=1)
    status = Column(String(50), default="pending", index=True) # pending, in_progress, completed, failed
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
