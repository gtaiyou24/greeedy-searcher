from __future__ import annotations

from typing import Set, Optional, List

from pydantic import BaseModel, Field


class RequestSaveItem(BaseModel):
    class Meta(BaseModel):
        keywords: str = Field(default="", description="メタ情報のキーワード")
        description: str = Field(default="", description="メタ情報の説明文")
        content: str = Field(default="", description="HTMLのコンテンツ")

    item_id: Optional[str] = Field(default=None, description="アイテムID。未指定の場合はIDを自動生成します。")
    item_name: str = Field(description="アイテム名")
    brand_name: str = Field(description="ブランド名")
    price: int = Field(description="価格")
    gender: str = Field(description="性別")
    images: List[str] = Field(description="アイテムの画像一覧")
    page_url: str = Field(description="アイテムのページURL")
    meta: RequestSaveItem.Meta
