# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy project files
COPY . /app/
# Run server with gunicorn
CMD ["gunicorn", "ArafaBE.wsgi:application", "--bind", "0.0.0.0:8000"]
