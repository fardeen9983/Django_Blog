# Very similar to how urls.py works for main web app
# import views.py to access render functions

from . import views # import blog.views
from django.urls import path


# Create URL patterns
urlpatterns = [
    # Map root URL to home function in views.py
    path("",views.home, name = "blog-home"),
    # Map about page route
    path("about/",views.about, name ="blog-about")
]

# Finally add these URL pattern to the main urls.py file
# Access the blog app's web pages through url : http://localhost:8000/blog