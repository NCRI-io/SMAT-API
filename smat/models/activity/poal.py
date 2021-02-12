# generated by datamodel-codegen:
#   filename:  sample.json
#   timestamp: 2021-02-12T20:18:50+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class _Shards(BaseModel):
    total: int
    successful: int
    skipped: int
    failed: int


class Total(BaseModel):
    value: int
    relation: str


class Hits(BaseModel):
    total: Total
    max_score: Any
    hits: List


class Bucket(BaseModel):
    key: str
    doc_count: int


class User(BaseModel):
    doc_count_error_upper_bound: int
    sum_other_doc_count: int
    buckets: List[Bucket]


class Aggregations(BaseModel):
    user: Optional[User] = None


class PoalActivity(BaseModel):
    took: int
    timed_out: bool
    _shards: _Shards
    hits: Hits
    aggregations: Optional[Aggregations] = None
    aggby_key: str
