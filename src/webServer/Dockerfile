## ---------------------------- Builder Stage --------------------------- ##
FROM python:3.13.3-alpine AS builder

# Set the working directory of the container
WORKDIR /app

# Copy the project files
COPY requirements.txt /app/
COPY webServer /app/webServer

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

## ---------------------------- Production Stage --------------------------- ##
FROM python:3.13.3-alpine AS production

# Set the working directory of the container
WORKDIR /app

# Copy dependencies
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
# Copy the project files
COPY webServer /app/webServer

# Expose the Django port
EXPOSE 8000

# Run the app
CMD ["python", "webServer/manage.py", "runserver", "0.0.0.0:8000"]