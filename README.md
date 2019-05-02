## Setting up a Python server using Django Framework
### Serve a Blog site with features as follows:

1. Authentication and registrartion
2. Admin privileges
3. Update profile
4. Checkout feed updates
5. Post and edit blogs

____

Firstly instal the django library in you Python environment
> pip install django

Using the django-admin command create a new Django Project
> django-admin startproject PROJECT_NAME

Note - Hyphen ' - ' characters not allowed

Django will automatically create a configuration folder and some Python files to get started with

____

## Initial Project structure

Command to display the project structure
> tree

manage.py - Execute command line arguments. Mostly unchanged throughout the project

PROJECT_NAME subfolder:

1. __ init__.py : Package file for Django project. Empty as of now
2. settings.py : Configuration file for web server
3. urls.py : This file is used for URL mappings. By default defines admin/ URL path.
4. wsgi.py : Interface between Python web application and the web server.Mostly untouched throughout the project

---

## Run the server

No need to write additional code for inital server setup like in the cask of 'Flask'. Instead simply use a command on the manage.py file to start the server:
> python manage.py runserver

On running the server following warnings are thrown :
> You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions., sessions.

To resolve this type the command (explained later on): 
> python manage.py migrate

The URL displayed on the console through which we can navigate through the web app
>  http://127.0.0.1:8000 or https://localhost:8000

This is the preview image for the above url

![](https://raw.githubusercontent.com/fardeen9983/images/master/django-initial.png)

Default admin route :
> http://localhost:8000/admin

Use Ctrl^C to stop the server

---

## Adding Apps to Django web app
To be clear, we have already created our web project. To add an app is similar to adding a section to the website. We can add multiple apps to single web project or add the same app across muliple web proects.

The commad to create an app:
> python manage.py startapp blog

Here blog is the name of the app we have added to our web project

___
## Proect app structure
1. views.py : Used to handle URL requests and render appropriate response on browser