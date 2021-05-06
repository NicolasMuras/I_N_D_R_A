from rest_framework import viewsets
from apps.users.api.serializers.user_serializers import UserSerializers



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = UserSerializers.Meta.model.objects.all()
