from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('tags/', include('apps.Tags.api.routers')),
    path('users/', include('apps.Users.api.routers')),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='login.html'), name='logout'),
]