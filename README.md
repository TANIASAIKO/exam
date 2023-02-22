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

## Dump data
```sh
./manage.py dumpdata > db.json
```

## Load data
```sh
./manage.py loaddata db.json
```
