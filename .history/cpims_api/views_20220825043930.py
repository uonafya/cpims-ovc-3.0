from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.
from cpims_api.serializers import RegOrgUnitSerializer
from cpovc_registry.models import RegOrgUnit

class RegOrgUnitViewSet(viewsets.ViewSet):
    # queryset = RegOrgUnit.objects.all()
    # serializer_class = RegOrgUnitSerializer
     # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    
