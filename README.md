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
2. urls.py: Mapping URL patterns to methods for this app
---
## HTML Templates
It is combersome to write down HTML response for each of the URL request. Sure we can deliver static web pages when needed, but things complicate when we need to deliver dynamic content.

For this templates are used.

Create a templates directory in 'blog' app root directory where all the templates will be stored. 

Actual path for templates:
> blog -> templates -> *.html

Next add our App configuration to the settings.py file of root web app, so that Django can look up for the templates for our app. The app config is stored in the apps.py file of the app directory. Add this configuration path to the settings.py file's INSTALLED_APPS list.

Next we can deliver content to the templates dynamically and embed Python code in HTML files using Jinja template synatx.
1. {% .... %} : Place python code in this manner
2. {{ ... }} : Used to print anything placed inside

Templates have the feature of inheritance. i.e, it is possible to create a template containing the content of the base template and adding your own. This is done through
> {% extends "base_template file" %}

Then we can define a block in the base template using:
> {% block content %} ... {% endblock %}

Whatever we write in the inherited templates as a block container, it will replace the container in the base template and render it

___
## Using static files like css
All the static resources such as css and js files can be used in the django web application by placing them in subfolder 'static' in our app root directrory.
> blog -> static -> *.css, etc 

To load the static files in templates:
> {% load static %}

And then simply include/link the static file in your template

To avoid rewriting URLs whenever we cahnge them across all files using them we can simply access it using template syntax.So url for blog home ("" - route ) : 
> {% url "blog-home" %} 

 Alias for blog root url : "blog-home" from urlspattern in urls.py

 ---
 ## Create an admin for Django web project
 First of all this will require one to create a Database for the web project with a admin_user table.

 To resolve this we need to run some migrations:
> python manage.py makemigrations

The message we get:
>No changes detected

This is because we have not yet created any tables/DB.

This still doesn't make any changes. To make the migrations:
>python manage.py migrate

 Now create the superuser. Use the command
 > python manage.py createsuperuser

 Specify the username, email and password and you are done. You can access the admin page from the ' /admin ' route

 ---
 ## Working with databases
 Django has it's own ORM (object relational mapping) tool which allows interaction with databases though object oriented manner abstracting the native structure of the DB without changing the code.

 Databases in Django are handles as classes called models. These models are placed in the models.py file in the app's directory.

After creating these models or making changes to them so as to update the database, we have to rerun the migrations. This would create a py files in the migration folders describing in detail the model creation and modification operations.

To view the SQL code that actually runs behind the migration use the command:
>python manage.py sqlmigrate APP_NAME MIGRATE_CODE

The migrate code is actually the number prefix of the migration file created. Ex:
> python manage.py sqlmigrate blog 0001

Finally run the migrate command to apply the migrations.

So migrations play a big role in abstracting Database and SQL operations.

---
## Running Django project from python command shell
Command:
>python manage.py shell
---
## Querysets
Django provides a pretty easy way to execute queries on model. For ex, if we fant to fetch all the posts made by a user all we hade to do is:
>user.post_set

Note - user is an instance of User mod. The following code wont work on the model itself.

This return a RelatedManager on which we can apply other queries like :

1. Get all the posts made by user : User.post_Set.all( )
2. Create a new post : User.post_set.create( post_paramas ), no need to set up author.
---
## Set up Post model on admin route 
This allows us to add, delete and modify Posts just like we do with Users and Groups.

To do so we need to register our model in admin.py file of the app directory

Django template date formating
>https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#date
___
## Create login page with input validation and user registration

Create a new app for handling user logic
> python manage.py startapp users

Django already has form classes such as for User creation which can be rendered as HTML forms. 
> django.contrib.auth.forms

To protect against CSRF scripting attack each form in Django web app passes a CSRF token.

Now to add extra fields to the form like Email addresses we would have to create a new one by extending the previous one. We need to first create a folder 'forms' in the root directory of the app and add a forms.py file

---
## Crispy Forms
Easily manage forms in HTML. Is compatible with other styling libraries

Installation:
>pip install django-crispy-forms

Add this as an installed app insettings.py
> ' crispy_forms '

By default it uses Bootstrap-2 CSS framework which is pretty old. So we can specify the CSS framework to use in the same settings.py file. At the end of that file, create a new configuration.
> CRISPY_TEMPLATE_PACK = 'bootstrap4'

Or any other CSS framework

To use crispy_forms in templates load it:
>{% load crispy_forms_tags %}
___
## Using inbuilt views : Login Page
Django has a library of views we can render as web pages like creating a login page without any hassle.

The login page view is stored in django.contrib.auth package
Add the login and logout view to respective URLs.
But as of now these views do not have predefined templates so they cannot be directly accessed. We would have to create our own templates for each view

Upon successfull login the browser tries calling the /account/profile route which does not exist as of now. But we would like to modify this to our preferred route by modifying the settings.py file.

Add the configuration:
>LOGIN_REDIRECT_URL = "blog-home"

If we do not specify Logout template Django will use the defalt Djando admin logout template.

Django specifies a global User variable that stores information of the current user whether he is logged in or not.

We can also specify that a route can only be accessed by authenticated users. For this we can use the login_required decorator annotation on the route. This will redirect the user to login pafe and bring them back to the desired page after login.

___
## Update the default User model to have features like photos

Create a Profile model extending the User model and adding extra features. To make the model use an image field we need to install Pillow module as well.
>pip install Pillow

Run migrations for the new model and apply them

We can specify the particular directory and URL for all our media files by adding the following in the settings.py file:
 > MEDIA_ROOT = 'path to the desried directory'

 > MEDIA_URL = ' public URL to access the MEDIA directory'
 ---
 ## Adding static media during development
 In the urls.py file of root project, to the urlpatterns add this:
 > urlpatterns = [ ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 This is not suitable for production phase.

 When no profile image is added for an user we can specify the default image by placing the image of same name in MEDIA_ROOT directory.
 
---
## Django Signals 
We can configure signals to respond to events such as model instantiation and perform some operation based on that. 

One entity is responsible for sending signals. like a USer model when it is created can cause a signal generation. Similarly a function will act like a reciever to this signal and performs some task.

After defining the signals, recievers and senders we need to register them in apps.py file of the app as a part of ready function of the app config class.

---
## User Update form
To update the user details we have to create a form specifically a model form taht realtes to the data of a particular form, just as we created the UserRegistrationForm in the forms.py file

Resize the images using Pillow  