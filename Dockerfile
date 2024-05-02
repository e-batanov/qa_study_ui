FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]