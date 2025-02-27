# Yatube
## _Лучшая соцсеть в мире! Мы вернули стену Дурова!_

[![N|Solid](https://static.djangoproject.com/img/icon-touch.e4872c4da341.png)](https://nodesource.com/products/nsolid)

## Возможности проекта:

- Регистрация и авторизация
- Публикование постов, комментариев к ним.
- Подписка на любимых авторов.
- Создание сообществ с помощью групп.
И всё это с помощью API запросов!

## Стек использованных технологий:

- [Django](https://www.djangoproject.com/) - бесплатный и свободный фреймворк для веб-приложений, написанный на Python.
- [Django REST Framework](https://www.django-rest-framework.org/) - мощный набор инструментов для создания веб-сервисов и API на основе фреймворка Django
- [SQLite](https://www.sqlite.org/) - компактная встраиваемая СУБД.
- [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html) - Реализация авторизации по токенам в DRF.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:warqone/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов и ответов:

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| URL | METHOD | BODY | RESPONSE
| ------ | ------ | ------- | ------- |
| /api/v1/jwt/create/ | POST | {"username": "admin","adminpassword": "string"} | {"refresh":"key", "access": "api_key"} |
| /api/v1/posts/ | POST  | {"text": "string","image": "string","group": 0} | {"id": 0,"author": "string","text": "string","pub_date": "2025-02-27T05:50:46.416Z","image": "string","group": 0} |
| /api/v1/posts/{post_id}/comments/ | GET | - | {"id": 0,"author": "string","text": "string","created": "2025-02-27T05:53:00.817Z","post": 0} |

##### Все примеры запросов можете посмотреть в [документации API](https://localhost:8000/redoc).

## Автор: [warqone](https://github.com/warqone)
За прекод спасибо: [evi1ghost](https://github.com/evi1ghost)
За ревью спасибо: [Port-tf](https://github.com/Port-tf)
