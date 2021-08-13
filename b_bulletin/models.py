from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from b_signup.models import User
from django.db import models
from django.utils import timezone
from b_info.models import Circle

# Create your models here.


class PromotionPost(models.Model):

    title = models.CharField(max_length=50)
    recruitStartDate = models.DateField(blank=True, null=True)
    recruitEndDate = models.DateField(blank=True, null=True)
    howManyMember = models.IntegerField(blank=True, default=0)
    keyword = models.CharField(max_length=50, blank=True)
    detailContent = models.TextField()
    img = models.CharField(max_length=100, blank=True)
    circleID = models.ForeignKey(Circle, on_delete=CASCADE)
    userID = models.ForeignKey(User, on_delete=CASCADE)
    writeDate = models.DateTimeField(default=timezone.now)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title
