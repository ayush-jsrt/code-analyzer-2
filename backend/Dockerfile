FROM python:3.11-slim-bullseye AS builder

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
FROM debian:bullseye-slim

RUN apt-get purge -y sudo && \
    rm -f /bin/su /usr/bin/sudo || true && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -d /app/apiserveruser -s /usr/sbin/nologin apiserveruser

WORKDIR /app

COPY --from=builder /app/dist/apiserver .

RUN chown apiserveruser:apiserveruser /app/apiserver && \
    chmod 500 /app/apiserver && \
    chmod 555 /app

USER apiserveruser

EXPOSE 5000

ENTRYPOINT ["./apiserver"]
