FROM python:3.6.14-alpine

RUN pip install fastapi uvicorn

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "60000"]
