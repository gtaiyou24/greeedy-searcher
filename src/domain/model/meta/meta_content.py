from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class MetaContent:
    text: str

    def __init__(self, text: str):
        assert text is not None, "コンテンツにNoneが指定されています"
        text = text.strip()
        super().__setattr__("text", text)
