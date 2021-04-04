from rest_framework.response import Response
from apps.Tags.api.serializers.tags_serializers import TagSerializers
from rest_framework import viewsets


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = TagSerializers.Meta.model.objects.all()
