from hashlib import sha256

from domain.model.item.id import ItemId
from domain.model.url import URL


class ItemIdFactory:
    def make(self, url: URL) -> ItemId:
        hash = sha256(url.link.encode('utf-8')).hexdigest()
        return ItemId(hash)
