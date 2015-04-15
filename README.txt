This project was built using virtual enviroments
  Source: http://www.openbookproject.net/courses/webappdev/units/webappdev2/resources/django_virtualenv.html
  http://docs.python-guide.org/en/latest/dev/virtualenvs/

  The HOME of the working environment is in $HOME/.virtualenvs (/home/<user>/.virtualenvsenv)

Using Django Version 1.8
  If there a problem you need to run the following command
  to install de requirements for the project
  
  pip install -r requirements.txt

Useful db commands

    > Connect to postgres
      psql -u root

    > Run server
      ./manage.py runserver PORT

    > Delete all tables
      ./manage.py slqclear <my app> | ./manage.py dbshell
      e.g: ./manage.py slqclear imageboard | ./manage.py dbshell

    > Sync database
    ./manage.py migrate

    > Load fixtures
      ./manage.py loaddata <fixture name>
      e.g: ./manage.py loaddata tag
          ./manage.py loaddata image
          ./manage.py loaddata imagetag


    > Reload indexes for searching
      ./manage.py rebuild_index


    > Update indexes for search
      ./manage.py update_index

    > Removing tabs
      tr -d \\t < input > output
      e.g: tr -d \\t < Image\ Fixtures\ -\ Sh\ -\ Sheet1.tsv  > Image\ Fixtures\ -\ Sh\ -\ Sheet1_notabs.tsv

    > All
      ./manage.py sqlclear imageboard | ./manage.py dbshell && ./manage.py migrate && ./manage.py loaddata tag && ./manage.py loaddata image && ./manage.py loaddata imagetag && ./manage.py rebuild_index 
