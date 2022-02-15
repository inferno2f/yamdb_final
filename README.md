# API YAMDB
![yamdb workflow](https://github.com/inferno2f/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

API для получения информации и обсуждения наиболее интересных произведений

## Стэк технологий:
- Python
- Django Rest Framework
- Postgres
- Docker
### Документация и возможности API:
К проекту подключен redoc. Для просмотра документации используйте эндпойнт `redoc/`

### Квикстарт:

- Склонируйте репозитрий на свой компьютер
- Создайте `.env` файл в директории `infra/`, в котором должны содержаться следующие переменные:
    >DB_ENGINE=django.db.backends.postgresql\
    >DB_NAME= # название БД\
    >POSTGRES_USER= # ваше имя пользователя\
    >POSTGRES_PASSWORD= # пароль для доступа к БД\
    >DB_HOST=db\
    >DB_PORT=5432
- Из папки `infra/` соберите образ при помощи docker-compose
`$ docker-compose up -d --build`
- Примените миграции
`$ docker-compose exec web python manage.py migrate`
- Соберите статику
`$ docker-compose exec web python manage.py collectstatic --no-input`
- Для доступа к админке не забудьте создать суперюзера
`$ docker-compose exec web python manage.py createsuperuser`

## Команда, ответственная за проект:
- [Влад Никитин](https://github.com/inferno2f) - архитектура проекта, API регистрации и авторизации пользователей, контейнеризация
- [Екатерина Кирькова](https://github.com/kate-kirkova) - API отзывов и комментариев к произведениям