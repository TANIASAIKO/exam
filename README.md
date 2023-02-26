# EXAM
Django and Python Exam Site


## Initialize  application

### Go to application folder
```sh
cd app
```

### Initialize environment
```sh
pip install virtualenvwrapper-win
mkvirtualenv examenv
workon examenv
python -m pip install -r requirements.txt
```

### Initialize database
```sh
python manage.py migrate
python manage.py createsuperuser
http://127.0.0.1:8000/init-cards
```



## Helpers

### Install virtualenv and virtualenvwrapper
```sh
pip install virtualenvwrapper-win
```

### Create project environment
```sh
mkvirtualenv examenv
```

### Turn on project environment
```sh
workon examenv
```

### Install django if necessary
```sh
python -m pip install Django
```

### Run app
```sh
cd ./app
python manage.py runserver
```

### Create superuser if necessary
```sh
python manage.py migrate
python manage.py createsuperuser
```

### Dump data
```sh
./manage.py dumpdata > db.json
```

### Load data
```sh
./manage.py loaddata db.json
```

### If you change models don't forget to do new migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Dump installed packages
```sh
python -m pip freeze > requirements.txt
```

### Load saved packages
```sh
python -m pip install -r requirements.txt
```
