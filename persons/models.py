from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname()

    @property
    def fullname(self):
        return f"{self.name} {self.last_name}"
