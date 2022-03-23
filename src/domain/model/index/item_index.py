import abc
from typing import NoReturn, Set, Optional

from domain.model.gender import Gender
from domain.model.item import Item
from domain.model.item.id import ItemId
from domain.model.index import SearchHitItems, ItemIndexRow
from domain.model.query import QuerySet


class ItemIndex(abc.ABC):

    @abc.abstractmethod
    def add(self, item_index_row: ItemIndexRow) -> NoReturn:
        pass

    @abc.abstractmethod
    def get(self, item_id: ItemId) -> Item:
        pass

    @abc.abstractmethod
    def delete(self, item_id: ItemId) -> NoReturn:
        pass

    @abc.abstractmethod
    def search(self, gender: Gender, keyword: Optional[str],
               category_query_set: Optional[QuerySet], colors: Optional[Set[str]],
               designs: Optional[Set[str]], details: Optional[Set[str]],
               price_from: Optional[int], price_to: Optional[int],
               sort: str, start: int, size: int) -> SearchHitItems:
        pass
