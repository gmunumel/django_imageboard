Django Imageboard
=================

<img style="float: right" src="https://travis-ci.org/gmunumel/djangoimageboard.svg?branch=master">

Django application to manage and display images using some cool features. 


Features
-------

* Extremely fast search of files: use of [haystack engine](http://haystacksearch.org/) and [whoosh indexer](https://bitbucket.org/mchaput/whoosh/wiki/Home).
* Easy and efficient way to upload images: there is an implementation of [jquery fileupload](https://blueimp.github.io/jQuery-File-Upload/) using the application [django-jfu](https://github.com/Alem/django-jfu).
* Use of [Jquery](http://jqueryui.com/autocomplete/) to simplified the search in some fields.



Installation
-----------

* Clone my repository

```
git clone https://github.com/gmunumel/djangoimageboard.git
```

* Install needed dependencies

```
pip install -r requirements.txt 
```

* Start a clean database

```
python manage.py migrate --settings=imageboard.settings.local
```

* Load initial data using fixtures

```
python manage.py loaddata tag --settings=imageboard.settings.local
python manage.py loaddata image --settings=imageboard.settings.local
python manage.py loaddata imagetag --settings=imageboard.settings.local
```
    
* Create super user for administrative purposes

```
python manage.py createsuperuser --settings=imageboard.settings.local
```

Usage
-----

Enter to the administrative site by clicking on `Add new images` and then login. Click on `Files` option and click on `Add File` (right side). Then you will see the [jQuery fileupload](https://blueimp.github.io/jQuery-File-Upload/) functionality running. You can add many files at once, either clicking in `Add files...` or using drag&drop feature. Please notice that you must specific a valid folder. If you want to create a folder which cointains your images go to the `admin`'s index page and click on `Images`.

Troubleshooting 
---------------

In case you have any problem to run the application please refer to [README2.md](https://github.com/gmunumel/djangoimageboard/blob/master/README2.md) file.


Notice
------

There are warnings related to `haystack` and `django v1.8`. There is also an error related to [translation error](https://code.djangoproject.com/ticket/24569) when using `whoosh` indexer, it will fix it in `django v1.9`.


License
-------

Please read the whole License information located in [LICENSE.txt](https://github.com/gmunumel/djangoimageboard/blob/master/LICENSE.md) file.


Author
------

Gabriel Muñumel


