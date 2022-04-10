from dataclasses import dataclass

from domain.model.meta import MetaKeywords, MetaDescription, MetaContent


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Meta:
    keywords: MetaKeywords
    description: MetaDescription

    def __init__(self, keywords: str, description: str):
        super().__setattr__("keywords", MetaKeywords(keywords))
        super().__setattr__("description", MetaDescription(description))
