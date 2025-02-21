FROM python:3.12-slim AS builder

WORKDIR /deps

RUN pip install poetry==1.8.3

ENV PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR \
    poetry install --no-root --no-ansi


FROM python:3.12-slim-bullseye AS prod

WORKDIR /app

ENV VIRTUAL_ENV=/deps/.venv \
PATH="/deps/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY src .

### Possible security improvements, will increase image size
# RUN groupadd -r appuser && useradd -r -g appuser appuser
# RUN chown -R appuser:appuser /app
# USER appuser

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]


FROM builder AS dev

ENV PATH="/deps/.venv/bin:$PATH"

RUN poetry install --no-root --no-interaction --no-ansi --with dev

COPY src .
