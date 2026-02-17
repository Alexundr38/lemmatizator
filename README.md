# lemmatizator

Лемматизатор на базе OpenCorpora

Для поднятия базы данных:

```
docker-compose up -d
```

Для запуска программы:

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 -m src.lemmatizator
```