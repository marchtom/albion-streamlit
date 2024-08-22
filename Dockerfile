FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
COPY src .

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "main.py"]
