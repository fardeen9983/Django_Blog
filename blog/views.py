from django.shortcuts import render
#import HttpResponse to handle HTTP requests
from django.http import HttpResponse

# Create your views here.

# Define response for home route. The function will take a HttpRequest obejct as argument
def home(request):
    # Return HTML response to the client
    # To map this to a specific URL create a urls.py file for current app
    return HttpResponse("<h1> Blog Home</h1>")

# Route for an About Page
def about(request):
    return HttpResponse("<h1>About Page</h1>")