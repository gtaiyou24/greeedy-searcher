from __future__ import annotations

from enum import Enum
from typing import Dict, List

from domain.model.query import QuerySetInterest, QuerySet, Query


class BoolType(Enum):
    AND = "must"
    OR = "should"
    NOT = "must_not"


class MultiMatch:
    @staticmethod
    def of(query: Query, fields: List[str]) -> Dict:
        return {
            "multi_match": {
                "query": query.text,
                "operator": query.operator.value,
                "fields": fields
            }
        }


class QuerySetJsonMapper(QuerySetInterest):
    def __init__(self, fields: List[str]):
        self.fields = fields

    def to_query_from(self, payload: Dict) -> QuerySet:
        raise NotImplementedError()

    def to_payload_from(self, query_set: QuerySet) -> Dict:
        _bool = {}
        for operator, queries in query_set.all.items():
            _bool[BoolType[operator.name].value] = [MultiMatch.of(query, self.fields) for query in queries]
        return {"bool": _bool}
