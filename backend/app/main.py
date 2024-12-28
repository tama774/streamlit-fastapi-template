from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, item

# FastAPIインスタンスの作成
app = FastAPI(
    title="FastAPI Streamlit Template",
    description="A template project for building a FastAPI backend and Streamlit frontend.",
    version="1.0.0",
)

# CORS設定
origins = [
    "http://localhost",
    "http://localhost:8501",  # Streamlitフロントエンド用
    "http://localhost:14024",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターの登録
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(item.router, prefix="/items", tags=["Items"])

# ルートエンドポイント
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the FastAPI Streamlit Template!"}
