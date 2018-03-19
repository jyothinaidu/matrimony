import os,sys
from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.db import transaction
from django.db import DatabaseError
from ..models import profiles
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class ProfilesSerializer(serializers.Serializer):
    class Meta:
        model = profiles
