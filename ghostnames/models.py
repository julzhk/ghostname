from django.db import models

class Username(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)