from django.shortcuts import render
# Import Django auth forms
from django.contrib.auth.forms import UserCreationForm
# To show a message on the template upon recieving valid data
from django.contrib import messages
# Import the redirect function to send the user to specific page
from django.shortcuts import redirect
# Import the new UserRegisterationForm, Profile and USer update forms
from .forms.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# Import decorator to ensure user is logged in
from django.contrib.auth.decorators import login_required

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
    
    # Create UserCreationForm instance and a template for Registration page 
    # Pass the form as context to the template
    # Replace UserCreationForm with UserRegisterationForm
    form = UserRegistrationForm()
    if request.method == "POST":
        # Create a UserCreationForm with the values of the post request body
        form = UserRegistrationForm(request.POST)    
        # Valid the form to conatin desired information only
        if form.is_valid():
                # To prevent regestering the same user save the form details 
                form.save()
                # Create fileds from form data
                username = form.cleaned_data.get('username')
                # Display a message on Register template that valid data was recieved. Also modify the base template for handling such messages
                messages.success(request,f"Your account has been created. You can now login")
                
                # Redirect the user to blog home page
                # return redirect('blog-home')

                # Better to redirect the user to login page
                return redirect('login')

    return render(request,"register.html",{ 'form' : form })


# Create User profile page and only allow logged in users to access it.
@login_required
def profile(request):
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        # Add ability to update profile and user details
        # Add already established data to default form value
        if request.method =="POST":
                u_form = UserUpdateForm(request.POST,instance = request.user)
                p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
                if u_form.is_valid and p_form.is_valid:
                        # Save the details if successfull
                        u_form.save()
                        p_form.save()

                        # Send success message
                        messages.success(request,"Updated successfully")
                        # Redirect the user to  Profile page through get request
                        return redirect('profile')

        # Pass the two forms over to the Profile template
        context = {
                'u_form' : u_form,
                'p_form' : p_form
        }

        return render(request,'profile.html',context) 