from django.db import models
from django.utils import timezone
# Create your models here.



class Testimonials(models.Model):
    testimonials_text = models.CharField(max_length=200)
    testimonials_name = models.CharField(max_length=200)
    testimonials_job = models.CharField(max_length=200)
    testimonials_date = models.DateTimeField("date published")
    stars = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials_images/', null=True, blank=True) 
    def __str__(self):
        return self.testimonials_text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
