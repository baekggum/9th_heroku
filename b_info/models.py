from b_signup.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.


class Circle(models.Model):
    name = models.CharField(max_length=30, unique=True)
    madeDate = models.DateTimeField(default=timezone.now)
    Introduction = models.TextField()
    topic = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class CircleMember(models.Model):
    circleID = models.ForeignKey(Circle, on_delete=CASCADE)
    userID = models.ForeignKey(User, on_delete=CASCADE)
    position = models.IntegerField(default=0) #0: 대기, 1: 일반동아리원, 2: 부회장, 3: 회장
    signupDate = models.DateTimeField(timezone.now)

    def __str__(self):
        return str(self.userID)
