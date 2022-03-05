from dataclasses import dataclass

from domain.model.item import Item
from domain.model.meta import Meta


@dataclass(init=False, eq=False, unsafe_hash=True, frozen=True)
class ItemIndexRow:
    item: Item
    meta: Meta

    def __init__(self, item: Item, meta: Meta):
        super().__setattr__("item", item)
        super().__setattr__("meta", meta)

    def __eq__(self, other):
        if not isinstance(other, ItemIndexRow) or other is None:
            return False
        return other.item.item_id == self.item.item_id
