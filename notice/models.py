from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    password = models.CharField(max_length=4, validators=[MinLengthValidator(limit_value=4)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    notice_id = models.ForeignKey(Notice, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)


class Emotion(models.Model):
    notice_id = models.ForeignKey(Notice, on_delete=models.CASCADE)
    user = models.CharField(max_length=10)
    like = models.BooleanField(default=True)

    class Meta:
        unique_together = ['notice_id', 'user']


