from django.urls import path
from apps.main.views import schedule_view
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('',login_required(schedule_view), name='schedule_view'),
]   
