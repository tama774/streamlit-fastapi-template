from fastapi import APIRouter, HTTPException
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not Found"}}
)

# ダミーデータベース（本番ではデータベースを使用）
dummy_users = {
    "admin": {"password": "password"}
}

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    print("hoge")
    user = dummy_users.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return LoginResponse(message="Login successful", username=request.username)
