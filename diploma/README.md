## Ведется разработка сайта интернет-магазина




## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:
```bash
pip install -r requirements.txt
```
Данные можно загрузить коммандой: `python3 manage.py loaddata app.json`

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python3 manage.py migrate
```

* Команда для запуска приложения
```bash
python3 manage.py runserver
```

* При создании моделей или их изменении необходимо выполнить следующие команды:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
* Для вызова команд в WINDOWS заместо python3 используйте python
