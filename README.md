# REST API Task

Thanks to the time presure I got myself into, I've decided to use tools to help me with the speed of the delivery. The tools are:

- [CookieCutter - Django](https://github.com/pydanny/cookiecutter-django)
- [Django REST Framework](https://www.django-rest-framework.org/)

If this breaks the task description please let me know.

## Introduction
As you can see CookieCutter gave me the ability to have at least basic setup for CI, build processess, Celery and so on out of the box, but the most important reason for me to use it was the automated project setup using Docker.

Also the app contains user administration so it would be easy to clean the code a little and let users have their tasks.

Practically the only important stuff regarding the task is in the `api/` folder.

The endpoints themselves are generated thanks to the `djangorestframework` which supports `GET`, `POST`, `PUT` and `DELETE` methods on it's own and the endpoints (views) can be overwritten or we can add more.

## Build & Run

> ℹ️ The configuration is currently setup only for the local environment.

### Build

This will take a while on the first run 🙃

```bash
docker-compose -f local.yml build
```

### Run

```bash
docker-compose -f local.yml up
```

Now you can visit UI (where there's nothing really) on ports 3000 and 8000 and send API requests to `/api/tasks/` on the same ports
