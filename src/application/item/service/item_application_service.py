from typing import Optional, Set, List

from injector import singleton, inject

from application.item.command import SaveItemCommand
from application.item.dpo import SearchHitItemsDpo, GetItemDpo, GetItemListDpo
from domain.model.category import CategoryRepository, CategoryId
from domain.model.gender import Gender
from domain.model.index import ItemIndex, ItemIndexRow
from domain.model.item import Item
from domain.model.item.id import ItemId, ItemIdFactory
from domain.model.meta import Meta
from domain.model.url import URL


@singleton
class ItemApplicationService:
    @inject
    def __init__(self, item_index: ItemIndex, category_repository: CategoryRepository):
        self.__item_index = item_index
        self.__category_repository = category_repository
        self.__item_id_factory = ItemIdFactory()

    def save(self, command: SaveItemCommand):
        _id: str = ""
        if not command.item_id:
            _id = self.__item_id_factory.make(URL(command.page_url)).id
        else:
            _id = command.item_id

        item = Item(_id, command.item_name, command.brand_name, command.price, command.description,
                    command.gender, command.images, command.page_url)
        meta = Meta(command.meta.keywords, command.meta.description)
        item_index_row = ItemIndexRow(item, meta)
        self.__item_index.add(item_index_row)

    def get(self, item_id: str) -> GetItemDpo:
        item_id = ItemId(item_id)
        item = self.__item_index.get(item_id)
        return GetItemDpo(item)

    def list(self, an_item_ids: List[str]) -> GetItemListDpo:
        items: List[Item] = [self.__item_index.get(ItemId(_id)) for _id in an_item_ids]
        return GetItemListDpo(items)

    def delete(self, item_id: str):
        item_id = ItemId(item_id)
        self.__item_index.delete(item_id)

    def search(self, gender: str, keyword: Optional[str], a_category_id: Optional[str],
               colors: Set[str], designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str = "relevance", start: int = 1, size: int = 20) -> SearchHitItemsDpo:

        category = None
        if a_category_id:
            category_id = CategoryId(a_category_id)
            category = self.__category_repository.category_of(category_id)

        search_hit_items = self.__item_index.search(Gender[gender], keyword,
                                                    category, colors,
                                                    designs, details,
                                                    price_from, price_to,
                                                    sort, start, size)
        return SearchHitItemsDpo(search_hit_items.total_results_available, search_hit_items.hits)
