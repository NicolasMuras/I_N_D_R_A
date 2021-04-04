from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('api/tags/', include('apps.tags.api.routers')),
    path('api/users/', include('apps.users.api.routers')),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='login.html'), name='logout'),
]