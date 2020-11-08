from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Event, Category, EventCategory

from django.views.generic import (ListView, DetailView,
                                    CreateView, DeleteView,
                                    TemplateView)

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

# Create your views here.
class EventList(ListView):
    model = EventCategory
    # paginate_by = 20
    
    template_name = 'event/event_list.html'