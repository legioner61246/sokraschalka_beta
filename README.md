# sokraschalka_beta

Простой и быстрый сервис для сокращения ссылок, написанный на Python (FastAPI).
-----------------------------------------------------------------------------------
Стек
- **Backend:** Python, FastAPI, Uvicorn
- **Деплой:** Docker
-----------------------------------------------------------------------------------
Структура 
- `silochki.py` — основной файл приложения
- `reqs.txt` — список зависимостей 
- `Dockerfile` — конфиг
-----------------------------------------------------------------------------------
Запуск локально

1. Клонировать репозиторий и перейти в папку проекта:
```bash
git clone [https://github.com/legioner61246/sokraschalka_beta.git](https://github.com/legioner61246/sokraschalka_beta.git)
cd sokraschalka_beta

python -m venv venv
# для linux/mac
source venv/bin/activate
#для windows (git bash)
source venv/Scripts/activate

pip install -r reqs.txt

uvicorn silochki:app --reload

2 Запуск через Docker
docker build -t sokraschalka .
docker run -d -p 8000:8000 --name sokraschalka_app sokraschalka