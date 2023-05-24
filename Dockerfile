FROM python:3.11.3-slim-buster

# Copy the framework
WORKDIR /test_auto
COPY . .

# Install requirements
RUN pip install -r requirements.txt

# Create instructions on how to run tests
ENTRYPOINT [ "pytest" ]
