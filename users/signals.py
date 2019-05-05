# Create a signal to be executed after a User model is saved
from django.db.models.signals import post_save
# Import the User model which will act as the signal sender
from django.contrib.auth.models import User
# Import the signal reciever class
from django.dispatch import receiver
# Import the Profile model we will create for each new User
from .models import Profile

# We need to add te signals to app's config file: apps.py

# Reciever function for User created signal
# If the signal is post_save and the sender is User .i.e, a User model object is created 
# Then call this function
@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    # Create a Profile object for new User
    if created:
        Profile.objects.create(user=instance)

# Save the profile instance 
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()


