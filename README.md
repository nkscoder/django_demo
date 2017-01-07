# django_demo

Linux
Ubuntu

In this tutorial, we will install Django 1.10 on a Ubuntu 16.04 server. Django can be installed on a server in many ways, in this tutorial, I will show you 3 different ways to install Django:
Django installation with pip.
Install Django with virtualenv.
Install Django fron it's github repository.
When the Django installation is done, I will show you the first steps to start a new project with the Django web framework.
Django is a web application framework written in python that follows the MVC (Model-View-Controller) architecture, it is available for free and released under an open source license. It is fast and designed to help developers get their application online as quickly as possible. Django helps developers to avoid many common security mistakes like SQL Injection, XSS, CSRF and clickjacking. Django is maintained by the Django Software Foundation and used by many big technology companies, government, and other organizations. Some large websites like Pinterest, Mozilla, Instagram, Discuss, The Washington Post etc. are developed with Django.

Run the following command:
sudo apt-get install python-pip
pip install virtualenv
sudo apt-get install python-django
django-admin startproject demo
sudo apt-get install virtualenv
virtualenv venv
source venv/bin/activate
python manage.py runserver
pip install django==1.10
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
vi settings.py
django-admin startapp core
