# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the entire project folder into the container
COPY . /app/

# Install any necessary dependencies
RUN pip install apache-airflow psycopg2

# Expose the Airflow web UI port (optional)
EXPOSE 8080

# Define the command to run when the container starts
CMD ["airflow", "webserver", "-p", "8080"]