from rest_framework import serializers
from apps.tags.models import Tag



class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'