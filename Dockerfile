FROM python:3.10.7-slim-buster

WORKDIR /code
ENV TZ Europe/Stockholm
COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]