from django.contrib import admin

# Register your models here.
from MyApp.models import UserProfile,Post

admin.site.register(UserProfile)
admin.site.register(Post)