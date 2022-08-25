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

    
      # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the rRegOrgUnit items for given requested user
        '''
        rRegOrgUnits = RegOrgUnit.objects.filter(user = request.user.id)
        serializer = RegOrgUnitSerializer(rRegOrgUnits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
