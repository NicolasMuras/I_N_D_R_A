from apps.Users.api.serializers.user_serializers import UserSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from apps.Users.models import User
from apps.Tags.models import Tag



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
