from django.shortcuts import render
#import HttpResponse to handle HTTP requests
from django.http import HttpResponse
# Import the post model
from .models import Post

# Create your views here.

# Define response for home route. The function will take a HttpRequest obejct as argument
def home(request):
    # Return HTML response to the client
    # To map this to a specific URL create a urls.py file for current app
    #return HttpResponse("<h1> Blog Home</h1>")

    # Instead of returning entire HTML pages just render the HTML template instead using render module
    # Create a context dictionary holding values to be sent to the template for dynamic rendering

    # Instead of passing the dummy values pass in the Post objects
    context = {
        # 'posts' : posts,
        'posts' : Post.objects.all()
    }
    
    # Since the Post model fields and the onces used in post template are same no other changes are needed

    # Pass the context dictionary to the HTML template
    # Add some Post objects from pyhton command shell
    return render(request,'home.html',context)

# Route for an About Page
def about(request):
    # return HttpResponse("<h1>About Page</h1>")
    # Give a title to the about page
    return render(request,'about.html',{ 'title': 'About' })