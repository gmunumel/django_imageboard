About this project
==================

This project was built using [virtual enviroments](http://www.openbookproject.net/courses/webappdev/units/webappdev2/resources/django_virtualenv.html). [Another source](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

The `HOME` of the working environment is in `$HOME/.virtualenvs (/home/<user>/.virtualenvsenv)`


Notice
------

This application use [Django Version 1.8](https://docs.djangoproject.com/en/1.8/releases/1.8/). If there is a problem you need to run the following command to install de requirements for the project:
  
      pip install -r requirements.txt


Useful db commands
------------------

* Connect to postgres

```
psql -u root
```

* Create Admin user

```
./manage.py createsuperuser --settings=imageboard.settings.local 
``` 

* Run server

```
./manage.py runserver PORT
```

* Delete all tables

```
./manage.py slqclear <my app> | ./manage.py dbshell
e.g: ./manage.py slqclear imageboard | ./manage.py dbshell
```

* Sync database

```
./manage.py migrate --settings=imageboard.settings.local 
```

* Load fixtures

```
./manage.py loaddata <fixture name> --settings=imageboard.settings.local 
e.g: ./manage.py loaddata tag
./manage.py loaddata image
./manage.py loaddata imagetag
```

* Reload indexes for searching

```
./manage.py rebuild_index --settings=imageboard.settings.local 
```

* Update indexes for search

```
./manage.py update_index --settings=imageboard.settings.local 
```

* Removing tabs
     
```
tr -d \\t < input > output
e.g: tr -d \\t < Image\ Fixtures\ -\ Sh\ -\ Sheet1.tsv  > Image\ Fixtures\ -\ Sh\ -\ Sheet1_notabs.tsv
```

* All (using local environment)

```
./manage.py sqlclear imageboard --settings=imageboard.settings.local | ./manage.py dbshell --settings=imageboard.settings.local && ./manage.py migrate --settings=imageboard.settings.local && ./manage.py loaddata tag --settings=imageboard.settings.local && ./manage.py loaddata image --settings=imageboard.settings.local && ./manage.py loaddata imagetag --settings=imageboard.settings.local && ./manage.py rebuild_index --settings=imageboard.settings.local
```

* All (using production environment, deployment to heroku)
      
```
heroku run './manage.py sqlclear imageboard --settings=imageboard.settings.production | ./manage.py dbshell --settings=imageboard.settings.production && ./manage.py migrate --settings=imageboard.settings.production && ./manage.py loaddata tag --settings=imageboard.settings.production && ./manage.py loaddata image --settings=imageboard.settings.production && ./manage.py loaddata imagetag --settings=imageboard.settings.production && ./manage.py rebuild_index --settings=imageboard.settings.production'
```
