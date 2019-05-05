from django.contrib import admin
# Import custom models
from .models import Profile

# Register your models here.

# Register Profile Model
admin.site.register(Profile)
