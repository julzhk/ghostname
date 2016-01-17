from django.db import models

class Username(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    date = models.DateTimeField(auto_now_add=True)