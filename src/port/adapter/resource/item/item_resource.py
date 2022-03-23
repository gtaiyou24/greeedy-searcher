from typing import Set, Optional

from fastapi import APIRouter

from application.item.command import SaveItemCommand
from application.item.service import ItemApplicationService
from di import DIManager
from port.adapter.resource.item.request import RequestSaveItem
from port.adapter.resource.item.response import SearchHitItemsJson, GetItemJson

router = APIRouter(
    prefix="/items",
    tags=["商品系"]
)

item_application_service = DIManager.get(ItemApplicationService)


@router.get("/search", response_model=SearchHitItemsJson, name="アイテム検索機能",
            description="クエリ指定でインデックスに検索し、該当アイテムを返却します。")
def search(gender: str, keyword: Optional[str] = None,
           category_id: Optional[str] = None, colors: Optional[str] = None,
           designs: Optional[str] = None, details: Optional[str] = None,
           price_from: Optional[int] = None, price_to: Optional[int] = None,
           sort: str = "relevance", start: int = 1, size: int = 20) -> SearchHitItemsJson:

    # カラー
    if colors is not None:
        colors = colors.split(",")
    else:
        colors = set()

    # 柄・デザイン
    if designs is not None:
        designs = designs.split(",")
    else:
        designs = set()

    # こだわり
    if details is not None:
        details = details.split(",")
    else:
        details = set()

    search_hit_items_dpo = item_application_service.search(gender, keyword,
                                                           category_id, colors,
                                                           designs, details,
                                                           price_from, price_to,
                                                           sort, start, size)
    return SearchHitItemsJson.make_by(search_hit_items_dpo, start)


@router.post("", name="アイテム保存機能")
def save(request: RequestSaveItem):
    command = SaveItemCommand(
        item_id=request.item_id,
        item_name=request.item_name,
        brand_name=request.brand_name,
        price=request.price,
        gender=request.gender,
        images=request.images,
        page_url=request.page_url,
        meta=SaveItemCommand.Meta(
            keywords=request.meta.keywords,
            description=request.meta.description,
            content=request.meta.content
        )
    )
    item_application_service.save(command)


@router.get("/{item_id}", response_model=GetItemJson, name="アイテム取得機能")
def get(item_id: str) -> GetItemJson:
    dpo = item_application_service.get(item_id)
    return GetItemJson.make_by(dpo)


@router.delete("/{item_id}", name="アイテム削除機能")
def delete(item_id: str):
    item_application_service.delete(item_id)
