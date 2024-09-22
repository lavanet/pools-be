# Use an official AWS Lambda base image for Python
FROM public.ecr.aws/lambda/python:3.12-x86_64
COPY django .
RUN pip install -r requirements.txt
CMD ["config.lambda.handler"]
