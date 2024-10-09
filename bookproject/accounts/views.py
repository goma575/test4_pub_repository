from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

from .forms import SignupForm

class SignupView(CreateView):
    template_name="accounts/signup.html"
    form_class = SignupForm
    success_url=reverse_lazy("list-book")
    