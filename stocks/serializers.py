# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File    : serializers.py.py
Description :
@Author :       pchaos
tradedate：          18-4-3
-------------------------------------------------
Change Activity:
               18-4-3:
@Contact : p19992003#gmail.com                   
-------------------------------------------------
"""
__author__ = 'pchaos'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from stocks.models import Listing
from stocks.models import BKDetail

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ('code', 'name', 'market', 'isindex')

class BKDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BKDetail
        fields = ('code', 'name', 'market', 'isindex')