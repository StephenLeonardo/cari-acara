from django.db import models
from django.urls import reverse
from django.conf import settings
import os.path

from django.contrib.auth import get_user_model
User = get_user_model()


def get_image_path(instance, filename):
    return os.path.join('photos', 'event_banner', filename)


# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'username':self.user.username, 'pk':self.pk})
        
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'name']
        db_table = "events"
        
class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return self.name
        
    class Meta:
        db_table = "categories"


class EventCategory(models.Model):
    event = models.ForeignKey(Event, related_name='event_categories', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='event_categories', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.event.name
    
    class Meta: 
        verbose_name = 'EventCategories'
        db_table = "event_categories"
    
    
    
    