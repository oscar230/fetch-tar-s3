FROM python:3.9-slim

# Install required packages
RUN pip install -r requirements.txt

# Copy the program into the container
COPY program.py /program.py

# Run the program
CMD ["python", "/program.py"]

