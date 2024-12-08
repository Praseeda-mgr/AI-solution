from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Solution(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()        
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)     
    image = models.ImageField(upload_to='solutions/', blank=True, null=True)  
    def __str__(self):
        return self.title


class PastSolution(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)  
    industry = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='past_solutions/', blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled"

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=100, default='Anonymous') 
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


class Feedback(models.Model):
    name = models.CharField(max_length=100)  
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating (1 to 5 stars)
    message = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"


