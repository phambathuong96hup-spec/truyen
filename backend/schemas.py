import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

# --- Novel Schemas ---
class NovelCreateFromUrl(BaseModel):
    url: str
    auto_detect: bool = True
    max_chapters: Optional[int] = Field(default=None, description="Max chapters to scrape initially, null for all")

class NovelCreateFromRaw(BaseModel):
    title: str
    author: Optional[str] = "Chưa rõ"
    description: Optional[str] = ""
    raw_text: str

class NovelProgressUpdate(BaseModel):
    last_read_chapter_id: Optional[int] = None
    last_read_index: Optional[int] = None
    scroll_position: Optional[float] = 0.0

class NovelResponse(BaseModel):
    id: int
    title: str
    author: str
    cover_url: str
    source_url: str
    description: str
    genre: str
    total_chapters: int
    last_read_chapter_id: Optional[int]
    last_read_index: int
    scroll_position: float
    translated_count: int = 0
    pending_count: int = 0
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True

# --- Chapter Schemas ---
class ChapterSummaryResponse(BaseModel):
    id: int
    novel_id: int
    chapter_index: int
    title: str
    title_translated: str
    translation_status: str
    updated_at: datetime.datetime

    class Config:
        from_attributes = True

class ChapterDetailResponse(BaseModel):
    id: int
    novel_id: int
    chapter_index: int
    title: str
    title_translated: str
    source_url: str
    raw_content: str
    translated_content: str
    translation_status: str
    error_message: Optional[str]
    prev_id: Optional[int] = None
    next_id: Optional[int] = None
    prev_index: Optional[int] = None
    next_index: Optional[int] = None
    prev_title: Optional[str] = None
    next_title: Optional[str] = None
    novel_title: Optional[str] = None
    total_chapters: Optional[int] = None

    class Config:
        from_attributes = True

class ChapterTranslateRequest(BaseModel):
    force: bool = False

class BatchTranslateRequest(BaseModel):
    start_index: int = 1
    count: int = 10
    all_remaining: bool = False

class BulkScrapeRequest(BaseModel):
    start_index: int = 1
    count: int = 50
    all_remaining: bool = False

# --- Glossary Schemas ---
class GlossaryItemCreate(BaseModel):
    source_term: str
    target_term: str
    category: str = "khac"
    notes: Optional[str] = ""

class GlossaryItemUpdate(BaseModel):
    source_term: Optional[str] = None
    target_term: Optional[str] = None
    category: Optional[str] = None
    notes: Optional[str] = None

class GlossaryItemResponse(BaseModel):
    id: int
    novel_id: int
    source_term: str
    target_term: str
    category: str
    notes: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True

class GlossaryBulkCreate(BaseModel):
    items: List[GlossaryItemCreate]

class GlossaryExtractSuggestion(BaseModel):
    source_term: str
    target_term: str
    category: str
    context: Optional[str] = ""

# --- Scraper Rule Schemas ---
class ScraperRuleBase(BaseModel):
    domain: str
    name: str
    novel_title_selector: str = ""
    novel_author_selector: str = ""
    novel_cover_selector: str = ""
    novel_desc_selector: str = ""
    chapter_list_selector: str = ""
    chapter_link_selector: str = ""
    chapter_title_selector: str = ""
    chapter_content_selector: str = ""
    content_remove_selectors: str = "script,style,ins,ads,.ads,#ads,.advertisement"
    encoding: str = "auto"

class ScraperRuleCreate(ScraperRuleBase):
    pass

class ScraperRuleResponse(ScraperRuleBase):
    id: int

    class Config:
        from_attributes = True

# --- Settings Schemas ---
class SettingsPayload(BaseModel):
    api_base_url: str
    api_key: Optional[str] = ""
    model_name: str
    temperature: float = 0.3
    system_prompt: str

class TestAiRequest(BaseModel):
    api_base_url: str
    api_key: Optional[str] = ""
    model_name: str
    test_prompt: Optional[str] = "你好，世界！"
