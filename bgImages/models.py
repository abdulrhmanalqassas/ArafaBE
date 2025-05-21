from django.db import models
from django.utils import timezone
class backGroundImages(models.Model):
    image_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to='bg/', null=True, blank=True) 
    def __str__(self):
        return str(self.image)

# Create your models here.
