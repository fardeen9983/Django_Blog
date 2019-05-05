from django.db import models
# Import base User model
from django.contrib.auth.models import User

# Create your models here.

# Create new User model with Profile features
class Profile(models.Model):
    # Have a one-to-one Relationship with User model
    # Have a User model to access default user fields 
    # Add any extra features required
    # Some can have one to one relationship withe user. Like only one profile picture for each user
    
    # Also specify what to do when base User model is deleted.
    # Use models.Cascade to delete the Profile model as well.
    # But this keeps the User model even if Profile model is removed
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add a profile image field and specify the storage extension
    # Also specify directories to which image will be stored to
    # Also specify the default file to be looked upon if none is provided
    image = models.ImageField(default='default.jpg',upload_to = "profile_pics")

    # Define toString method
    def __str__(self):
        return f'{ self.user.username } Profile'

# Finally run migrations for Profile model and register it in admin.py

