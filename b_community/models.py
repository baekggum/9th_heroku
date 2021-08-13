from django.db.models.deletion import CASCADE
from b_signup.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Community(models.Model):
    userID = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=50)
    keywordID = models.CharField(max_length=50, null=True)
    detailContent = models.TextField()
    image = models.ImageField(upload_to = 'community/', blank=True, null=True)
    writeDay = models.TimeField(default=timezone.now)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title
