FROM python:3.9-slim

# Install required packages
RUN pip install -r requirements.txt

# Set environment variables from arguments
ARG ENDPOINT_URL
ARG ACCESS_KEY
ARG SECRET_KEY
ARG BUCKET_NAME
ARG DEST_PATH

ENV ENDPOINT_URL=$ENDPOINT_URL
ENV ACCESS_KEY=$ACCESS_KEY
ENV SECRET_KEY=$SECRET_KEY
ENV BUCKET_NAME=$BUCKET_NAME
ENV DEST_PATH=$DEST_PATH

# Copy the script into the container
COPY program.py /program.py

# Run the script
CMD ["python", "/program.py"]
