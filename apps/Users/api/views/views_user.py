from apps.Users.api.serializers.user_serializers import UserSerializers
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = UserSerializers.Meta.model.objects.all()
