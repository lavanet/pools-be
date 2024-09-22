# Use an official AWS Lambda base image for Python
FROM python:3.12.6-alpine3.20
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["./docker-entrypoint.sh"]
