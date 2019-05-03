from django.shortcuts import render
# Import Django auth forms
from django.contrib.auth.forms import UserCreationForm
# To show a message on the template upon recieving valid data
from django.contrib import messages
# Import the redirect function to send the user to specific page
from django.shortcuts import redirect

"""
Types of messages in Django
1. message.debug
2. message.info
3. message.success
4. message.warning
5. message.error
"""

# Create your views here.

# Create a register new account page (View)
def register(request):
    # Since all the submit operations on the Regiteration form are being redrrected here we can simply place a check and handle form validation,etc
    if request.method == "POST":
        # Create a UserCreationForm with the values of the post request body
        form = UserCreationForm(request.POST)    
        # Valid the form to conatin desired information only
        if form.is_valid():
            # Create fileds from form data
            username = form.cleaned_data.get('username')
            # Display a message on Register template that valid data was recieved. Also modify the base template for handling such messages
            messages.success(request,f"Account created for {username}!")
            # Redirect the user to blog home page
            return redirect('blog-home')
        else:
            messages.error(request,form.error_messages) 
    else:
        # Create UserCreationForm instance and a template for Registration page 
        # Pass the form as context to the template
        form = UserCreationForm()
    return render(request,"register.html",{ 'form' : form })