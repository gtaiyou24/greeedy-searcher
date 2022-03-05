from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Color:
    name: str

    def __init__(self, name: str):
        assert name, "カラー名は必須です"
        super().__setattr__("name", name)
