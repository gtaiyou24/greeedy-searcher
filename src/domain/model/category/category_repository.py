import abc
from typing import List

from domain.model.category import CategoryTree
from domain.model.gender import Gender


class CategoryRepository(abc.ABC):
    @abc.abstractmethod
    def category_tree(self, gender: Gender) -> List[CategoryTree]:
        pass
