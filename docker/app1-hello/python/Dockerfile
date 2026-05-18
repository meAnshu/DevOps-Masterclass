# ──────────────────────────────────────────────
# Stage 1: Build & install dependencies
# ──────────────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

# Install dependencies into a separate location for copying
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ──────────────────────────────────────────────
# Stage 2: Production image
# ──────────────────────────────────────────────
FROM python:3.12-slim AS prod

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy application source
COPY main.py .

# Run as non-root user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

EXPOSE 3000

CMD ["python", "main.py"]
