# ──────────────────────────────────────────────
# Stage 1: Install dependencies
# ──────────────────────────────────────────────
FROM node:22-alpine AS deps

WORKDIR /app

# Copy only package files first (better layer caching)
COPY package.json package-lock.json* ./

RUN npm install --omit=dev

# ──────────────────────────────────────────────
# Stage 2: Production image
# ──────────────────────────────────────────────
FROM node:22-alpine AS prod

WORKDIR /app

# Copy installed dependencies from deps stage
COPY --from=deps /app/node_modules ./node_modules

# Copy application source
COPY . .

# Run as non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000

CMD ["node", "app.js"]
