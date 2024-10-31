# Use the Python 3.9 image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Environment variable to make Flask available externally
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port Flask is running on
EXPOSE 5000

# Use Gunicorn to run the app in production mode
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
