import collections

from rest_framework import generics, views, status
from rest_framework.response import Response
from django.http import Http404
from .models import Pereval_added
from .serializers import *


class PerevalCreate(generics.ListCreateAPIView):
    """
    Метод POST создает новую запись. Если пришла картинка - обрабатывает в функцией add_img_info
    Метод GET возвращает все записи
    """
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def get(self, request):
        objs = Pereval_added.objects.all()
        serializer = PerevalSerializer(objs, many=True)
        add_img_info(serializer.data)
        return Response(serializer.data)


class PerevalStatus(views.APIView):
    """
    Возвращает статус записи
    """
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
    """
    Метод GET возвращает запись по её id
    Метод PUT обновляет запись в БД
    """
    def get_object(self, pk):
        try:
            return Pereval_added.objects.get(pk=pk)
        except Pereval_added.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pereval = self.get_object(pk)
        serializer = PerevalSerializer(pereval)
        data = add_img_info(serializer.data, many=False)
        return Response(data)

    def put(self, request, pk, format=None):
        pereval = self.get_object(pk)
        if request.data.get('user') != pereval.user:
            return Response('Сhanges are prohibited', status=status.HTTP_400_BAD_REQUEST)
        serializer = PerevalSerializer(pereval, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesCreate(generics.ListCreateAPIView):
    """
    Сохраняет картинку в БД. Требование заказчика
    """
    queryset = Pereval_images.objects.all()
    serializer_class = ImagesSerializer
#     # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = ImagesSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            print(f'id: {instance.id}')
            file = request.FILES['img']
            with open(f'media\{file.name}', 'rb') as f:
                output = f.read()
                instance.blob = output
                instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesDetail(views.APIView):
    """
    Возвращает картинку по id
    """
    def get_object(self, pk):
        try:
            return Pereval_images.objects.get(pk=pk)
        except Pereval_images.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ImagesSerializer(image)
        return Response(serializer.data)


def add_img_info(data: collections.OrderedDict, many: bool = True):
    """
    Add images info to dict
    :param data: OrderedDict or Dict
    :param many: True - if many objects, False - if one object
    :return: OrderedDict or Dict with ing info
    """
    if many:
        for el in data:
            _id = el.get('id')
            objs = Pereval_images.objects.filter(id_pereval=_id)
            lst = []
            if objs:
                for obj in objs:
                    lst.append({'id': obj.id, 'url': f'media/{obj.img}', 'title': obj.title})
            el.update(img=lst)
    else:
        objs = Pereval_images.objects.filter(id_pereval=data.get('id'))
        lst = []
        if objs:
            for obj in objs:
                lst.append({'id': obj.id,
                            'url': f'media/{obj.img}',
                            'title': obj.title})
        data['img'] = lst
        return data
