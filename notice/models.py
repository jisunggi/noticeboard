from django.db import models


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title