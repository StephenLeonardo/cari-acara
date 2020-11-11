import os.path
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Event, Category, EventCategory
from .forms import *
import uuid

from django.views.generic import (ListView, DetailView,
                                    CreateView, DeleteView,
                                    TemplateView)

from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

from django.forms import formset_factory

# Create your views here.
class EventList(ListView):
    model = Event
    # paginate_by = 20
    
    
    template_name = 'event/event_list.html'
    

class EventCreate(LoginRequiredMixin, CreateView):
    template_name = 'event/event_create.html'
    form_class = EventForm
        
    def form_valid(self, form):
        context = self.get_context_data()
        print(form)
        print('HAHAHHAHAH')
        categories = form.cleaned_data['category_name']
        print(categories)
        event_name = form.cleaned_data['name']
        event_desc = form.cleaned_data['description']
        
        # self.request.FILES['image']
        temp_image = None
        if self.request.FILES and self.request.FILES['image']:
            extension = os.path.splitext(temp_image.name)[1]
            
            if not (temp_image.name.endswith('.jpg')
                or temp_image.name.endswith('jpeg')
                or temp_image.name.endswith('png')):
                messages.error(self.request, 'image must be either jpg, jpeg, or png format.')
                return super().form_invalid(form)
                
            unique_filename = str(uuid.uuid4()) + extension
            temp_image.name = unique_filename
            
        
        
        event = Event(user=self.request.user, name=event_name, description=event_desc, image=temp_image)
        event.save()
        for key in categories:
            event_category = EventCategory(event = event, category = Category.objects.get(pk=key))
            event_category.save()
        
        return HttpResponseRedirect(reverse_lazy('events:list'))
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        print(form.errors)
        return super().form_invalid(form)
    

class EventDetail(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event']
        context['event_categories'] = EventCategory.objects.filter(event_id=self.kwargs.get('pk'))
        return context


