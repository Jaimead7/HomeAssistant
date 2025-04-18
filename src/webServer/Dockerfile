# Base image
FROM python:3.13.3-alpine

# Create app directory
RUN mkdir /app

# Set the working directory of the container
WORKDIR /app

# Copy the project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Django port
EXPOSE 8000

# Run the app
CMD ["python", "webServer/manage.py", "runserver", "0.0.0.0:8000"]