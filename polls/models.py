from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Meta:
    app_label = 'polls'
