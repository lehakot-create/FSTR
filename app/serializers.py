from rest_framework import serializers
from .models import Pereval_added, Pereval_images


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_images
        fields = '__all__'
