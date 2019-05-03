from django.shortcuts import render
#import HttpResponse to handle HTTP requests
from django.http import HttpResponse

# Create your views here.

# Define some dummy post data
posts = [
    {
    'author' : 'FK',
    'title' : 'Dummy_blog',
    'content' : 'First blog - dummy content',
    'date_posted' : 'Aug 27,2018'
    },
    {
    'author' : 'Jane Doe',
    'title' : 'Dummy_blog 2',
    'content' : 'Second blog - dummy content',
    'date_posted' : 'May 2,2019'
    }
]

# Define response for home route. The function will take a HttpRequest obejct as argument
def home(request):
    # Return HTML response to the client
    # To map this to a specific URL create a urls.py file for current app
    #return HttpResponse("<h1> Blog Home</h1>")

    # Instead of returning entire HTML pages just render the HTML template instead using render module
    # Create a context dictionary holding values to be sent to the template for dynamic rendering
    context = {
        'posts' : posts,
    }
    # Pass the context dictionary to the HTML template
    return render(request,'home.html',context)

# Route for an About Page
def about(request):
    # return HttpResponse("<h1>About Page</h1>")
    # Give a title to the about page
    return render(request,'about.html',{ 'title': 'About' })