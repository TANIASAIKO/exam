# exam
Site on django and Python

## Install virtualenv and virtualenvwrapper
```sh
pip install virtualenvwrapper-win
```

## Create project environment
```sh
mkvirtualenv examenv
```

## Turn on project environment
```sh
workon examenv
```

## Install django if necessary
```sh
python -m pip install Django
```

## Run app
```sh
cd ./app
python manage.py runserver
```

## Create superuser if necessary
```sh
python manage.py migrate
python manage.py createsuperuser
```

Superuser by  default
username: user
password: pass

## Dump data
```sh
./manage.py dumpdata > db.json
```

## Load data
```sh
./manage.py loaddata db.json
```

## If you change models don't forget to do new migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

## Dump installed packages
```sh
python -m pip freeze > requirements.txt
```

## Load saved packages
```sh
python -m pip install -r requirements.txt
```
