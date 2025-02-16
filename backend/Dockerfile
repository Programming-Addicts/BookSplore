# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .
COPY .env .env

EXPOSE 8000

# Specify the command to run your Python program
CMD ["uvicorn", "main:app"]
