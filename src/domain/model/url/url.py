import re
from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class URL:
    link: str

    def __init__(self, link: str):
        assert link, "URLは必須です"
        assert re.match(r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", link) is not None, "http,httpsから始まるURLを指定して下さい"
        super().__setattr__("link", link)
