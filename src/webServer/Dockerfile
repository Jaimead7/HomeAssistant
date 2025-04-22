## ---------------------------- Builder Stage --------------------------- ##
FROM python:3.13.3-alpine AS builder

# Set the working directory
WORKDIR /app/webServer

# Copy project files
COPY . /app/webServer

# Setup uv
COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /uvx /bin/

# Install dependencies
RUN uv sync

## ---------------------------- Production Stage --------------------------- ##
FROM python:3.13.3-alpine AS production

# Set the working directory
WORKDIR /app/webServer

# Copy dependencies
COPY --from=builder /app/webServer/.venv /app/.venv

# Copy project files
COPY . /app/webServer

# Set up environment variables for production
ENV PATH="/app/.venv/bin:$PATH"

# Expose the Django port
EXPOSE 8000

# Run the app
CMD ["python3", "./webServer/manage.py", "runserver", "0.0.0.0:8000"]