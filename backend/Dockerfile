FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apiserver.py .

RUN pip install pyinstaller
RUN pyinstaller --onefile apiserver.py

# ====== FINAL STAGE ======
FROM alpine:latest
WORKDIR /app

COPY --from=builder /app/dist/apiserver .

EXPOSE 5000

CMD ["./apiserver"]
