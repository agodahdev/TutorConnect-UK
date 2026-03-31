from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'core/home.html'

class HowItWorksView(TemplateView):
    template_name = 'core/how_it_works.html'
    
