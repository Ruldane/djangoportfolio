from django.urls import path, include
# '.' means, it's in our directory
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    ]