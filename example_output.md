# Test Project

## Local Setup

Create .env file

```bash
cp .env.example .env
```

Run Storage

```bash
docker compose up storage
```

Go to [http://127.0.0.1:9000/ui](http://127.0.0.1:9000/ui)

Create Bucket

Fill variables in .env file

- AWS_STORAGE_BUCKET_NAME
- AWS_S3_ACCESS_KEY_ID
- AWS_S3_SECRET_ACCESS_KEY

More info can be found [here](https://s3ninja.net/).

Build Project

```bash
docker compose build
```

Create superuser

Inside Python container execute command

```bash
python manage.py createsuperuser
```

Follow further instructions

## How to run tests

Inside python container

```bash
pytest
```

## Containers description
| Container name | Purpose |
|----------------|---------|
| python | main django application|
| postgres | database |
| scheduler | django_celery_beat scheduler |
| worker | celery worker |
| rabbitmq | celery message broker |
| storage | amazon s3 emulator |

