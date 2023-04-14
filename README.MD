### Simple Chat Django

Simple Chat Django is a Django project with two apps: accounts and chats. It provides Django REST framework endpoints for creating user accounts, managing chat threads, and exchanging messages. The project uses SQLite as the default database backend and requires Django version 4.2 or later.

**Docker
**

` docker build .`

`docker-compose up -d`

## You can use Django REST Swagger


`http://127.0.0.1:8000/swagger/`

## Importing the Data

Fixtures: simple_chat.json
`python3 manage.py loaddata "simple_chat.json"`

# Endpoints

The following REST endpoints are provided by the project:

## JWT token
`POST /api/token/`

Takes a set of user credentials and returns an access and refresh JSON web

`POST /api/token/refresh/`

Takes a refresh type JSON web token and returns an access type JSON web

## Register user

`POST /register/`

## Threads

`POST /api/threads/`

## Messages
`POST /api/messages/`

## Register user

`POST /api/register/`

## Delete a thread

`DELETE /api/threads/<thread_id>/delete/`

## Count unread messages
`GET /api/unread/`

## List of threads for specific user
`GET /api/threads/<user_id>/`

## Tests
`docker-compose exec web python manage.py test
`
