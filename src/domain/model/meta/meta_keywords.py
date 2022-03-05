from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class MetaKeywords:
    text: str

    def __init__(self, text: str):
        assert text is not None, "メタキーワードにNoneが指定されています"
        text = text.strip()
        super().__setattr__("text", text)
