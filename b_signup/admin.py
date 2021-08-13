from django.contrib import admin
from .models import User
from .models import UserInterest


admin.site.register(User)
admin.site.register(UserInterest)
