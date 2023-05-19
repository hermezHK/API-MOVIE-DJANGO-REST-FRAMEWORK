## Step deployment 

## 1. Install

```bash
pip install gunicorn
pip install whitenoise
pip install dj-database-url
pip install psycopg2
```

## 2. copy static files && config staticfiles settings.py

```python
- run cli venv

python manage.py collectstatic
```

```python
- settings.py

import os

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


```

## 2. Create requirements

```bash
pip install > requirements.txt
```

## 3. Config whitenoise

```python
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]

- added staticfiles
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

## 4. Create Profile

```bash
web: python manage.py migrate && python manage.py collectstatic && gunicorn movies.wsgi
```

## 5. Create runtime.txt
- just write the python version
```python
3.11.0
```

## 5. Create DB in railway

using PostgreSQL
[railway.app](https://railway.app/)


```python
- settings.py

- import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default="sqlite://db.sqlite3")
}

```

```python
 - step install railway cli for windows
 
 - 5.1 - enable scoopy reading install railway cli run for windows in powershell or cmd
 - 5.2 -> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
 - 5.3 -> irm get.scoop.sh | iex
 - 5.4 -> scoop install railway
```

## 6. use cli railway in your cli projects venv
```python
- 6.1 -> railway login 
- 6.1 -> railway link 
- 6.1 -> railway service

- you need to add the variables manually before executing the command
- 6.1 -> railway variables 

```

##  7. use api projects
```bash
to use the api check the documentation in swagger click link in production
```
