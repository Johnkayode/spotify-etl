#!/usr/bin/env bash

# Initialize db
airflow db upgrade

# Run webserver
airflow webserver