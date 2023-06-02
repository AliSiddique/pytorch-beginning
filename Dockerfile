FROM python:alpine

# Path: /app
WORKDIR /app

# Path: /app
COPY . /app

# Path: /app
RUN pip install -r requirements.txt

# Path: /app
EXPOSE 5000

# Path: /app
ENTRYPOINT ["python"]



# Path: /app
CMD ["python","start.py"]
