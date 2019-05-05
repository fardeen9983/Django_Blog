"""Django_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
# Import inbuilt views for authentication
from django.contrib.auth import views as auth_views

# import include module from django.urls to include url patterns from apps

urlpatterns = [
    path('admin/', admin.site.urls),
    # Map URL patterns for blog app as the default
    path("",include('blog.urls')),
    # Map URL patterns of users app to /users route
    path("register/",user_views.register,name = 'register'),
    # Create a login view from inbuilt ones and specify the template
    path('login/',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    # Create a logout view from inbuilt ones and specify the template
    path('logout/',auth_views.LogoutView.as_view(template_name="logout.html"),name="logout")
]

# Adding new URL patterns will lead to no longer displaying the default page on server root url