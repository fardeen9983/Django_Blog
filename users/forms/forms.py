# Import forms from django
from django import forms
# Import USer model
from django.contrib.auth.models import User
# Import UserCreationForm so as to inherit it
from django.contrib.auth.forms import UserCreationForm

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
        