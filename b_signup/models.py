from django.db import models
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.


class User(models.Model):
    login_ID = models.CharField(max_length=100, unique=True)
    nickName = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, blank=True)
    passWord = models.CharField(max_length=200)
    enterYear = models.DateField(null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=100)
    email = models.EmailField()
    isAuth = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    registDate = models.DateTimeField(default=timezone.now)
    profileImg = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.login_ID


class UserInterest(models.Model):
    user_ID = models.ForeignKey('User', on_delete=models.CASCADE)
    culture_art = models.BooleanField(default=False)
    volunteer_social = models.BooleanField(default=False)
    academic_cultivative = models.BooleanField(default=False)
    startup_employment = models.BooleanField(default=False)
    language = models.BooleanField(default=False)
    physics = models.BooleanField(default=False)
    coding = models.BooleanField(default=False)
    study = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_ID} 의 관심분야'
