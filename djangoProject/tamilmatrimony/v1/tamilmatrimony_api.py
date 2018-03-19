from urllib.parse import parse_qs
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q,Count
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rest_framework import generics,permissions,status
from rest_framework.decorators import api_view
from rest_framework.pagination import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from ..models import profiles
from .tamilmatrimony_api_serializers import ProfilesSerializer
import collections
from rest_framework import viewsets
from django.http import Http404
import json
from django.shortcuts import get_object_or_404
@api_view(['GET'])
def api_root(request,format=None):
    response_directory =collections.OrderedDict()
    response_directory['Profiles'] = reverse('tamilmatrimony-api:details-profiles',request=request,format=None)

    return Response(response_directory)



class ProfilesApiList(viewsets.ModelViewSet):
    queryset = profiles.objects.all()
    print (">>>>>>>>>>>>>",type(queryset))
    serializer_class = ProfilesSerializer


    # def list(self,request):
    #     queryset = profiles.objects.all()
    #     serializer = ProfilesSerializer(queryset,many=True)
    #     return Response(serializer.data)
    # def retrieve(self,request,pk=None):
    #     queryset = profiles.objects.all()
    #     user = get_object_or_404(queryset,pk=pk)
    #     serializer = ProfilesSerializer(user)
    #     return Response(serializer.data)
