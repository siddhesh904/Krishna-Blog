from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    images = models.ImageField(upload_to='blogImages')

    def __str__(self):
        return self.name



    

