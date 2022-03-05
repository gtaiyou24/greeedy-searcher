from typing import Optional, Set

from injector import singleton, inject

from application.item.command import SaveItemCommand
from application.item.dpo import SearchHitItemsDpo, GetItemDpo
from domain.model.index import ItemIndex, ItemIndexRow
from domain.model.item import Item, Gender
from domain.model.item.id import ItemId, ItemIdFactory
from domain.model.meta import Meta
from domain.model.url import URL


@singleton
class ItemApplicationService:
    @inject
    def __init__(self, item_index: ItemIndex):
        self.__item_index = item_index
        self.__item_id_factory = ItemIdFactory()

    def save(self, command: SaveItemCommand):
        _id: str = ""
        if not command.item_id:
            _id = self.__item_id_factory.make(URL(command.page_url)).id
        else:
            _id = command.item_id

        item = Item(_id, command.item_name, command.brand_name, command.price,
                    command.gender, command.images, command.page_url)
        meta = Meta(command.meta.keywords, command.meta.description, command.meta.content)
        item_index_row = ItemIndexRow(item, meta)
        self.__item_index.add(item_index_row)

    def get(self, item_id: str) -> GetItemDpo:
        item_id = ItemId(item_id)
        item = self.__item_index.get(item_id)
        return GetItemDpo(item)

    def delete(self, item_id: str):
        item_id = ItemId(item_id)
        self.__item_index.delete(item_id)

    def search(self, gender: str, keyword: Optional[str], category: Optional[str],
               colors: Set[str], designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str = "relevance", start: int = 1, size: int = 20) -> SearchHitItemsDpo:

        search_hit_items = self.__item_index.search(Gender[gender], keyword,
                                                    category, colors,
                                                    designs, details,
                                                    price_from, price_to,
                                                    sort, start, size)
        return SearchHitItemsDpo(search_hit_items.total_results_available, search_hit_items.hits)
