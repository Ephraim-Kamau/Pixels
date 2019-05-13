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
    gallery_image = models.ImageField(upload_to = 'pix/', blank=True)

    class Meta:
        ordering = ['name']

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(categories__name__icontains=search_images)
        return images  

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def view_category(cls,cat):
        categories = cls.objects.filter(categories=cat)
        return categories  