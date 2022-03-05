from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from application.item.dpo import GetItemDpo


class GetItemJson(BaseModel):
    id: str = Field(title="アイテムID")
    name: str = Field(title="アイテム名")
    brand_name: str = Field(title="ブランド名")
    price: int = Field(title="価格")
    gender: str = Field(title="性別")
    images: List[str] = Field(default=[], title="画像URL一覧")
    page_url: str = Field(title="アイテムのページURL")

    @staticmethod
    def make_by(dpo: GetItemDpo) -> GetItemJson:
        item = dpo.item
        return GetItemJson(id=item.item_id.id, name=item.item_name.text, brand_name=item.brand_name.name,
                           price=item.price.yen, gender=item.gender.name, images=[url.link for url in item.images],
                           page_url=item.page_url.link)
