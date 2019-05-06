# Import forms from django
from django import forms
# Import USer model
from django.contrib.auth.models import User
# Import UserCreationForm so as to inherit it
from django.contrib.auth.forms import UserCreationForm
# Importing Profile model for working with user update form
from ..models import Profile

# Create a new registeration form using UserCreationForm
class UserRegistrationForm(UserCreationForm):
    # Add all the desired fields
    email = forms.EmailField(required=False)

    # Define inner class to describe interactions with the model
    class Meta:
        # Specify the models
        model = User
        # SPecify the fields and their order of appearnace
        fields = ['username','email','password1','password2']
        

# Model form for updating USer detials
class UserUpdateForm(forms.ModelForm):
    # For now we only wish to modify the username and the email
    email = forms.EmailField()
    class Meta:
        # User model for the form
        model = User
        # Fields of the form
        fields =['username','email']


# Form for upating Profile Picture 
class ProfileUpdateForm(forms.ModelForm):
    # No additional form required

    class Meta:
        model = Profile
        fields =["image"]