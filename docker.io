# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Expose the port on which the server will run (default port for http.server is 8000)
EXPOSE 8000

# Command to run the Python script serving "Hello, World!" via HTTP
CMD ["python", "-m", "http.server", "8000"]
