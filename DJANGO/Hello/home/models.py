from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    query =models.TextField(max_length=500)
    phone =models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.name