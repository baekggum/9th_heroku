from django.db.models.deletion import CASCADE
from b_bulletin.models import PromotionPost
from b_signup.models import User
from django.db import models

# Create your models here.


class Question(models.Model):
    promotionPostID = models.ForeignKey(PromotionPost, on_delete=CASCADE)
    question = models.CharField(max_length=200)

class Apply(models.Model):
    promotionPostID = models.ForeignKey(PromotionPost, on_delete=CASCADE)
    questionID = models.IntegerField(null=True)
    userID = models.IntegerField(null=True)
    answer = models.CharField(max_length=100, null=True)
    temporary = models.BooleanField(default=False)
