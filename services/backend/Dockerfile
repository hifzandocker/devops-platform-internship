FROM python:3.14-slim AS builder

WORKDIR /build

COPY app.py .


FROM python:3.14-slim AS runtime

WORKDIR /app

COPY --from=builder /build/app.py .

RUN useradd --uid 1001 --create-home appuser

USER 1001

EXPOSE 8081

CMD ["python", "app.py"]
