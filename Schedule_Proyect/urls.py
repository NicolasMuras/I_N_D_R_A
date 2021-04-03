from django.contrib import admin
from django.urls import path,include, re_path
from django.contrib.auth.views import LoginView,LogoutView 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('tags/', include('apps.Tags.api.routers')),
    path('users/', include('apps.Users.api.routers')),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='login.html'), name='logout'),
]