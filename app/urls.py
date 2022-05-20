from django.urls import path, include
from .views import *


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/pereval/', PerevalCreate.as_view()),
    path('api/v1/pereval/<int:pk>/status/', PerevalStatus.as_view()),
    path('api/v1/pereval/<int:pk>/', PerevalDetail.as_view()),
    path('api/v1/images/', ImagesCreate.as_view()),
    path('api/v1/images/<int:pk>/', ImagesDetail.as_view()),
]
