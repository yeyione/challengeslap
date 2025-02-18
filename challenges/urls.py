from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("January", views.january),
    path("February", views.february),
    path("March", views.march), 
    path("April",views.april),
    path("May", views.may),
    path("June", views.june),
    path("July", views.july),
    path("August", views.august),
    path("September", views.september),
    path("October", views.october),
    path("November", views.november),
    path("December", views.december)
]
    
