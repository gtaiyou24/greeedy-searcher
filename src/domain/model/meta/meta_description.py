from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class MetaDescription:
    text: str

    def __init__(self, text: str):
        assert text is not None, "メタディスクリプションにNoneが指定されています"
        text = text.strip()
        super().__setattr__("text", text)
