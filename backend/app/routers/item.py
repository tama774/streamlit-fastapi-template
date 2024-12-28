from fastapi import APIRouter, HTTPException

router = APIRouter()

# サンプルアイテムデータ
items = {
    1: {"name": "Item One", "description": "This is item one."},
    2: {"name": "Item Two", "description": "This is item two."}
}

@router.get("/")
async def list_items():
    """
    すべてのアイテムをリスト表示するエンドポイント。
    """
    return {"items": items}

@router.get("/{item_id}")
async def get_item(item_id: int):
    """
    特定のアイテムを取得するエンドポイント。
    """
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": item}

@router.post("/")
async def create_item(name: str, description: str):
    """
    新しいアイテムを作成するエンドポイント。
    """
    item_id = max(items.keys()) + 1 if items else 1
    items[item_id] = {"name": name, "description": description}
    return {"message": "Item created", "item_id": item_id}
