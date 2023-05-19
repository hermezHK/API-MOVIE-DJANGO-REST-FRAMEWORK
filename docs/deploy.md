## Step deployment 

## 1. Install

```bash
pip install gunicorn
pip install django-environ
```

## 2. Create requirements

```bash
pip install > requirements.txt
```

## 3. Create Profile

```bash
web: python manage.py migrate && gunicorn movies.wsgi
```

## 4. Create DB in railway

using Mysql
[railway.app](https://railway.app/)

