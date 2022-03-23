from __future__ import annotations

from dataclasses import dataclass
from typing import List

from domain.model.category import Category


@dataclass(init=False, unsafe_hash=True, frozen=True)
class CategoryTree:
    current: Category
    children: List[CategoryTree]

    def __init__(self, current: Category, children: List[CategoryTree]):
        assert isinstance(current, Category), "currentにはCategoryを指定してください。(type={})".format(type(current))
        assert isinstance(children, List), "childrenにはList[CategoryTree]を指定してください。(type={})".format(type(children))
        super().__setattr__("current", current)
        super().__setattr__("children", children)
