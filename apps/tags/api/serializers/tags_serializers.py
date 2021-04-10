from rest_framework import serializers
from apps.tags.models import Tag



class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
    #Custom Validations
    def validate_colour(self,value):
        colours = [
            "red", "green", "blue", "yellow", "lightblue", "black", 
            "grey", "white", "orange", "purple", "brown", "pink"
            ]
        if value not in colours:
            raise serializers.ValidationError('Error, su color no esta en la lista permitida')
        return value   