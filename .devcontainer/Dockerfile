# Use the official Python image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /workspace

# Copy the current directory contents into the container at /workspace
COPY . /workspace

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install additional tools and utilities
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    && apt-get clean

# Expose any ports the app is expected to run on
EXPOSE 8000

# Command to run when the container starts
CMD ["python", "src/main.py"]

