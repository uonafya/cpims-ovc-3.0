from django.shortcuts import render

from rest_framework import viewsets



# models
from cpovc_registry.models import RegOrgUnit, RegPerson
from cpovc_ovc.models import OVCRegistration, OVCViralload, OVCExit
from cpovc_main.models   import FacilityList, SchoolList
from cpovc_forms.models import OVCCareServices, OVCEducationLevelFollowUp, OVCEducationFollowUp, OVCCarePriority

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from rest_framework.authentication import TokenAuthentication

# Create your views here.
from cpims_api.serializers import (
    RegOrgUnitSerializer,
    OVCRegistrationSerializers,
    RegPersonSerializers,
    FacilityListSerializers,
    SchoolistSeriallizers,
    OvcCareServicesSerializers,
    OvcViralLoadSerializers,
    OVCEducationFollowUpSerializers,
    OVCEducationLevelFollowUpSerializer,
    OVCExitSerializer,
    OVCCarePrioritySerializer

)

class RegOrgUnitViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)   
    queryset = RegOrgUnit.objects.all()
    serializer_class = RegOrgUnitSerializer
    

class OVCRegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = OVCRegistration.objects.all()
    serializer_class = OVCRegistrationSerializers
    
class RegpersonViewSet(viewsets.ModelViewSet):
    permission_classes  = (IsAuthenticated)
    queryset = RegPerson.objects.all()
    serializer_class = RegPersonSerializers
    
class FacilityListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FacilityList.objects.all()
    serializer_class = FacilityListSerializers
    
class SchoolListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset  = SchoolList.objects.all()
    serializer_class = SchoolistSeriallizers
    
class OvcCareServicesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset =  OVCCareServices.objects.all()
    serializer_class = OvcCareServicesSerializers

class OvcViralLoadViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OVCViralload.objects.all()
    serializer_class = OvcViralLoadSerializers
    

class OVCEducationLevelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OVCEducationLevelFollowUp.objects.all()
    serializer_class = OVCEducationLevelFollowUpSerializer
    
    
class OVCEducationFollowUpViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OVCEducationFollowUp.objects.all()
    serializer_class = OVCEducationFollowUpSerializers
    
class OVCExitViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OVCExit.objects.all()
    serializer_class = OVCExitSerializer  
    
    
class OVCCarePriorityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OVCCarePriority.objects.all()
    serializer_class = OVCCarePrioritySerializer  


     
    
    
