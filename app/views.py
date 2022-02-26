from rest_framework import generics, permissions
from .models import *
from .serializers import *


class PerevalCreate(generics.ListCreateAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ImagesCreate(generics.ListCreateAPIView):
    queryset = Pereval_images.objects.all()
    serializer_class = ImagesSerializer
    # permission_classes = [permissions.IsAuthenticated]
