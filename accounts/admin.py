from django.contrib import admin
from .models import UserProfile, Experience, Education

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Experience)
admin.site.register(Education)
