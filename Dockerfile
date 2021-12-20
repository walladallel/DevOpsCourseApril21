FROM python:3.7-slim-buster
RUN apt update -y && apt install -y git
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]