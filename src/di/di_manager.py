from typing import Type

from injector import Injector, T

from di import DI
from domain.model.index import ItemIndex

from port.adapter.persistence.index.elasticsearch.credential import CredentialGetter, LocalCredentialGetter
from port.adapter.persistence.index.elasticsearch.item import ElasticsearchItemIndex


class DIManager:
    __injector = Injector([
        DI.new(CredentialGetter, {}, LocalCredentialGetter),
        DI.new(ItemIndex, {}, ElasticsearchItemIndex),
    ])

    @classmethod
    def get(cls, interface: Type[T]) -> T:
        return cls.__injector.get(interface)
