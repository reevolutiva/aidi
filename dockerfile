FROM python:3.9.18

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "run.py"]