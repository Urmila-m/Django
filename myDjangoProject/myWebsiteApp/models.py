from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class MyModel(models.Model):
    GENDER =[('male', 'Male'), ('female', 'Female'), ('others', 'Others')]
    ITEM =[('momo', 'momo'), ('pizza', 'pizza'), ('chwela baji', 'chwela baji'), ('newari khaja set', 'newari khaja set'), ('chicken chilly', 'chicken chilly'), ('coffee', 'coffee')]
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField() #primary_key=True raakhda ni hunxa or by default euta integer primary field id, django le asssign gareko hunxa
    gender = models.CharField(choices= GENDER, max_length=50)
    item = models.CharField(choices= ITEM, max_length=50)
    quantity = models.IntegerField()
    password = models.CharField(max_length=50)
    suggestion = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)  # we are sending the function as an argument, not the value returned by the function
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ImageAndFileModel(models.Model):
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file.name+"/"+self.image.name
