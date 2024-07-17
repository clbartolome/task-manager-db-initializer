FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]