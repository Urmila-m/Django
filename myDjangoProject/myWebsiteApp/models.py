from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in as user


class MyModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField() #primary_key=True raakhda ni hunxa or by default euta integer primary field id, django le asssign gareko hunxa
    gender = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    password = models.CharField(max_length=50)
    suggestion = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)  # we are sending the function as an argument, not the value returned by the function
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name