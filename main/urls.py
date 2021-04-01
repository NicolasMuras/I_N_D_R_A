from django.urls import path
from main.views import schedule_view

urlpatterns = [
    path('', schedule_view, name = 'schedule_view'),
]