FROM python:3.12-slim

WORKDIR /app

# Poetryのインストール
RUN pip install poetry

# Poetryで依存関係をインストール
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# アプリケーションのコピー
COPY . .

# Streamlitサーバー起動
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
