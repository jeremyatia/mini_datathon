FROM python:3.8.13-slim

WORKDIR /mini_datathon
RUN yes | apt-get update
RUN yes | apt install build-essential

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501

COPY . .

CMD ["python", "main.py"]