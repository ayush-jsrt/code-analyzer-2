# ====== BUILDER STAGE ======
FROM python:3.11-slim AS builder

WORKDIR /app
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
