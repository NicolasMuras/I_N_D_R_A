from rest_framework import serializers
from apps.Users.models import User



class UserSerializers(serializers.ModelSerializer):
    tag_name =  serializers.ReadOnlyField(source='tags.name')
    class Meta:
        model = User
        fields = ('name','password','tag_name')
       
      