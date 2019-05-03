from django.contrib import admin
# Import Post model
from .models import Post

# Register your models here.

admin.site.register(Post)