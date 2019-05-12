from django.db import models

# Create your models here.
class categories(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']