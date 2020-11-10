from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventList.as_view(), name='list'),  
    path('create/', views.EventCreate.as_view(), name='create')  
]