from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Description:
    text: str

    def __init__(self, text: str):
        super().__setattr__("text", text)
