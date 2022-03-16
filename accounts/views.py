from ast import Index
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import UserCustom

class ProfielDetailView(DetailView):
    model = UserCustom
    template_name = 'accounts/index.html'