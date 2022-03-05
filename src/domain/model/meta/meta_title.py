from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class MetaTitle:
    text: str

    def __init__(self, text: str):
        assert text is not None, "メタタイトルにNoneが指定されています"
        text = text.strip()
        super().__setattr__("text", text)
