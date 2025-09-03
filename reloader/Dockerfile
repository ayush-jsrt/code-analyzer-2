FROM python:3.12-bookworm

WORKDIR /app

# Copy application code
COPY main.py .

# Install dependencies (FastAPI/Starlette, Uvicorn, llama-cpp)
RUN pip install --no-cache-dir fastapi uvicorn llama-cpp-python

# Expose port and use volume for models
EXPOSE 8000
# (Optional) VOLUME /models  # not strictly required, see note below

# Launch the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]