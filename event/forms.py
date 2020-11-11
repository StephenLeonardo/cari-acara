from django import forms
from .models import Event, Category, EventCategory




class EventForm(forms.ModelForm):
    category_name = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(
                                                    attrs={'class': 'custom-checkbox-test'}
                                                ),
                                                choices=Category.objects.all().values_list('id', 'name'))
                                    
    
    class Meta:
        model = Event
        fields = ['name', 'description', 'event_date', 'event_time', 'category_name', 'image']
        
        # widgets = {
        #     'event_date': 
        # }


class CategoryForm(forms.ModelForm):
    category_name = forms.ChoiceField(choices=Category.objects.all())
    class Meta:
        model = Category
        fields = ['category_name']
        
        # widgets = {'name': forms.MultipleChoiceField(choices=(Category.objects.all()))}