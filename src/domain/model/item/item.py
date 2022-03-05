from __future__ import annotations

from dataclasses import dataclass
from typing import List

from domain.model.item import ItemName, Gender, Price, BrandName
from domain.model.item.id import ItemId
from domain.model.url import URL


@dataclass(init=False, eq=False, unsafe_hash=True)
class Item:
    item_id: ItemId
    item_name: ItemName
    brand_name: BrandName
    price: Price
    gender: Gender
    images: List[URL]
    page_url: URL

    # NOTE: 今後は、系統/サイズ/在庫/レビューを追加する

    def __init__(self, id: str, name: str, brand_name: str, price: int, gender: str, images: List[str], page_url: str):
        super().__setattr__("item_id", ItemId(id))
        super().__setattr__("item_name", ItemName(name))
        super().__setattr__("brand_name", BrandName(brand_name))
        super().__setattr__("price", Price(price))
        super().__setattr__("gender", Gender[gender])
        super().__setattr__("images", [URL(image) for image in images])
        super().__setattr__("page_url", URL(page_url))

    def __eq__(self, other: Item):
        if not isinstance(other, Item) or other is None:
            return False
        return self.item_id == other.item_id
