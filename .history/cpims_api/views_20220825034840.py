from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
from cpims_api.serializers import RegOrgUnitSerializer
from cpovc_registry.models import RegOrgUnit

class RegOrgUnitViewSet(viewsets.ModelViewSet):
    
