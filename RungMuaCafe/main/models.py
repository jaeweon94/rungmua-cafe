from django.db import models
from django.urls import reverse  # generate urls from url patterns
#from phone_field import PhoneField


class Feedback(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=10) #PhoneField()
    feedback = models.TextField(max_length=1000)

    def __str__(self):
        return self.email


