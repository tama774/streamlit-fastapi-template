FROM python:3.12-slim

WORKDIR /app

# Poetryのインストール
RUN pip install poetry

# Poetryでプロジェクトの依存関係をインストール
COPY ../pyproject.toml ../poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# アプリケーションのコピー
COPY . .

# サーバー起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
