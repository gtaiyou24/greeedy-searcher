from dataclasses import dataclass
from typing import Set

from domain.model.item.color import Color


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Colors:
    set: Set[Color]

    def __init__(self, set: Set[Color]):
        assert set is not None, "カラー一覧は必須です"
        assert isinstance(set, Set), "カラー一覧にはSet型を指定してください"
        super().__setattr__("set", set)
