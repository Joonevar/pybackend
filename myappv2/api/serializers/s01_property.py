from rest_framework import serializers

from api.serializers import s02_user
from main import models


# Image and Video Files Serializer
class ImageVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PropertyImagesVideos()
        fields = ("__all__")



# Property Model Serializer
class PropertySerializer(serializers.ModelSerializer):
    images_videos               = ImageVideoSerializer(many = True)
    lister                      = s02_user.CustomUserSerializer()

    class Meta:
        model = models.Property()
        fields = ('__all__')


# Property Search Serializer
class PropertySearchSerializer(serializers.Serializer):
    keyword                 = serializers.CharField(required = False)
    page                    = serializers.IntegerField(required = False)
    category                = serializers.CharField(required = False)
    filter_dict             = serializers.JSONField(required = False)
    location                = serializers.ListField(required = False)
    distance                = serializers.IntegerField(required = False)
    country                 = serializers.CharField(required = False)
    id                      = serializers.IntegerField(required = False)


# Check Property in Wishlist
class CheckWishlist(serializers.Serializer):
    tokens                  = serializers.CharField()
    id                      = serializers.CharField()


