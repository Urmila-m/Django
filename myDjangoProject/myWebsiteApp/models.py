from django.db import models
from django.utils import timezone


class MyModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField() #primary_kry=True raakhda ni hunxa or by default euta integer primary field id, django le asssign gareko hunxa
    gender = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    password = models.CharField(max_length=50)
    suggestion = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)  # we are sending the function as an argument, not the value returned by the function

    def __str__(self):
        return self.name