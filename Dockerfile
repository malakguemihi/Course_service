# Step 1: Base image with Python
FROM python:3.11-slim

# Step 2: Set work directory
WORKDIR /app

# Step 3: Install system dependencies (Postgres client for psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 5: Copy project code
COPY . .

# Step 6: Set environment variable for production settings
ENV DJANGO_SETTINGS_MODULE=myproject.settings_prod

# Step 7: Collect static files
RUN python manage.py collectstatic --noinput

# Step 8: Expose port
EXPOSE 8000

# Step 9: Run the server with Gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
