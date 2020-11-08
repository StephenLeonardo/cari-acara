from django.db import models
from django.urls import reverse
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event:detail', kwargs={'username':self.user.username, 'pk':self.pk})
        
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
    
    
    
    