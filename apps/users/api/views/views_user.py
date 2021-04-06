from rest_framework import viewsets
from apps.users.api.serializers.user_serializers import UserSerializers
from apps.Users.models import User



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()