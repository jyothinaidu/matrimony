from django.conf.urls import url
from .tamilmatrimony_api import *
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
router = routers.DefaultRouter()
router.register(r'pofileslist', ProfilesApiList)
urlpatterns =[
    url(r'^', include(router.urls)),
    url(r'^$',api_root),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # url(r'pofileslist/?$',ProfilesApiList.as_view({'get': 'retrieve'}),name="details-profiles")
]