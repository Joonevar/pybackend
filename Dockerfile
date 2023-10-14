# Use a more lightweight base image
FROM python:3.11.6-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy your application code
COPY ./myappv2 ./

# Copy the "wait-for-it" script
#COPY wait-for-it.sh /usr/local/bin/

# Update and install system dependencies and packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libglib2.0-0 \
        libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt --no-cache-dir

# Make the "wait-for-it" script executable
#RUN chmod +x /usr/local/bin/wait-for-it.sh

# Remove unnecessary packages and cache to reduce image size
RUN apt-get remove --purge -y && apt-get autoremove -y && apt-get clean

# Specify the command to run your application
CMD ["gunicorn", "real_estate.wsgi:application","--bind","0.0.0.0:8000"]

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


