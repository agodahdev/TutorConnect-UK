from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('how-it-works/', views.HowItWorksView.as_view(), name='how_it_works'),
]