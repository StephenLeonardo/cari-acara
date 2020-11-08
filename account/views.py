from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from . import forms
from .models import Account

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'




class AccountDetail(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'account/profile_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context