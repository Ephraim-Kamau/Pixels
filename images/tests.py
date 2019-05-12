from django.test import TestCase
from .models import Image,Location,categories

# Create your tests here.
class ImageTestclass(TestCase):
    # Set up method
    def setUp(self):
        self.machine = categories.objects.create(name='machine')
        self.beast = categories.objects.create(name='beast')
        self.mombasa = Location.objects.create(name='Mombasa')

        self.car = Image.objects.create(
            name='skyline', location='self.mombasa', description='Quite a fast car')

        self.car.categories.add(self.machine)
        self.car.categories.add(self.beast)   

        
    # Testing  instance
    def test_instance(self):
        self.car.save()
        self.assertTrue(isinstance(self.car,Image))    