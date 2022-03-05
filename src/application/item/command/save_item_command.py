from dataclasses import dataclass
from typing import List, Set


@dataclass(unsafe_hash=True, frozen=True)
class SaveItemCommand:
    @dataclass(unsafe_hash=True, frozen=True)
    class Meta:
        keywords: str
        description: str
        content: str

    item_id: str
    item_name: str
    brand_name: str
    price: int
    gender: str
    images: List[str]
    page_url: str
    meta: Meta
