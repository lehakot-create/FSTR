from rest_framework import generics, views, status
from rest_framework.response import Response
from django.http import Http404
from .models import Pereval_added
from .serializers import *


class PerevalCreate(generics.ListCreateAPIView):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PerevalStatus(views.APIView):
    def get_object(self, pk):
        try:
            return Pereval_added.objects.get(pk=pk)
        except Pereval_added.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pereval = self.get_object(pk)
        serializer = PerevalSerializer(pereval)
        status = {'status': serializer.data.get('status')}
        return Response(status)


class PerevalDetail(views.APIView):
    def get_object(self, pk):
        try:
            return Pereval_added.objects.get(pk=pk)
        except Pereval_added.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pererval = self.get_object(pk)
        serializer = PerevalSerializer(pererval)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pereval = self.get_object(pk)
        if request.data.get('user') != pereval.user:
            return Response('Сhanges are prohibited', status=status.HTTP_400_BAD_REQUEST)
        serializer = PerevalSerializer(pereval, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ImagesCreate(generics.ListCreateAPIView):
#     queryset = Pereval_images.objects.all()
#     serializer_class = ImagesSerializer
#     # permission_classes = [permissions.IsAuthenticated]
