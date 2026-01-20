# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set PYTHONPATH so src/shared is accessible
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Command ran by default - can be overridden
CMD ["python", "manage.py", "run", "1"]
