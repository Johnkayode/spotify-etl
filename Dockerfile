#Use the official Airflow base image as the starting point
FROM apache/airflow:slim-2.6.1

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt


# Set environment variables
ENV AIRFLOW_HOME=/usr/local/airflow

USER root
RUN mkdir /usr/local/airflow/
RUN mkdir /usr/local/etl-pipeline

# Copy the DAGs and other files to the container
COPY ./ /usr/local/etl-pipeline

# Change the working directory
WORKDIR /usr/local/etl-pipeline

# Change ownership of the /usr/local/airflow directory and its contents
RUN chown -R airflow: /usr/local/airflow

USER airflow
