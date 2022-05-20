from rest_framework import serializers
from .models import Pereval_added, Pereval_images


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        fields = ('id', 'beautyTitle', 'title', 'other_titles',
                  'connect', 'add_time', 'user', 'coords', 'type',
                  'level', 'status',)


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_images
        fields = '__all__'
