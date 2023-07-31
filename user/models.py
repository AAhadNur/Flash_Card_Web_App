from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="user", on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    bio = models.CharField(max_length=510, null=True, blank=True)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    education = models.CharField(max_length=510, null=True, blank=True)
    country = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return str(self.name)
