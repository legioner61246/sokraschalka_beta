FROM python:3.10-slim

WORKDIR /app

COPY reqs.txt .
RUN pip install --no-cache-dir -r reqs.txt

COPY . .

CMD ["uvicorn", "silochki:app", "--host", "0.0.0.0", "--port", "8000"]