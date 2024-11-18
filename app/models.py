from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SoftwareSolution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class PastSolution(models.Model):
    industry = models.CharField(max_length=200)
    description = models.TextField()

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    rating = models.IntegerField()  
    feedback = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

class PhotoGallery(models.Model):
    name = models.CharField(max_length=255)  # Name of the gallery or album
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    gallery = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE, related_name='event_photos')
    image = models.ImageField(upload_to='event_photos/')  # Upload folder: 'media/photos/'
    caption = models.CharField(max_length=255, blank=True, null=True)  # Optional caption
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo in {self.gallery.name}"


class CustomerInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_details = models.TextField()
    inquiry_date = models.DateTimeField(auto_now_add=True)





