# Use official Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip wheel
RUN pip install -r requirements.txt

# Copy app source code
COPY . .

# Expose port (Flask default)
EXPOSE 5000

# Command to run the app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
