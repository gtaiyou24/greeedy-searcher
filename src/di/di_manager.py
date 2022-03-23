from typing import Type

from injector import Injector, T

from di import DI
from domain.model.category import CategoryRepository
from domain.model.index import ItemIndex

from port.adapter.persistence.index.elasticsearch.credential import CredentialGetter, LocalCredentialGetter
from port.adapter.persistence.index.elasticsearch.item import ElasticsearchItemIndex
from port.adapter.standalone.inmemories import InMemCategoryRepository


class DIManager:
    __injector = Injector([
        DI.new(CredentialGetter, {}, LocalCredentialGetter),
        DI.new(ItemIndex, {}, ElasticsearchItemIndex),
        DI.new(CategoryRepository, {}, InMemCategoryRepository),
    ])

    @classmethod
    def get(cls, interface: Type[T]) -> T:
        return cls.__injector.get(interface)
