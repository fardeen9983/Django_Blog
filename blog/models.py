from django.db import models
# For timezone considerations
from django.utils import timezone
# Import user model
from django.contrib.auth.models import User

# Create your models here.

"""
Few operations on the USer model:
User.objects.all() : Fetches all usernames
User.objects.first() : Fetches first user
User.objects.filter(field='value') : Return specific users 
User.objects.get(id='1') : Get users by Id

Attributes:
id/pk - returns id
"""

# Create model for posts on the blog. This class will be translated to a table of the same name.
class Post(models.Model):
    # Now we have to define various fields for class which will becomes corresponding column in the table
    # We assign the valid models datatypes to each of these fields

    # A restricted string
    title = models.CharField(max_length=100)
    
    # Unrestricted text
    content = models.TextField()
    
    # DateTime of creation. Various arguments are:
    # auto_now : To set the date time to present
    # auto_now_add : To set the date time to present only when the object is created   
    # default : Takes a timestamp
    date_posted = models.DateTimeField(default=timezone.now)

    # Specify the author of the post
    # Since we are using User model we can create a Foreign key pointing to it as relation between User and Post is one to many
    # We have to also specify what to do when User model is deleted. We can delete the post or set the User to None
    # Option - CASCADE : Cascades the delete operation form User as well to the foreign key dependent Post model
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    # Define a toString method to get the string description of the Post object
    def __str__(self):
        return self.title

# To update these changes to the database we have to rerun the migrations again

"""
Accessing Post model records
Post.objects.all() : Initially empty

Create a Post object with field values all set.
To save the object as record in Post table:
post_obj.save()
"""



