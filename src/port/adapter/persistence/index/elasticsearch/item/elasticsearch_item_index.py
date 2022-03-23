import os
from typing import NoReturn, Optional, Set

from elasticsearch import Elasticsearch
from injector import inject

from domain.model.category import Category
from domain.model.gender import Gender
from domain.model.item import Item
from domain.model.item.id import ItemId
from domain.model.index import ItemIndex, ItemIndexRow, SearchHitItems
from domain.model.query import QuerySetInterest
from port.adapter.persistence.index.elasticsearch.credential import CredentialGetter
from port.adapter.persistence.index.elasticsearch.interest import QuerySetJsonMapper


class ElasticsearchItemIndex(ItemIndex):
    INDEX_NAME = "items_20220224"
    MAPPING = {
        "settings": {
            "analysis": {
                # 1. Character filters
                "char_filter": {
                    # 正規化を行う
                    "normalize": {
                        "type": "icu_normalizer",
                        "name": "nfkc",
                        "mode": "compose"
                    }
                },
                # 2. Tokenizer
                "tokenizer": {
                    # 形態素解析
                    "ja_kuromoji_tokenizer": {
                        "mode": "search",
                        "type": "kuromoji_tokenizer",
                        "discard_compound_token": True,
                        "user_dictionary": os.getenv("USER_DICTIONARY"),
                    },
                    # Nグラム
                    "ja_ngram_tokenizer": {
                        "type": "ngram",
                        "min_gram": 3,
                        "max_gram": 3,
                        "token_chars": [
                            "letter",  # 文字
                            "digit"    # 数字
                        ]
                    }
                },
                # 3. Token filters
                "filter": {
                    # インデックス時の同義語展開
                    "ja_index_synonym": {
                        "type": "synonym",
                        "lenient": False,
                        "synonyms": []
                    },
                    # 検索時の同義語展開
                    "ja_search_synonym": {
                        "type": "synonym_graph",
                        "lenient": False,
                        "synonyms_path": os.getenv("SYNONYMS_PATH"),
                        "updateable": True
                    }
                },
                # Analyzer
                "analyzer": {
                    # インデックス時のkuromojiアナライザー
                    "ja_kuromoji_index_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_kuromoji_tokenizer",
                        "filter": [
                            "kuromoji_baseform",
                            "kuromoji_part_of_speech",
                            "ja_index_synonym",
                            "cjk_width",
                            "ja_stop",
                            "kuromoji_stemmer",
                            "lowercase"
                        ]
                    },
                    # 検索時のkuromojiアナライザー
                    "ja_kuromoji_search_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_kuromoji_tokenizer",
                        "filter": [
                            "kuromoji_baseform",
                            "kuromoji_part_of_speech",
                            "ja_search_synonym",
                            "cjk_width",
                            "ja_stop",
                            "kuromoji_stemmer",
                            "lowercase"
                        ]
                    },
                    # インデックス時のNグラムアナライザー
                    "ja_ngram_index_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_ngram_tokenizer",
                        "filter": [
                            "lowercase"
                        ]
                    },
                    # 検索時のNグラムアナライザー
                    "ja_ngram_search_analyzer": {
                        "type": "custom",
                        "char_filter": [
                            "normalize"
                        ],
                        "tokenizer": "ja_ngram_tokenizer",
                        "filter": [
                            "ja_search_synonym",
                            "lowercase"
                        ]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "name": {
                    "type": "text",
                    "search_analyzer": "ja_kuromoji_search_analyzer",
                    "analyzer": "ja_kuromoji_index_analyzer",
                    "fields": {
                        "ngram": {
                            "type": "text",
                            "search_analyzer": "ja_ngram_search_analyzer",
                            "analyzer": "ja_ngram_index_analyzer"
                        }
                    }
                },
                "brand_name": {"type": "keyword"},
                "price": {
                    "type": "integer",
                    "meta": {
                        "currency": "yen"
                    }
                },
                "gender": {"type": "keyword"},
                "images": {"type": "keyword"},
                "page_url": {"type": "keyword"},
                "keywords": {
                    "type": "text",
                    "search_analyzer": "ja_kuromoji_search_analyzer",
                    "analyzer": "ja_kuromoji_index_analyzer"
                },
                "description": {
                    "type": "text",
                    "search_analyzer": "ja_kuromoji_search_analyzer",
                    "analyzer": "ja_kuromoji_index_analyzer",
                    "fields": {
                        "ngram": {
                            "type": "text",
                            "search_analyzer": "ja_ngram_search_analyzer",
                            "analyzer": "ja_ngram_index_analyzer"
                        }
                    }
                },
                "content": {
                    "type": "text",
                    "search_analyzer": "ja_kuromoji_search_analyzer",
                    "analyzer": "ja_kuromoji_index_analyzer",
                    "fields": {
                        "ngram": {
                            "type": "text",
                            "search_analyzer": "ja_ngram_search_analyzer",
                            "analyzer": "ja_ngram_index_analyzer"
                        }
                    }
                }
            }
        }
    }

    @inject
    def __init__(self, credential_getter: CredentialGetter):
        self.__credential_getter = credential_getter
        self.__category_json_mapper: QuerySetInterest = QuerySetJsonMapper(fields=['name^3', 'keywords'])
        self.__search_engine = Elasticsearch(
            self.__credential_getter.get_host(),
            http_auth=(
                self.__credential_getter.get_username(),
                self.__credential_getter.get_password()
            )
        )

        if not self.__search_engine.indices.exists(index=self.INDEX_NAME):
            self.__search_engine.indices.create(index=self.INDEX_NAME, body=self.MAPPING)

    def add(self, item_index_row: ItemIndexRow) -> NoReturn:
        document = {
            'name': item_index_row.item.item_name.text,
            'brand_name': item_index_row.item.brand_name.name,
            'price': item_index_row.item.price.yen,
            'gender': item_index_row.item.gender.name,
            'images': [url.link for url in item_index_row.item.images],
            'page_url': item_index_row.item.page_url.link,
            'keywords': item_index_row.meta.keywords.text,
            'description': item_index_row.meta.description.text,
            'content': item_index_row.meta.content.text,
        }
        self.__search_engine.index(index=self.INDEX_NAME, id=item_index_row.item.item_id.id, body=document)

    def get(self, item_id: ItemId) -> Item:
        doc = self.__search_engine.get(index=self.INDEX_NAME, id=item_id.id)
        _id = str(doc['_id'])
        source = doc['_source']
        return Item(_id, str(source['name']), str(source['brand_name']), int(source['price']),
                    str(source['gender']), list(source['images']), str(source['page_url']))

    def delete(self, item_id: ItemId) -> NoReturn:
        self.__search_engine.delete(index=self.INDEX_NAME, id=item_id.id)

    def search(self, gender: Gender, keyword: Optional[str],
               category: Optional[Category], colors: Optional[Set[str]],
               designs: Optional[Set[str]], details: Optional[Set[str]],
               price_from: Optional[int], price_to: Optional[int],
               sort: str, start: int, size: int) -> SearchHitItems:
        must = []

        # キーワード検索
        if keyword:
            must.append({
                'multi_match': {
                    'query': keyword,
                    'fields': ['name^2', 'name.gram', 'brand_name^2', 'keywords', 'description',
                               'description.ngram', 'content', 'content.ngram']
                }
            })

        # カテゴリ
        if category:
            must.append(self.__category_json_mapper.to_payload_from(category.query_set))

        # 柄・デザイン
        if designs:
            must.append({
                "multi_match": {
                    "query": " ".join(designs),
                    "fields": ["name^3", "keywords", "description", "content^2"]
                }
            })

        # こだわり
        if details:
            must.append({
                "multi_match": {
                    "query": " ".join(details),
                    "fields": ["name^3", "keywords^2", "description^2", "content^2"],
                }
            })

        filter = [
            # 性別
            {'term': {'gender': gender.name}}
        ]

        # カラー
        if colors:
            filter.append({
                "multi_match": {
                    'query': ' '.join(colors),
                    "fields": ["name", "name.ngram", "keywords", "description",
                               "description.ngram", "content", "content.ngram"]
                }
            })

        # 価格範囲
        if price_from and price_to:
            filter.append({'range': {'price': {'gte': price_from, 'lte': price_to}}})
        elif price_from:
            filter.append({'range': {'price': {'gte': price_from}}})
        elif price_to:
            filter.append({'range': {'price': {'lte': price_to}}})

        # 条件が指定されていない場合は全件取得される
        body = {
            "query": {
                "bool": {
                    # must: 配下の条件すべてを必須条件とする。検索結果のスコアに影響する。
                    "must": must,
                    # filter: 条件すべてを必須条件とする。検索結果のスコアに影響しない。
                    "filter": filter
                }
            }
        }

        search_result = self.__search_engine.search(
            index=self.INDEX_NAME,
            body=body,
            size=size,
            from_=start - 1
        )

        item_list = []
        for doc in search_result['hits']['hits']:
            _id = str(doc['_id'])
            source = doc['_source']

            item = Item(_id, str(source['name']), str(source['brand_name']), int(source['price']),
                        str(source['gender']), list(source['images']), str(source['page_url']))

            item_list.append(item)

        total_results_available = int(search_result['hits']['total']['value'])
        return SearchHitItems(total_results_available, item_list)
