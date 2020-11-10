from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Event, Category, EventCategory
from .forms import *

from django.views.generic import (ListView, DetailView,
                                    CreateView, DeleteView,
                                    TemplateView)

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
    # model = Event
    # fields = ['name', 'description']
    form_class = EventForm
    # form_class = CategoryForm
    # success_url = reverse('events:list')
    
    # def get_success_url(self):
    #     return reverse('events:list')
        
    def form_valid(self, form):
        context = self.get_context_data()
        print('HEHEHEHHEHEHEHEHEHHEH')
        
        categories = form.cleaned_data['category_name']
        event_name = form.cleaned_data['name']
        event_desc = form.cleaned_data['description']
        
        event = Event(user=self.request.user, name=event_name, description=event_desc)
        event.save()
        # print()
        for key in categories:
            event_category = EventCategory(event = event, category = Category.objects.get(pk=key))
            event_category.save()
        
        return HttpResponseRedirect(reverse_lazy('events:list'))
        # event.save()
        
        # with transaction.atomic():
        #     form.instance.created_by = self.request.user
        #     self.object = form.save()
        #     if categories.is_valid():
        #         categories.instance = self.object
        #         categories.save()
        # return super(EventCreate, self).form_valid(form)
    


