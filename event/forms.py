from django import forms
from .models import Event, Category, EventCategory




class EventForm(forms.ModelForm):
    category_name = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                choices=Category.objects.all().values_list('id', 'name'))
    class Meta:
        model = Event
        fields = ['name', 'description', 'category_name']


class CategoryForm(forms.ModelForm):
    category_name = forms.ChoiceField(choices=Category.objects.all())
    class Meta:
        model = Category
        fields = ['category_name']
        
        # widgets = {'name': forms.MultipleChoiceField(choices=(Category.objects.all()))}