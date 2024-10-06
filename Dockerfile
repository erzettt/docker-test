FROM python:3.12-slim as python-base

ENV port=4001

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential

WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4001"]