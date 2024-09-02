# base
FROM python:3.12-slim as base-image

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi --without dev

COPY src .

# prod
FROM base-image as prod-image

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]

# dev
FROM base-image as dev-image

RUN poetry install --no-root --no-interaction --no-ansi --only dev

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
