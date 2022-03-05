from __future__ import annotations

from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Price:
    yen: int

    def __init__(self, yen: int):
        assert isinstance(yen, int), "日本円にはint型を指定して下さい"
        assert yen > 0, "0円以上の価格を指定して下さい"
        super().__setattr__("yen", yen)
