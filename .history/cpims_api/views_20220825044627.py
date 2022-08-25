from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
from cpims_api.serializers import RegOrgUnitSerializer
from cpovc_registry.models import RegOrgUnit

from rest_framework.permissions import IsAuthenticated

class RegOrgUnitViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    
    queryset = RegOrgUnit.objects.all()
    serializer_class = RegOrgUnitSerializer
    
