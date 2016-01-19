from django.db import models
from ghostnames.utils import tuplify_list

GHOST_NAME_AVAILABILITY = tuplify_list(['taken','available'])

class Ghost(models.Model):
    name = models.CharField(max_length=255)
    taken = models.CharField(max_length=32, choices=GHOST_NAME_AVAILABILITY)
    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name



class Username(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def given_name(self):
        return u'{} {}'.format(self.firstname, self.lastname)