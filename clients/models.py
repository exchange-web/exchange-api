from django.db import models
from django.contrib.postgres.fields import JSONField

class Client(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
