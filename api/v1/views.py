from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
# from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from .serializers import RegPersonSerializer
from cpovc_registry.models import RegPerson


def regperson_list(request):
    if request.method == 'GET': # get method for the api endpoint
        reg_person = RegPerson.objects.all()
        serializer = RegPersonSerializer(reg_person, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    """
    A POST method for the api endpoint.
    """
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = RegPersonSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

def regperson_detail(request, pk):
     
    """
    One known instance of a person.
    """
    try:
        reg_person = RegPerson.objects.get(pk=pk)
    except RegPerson.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegPersonSerializer(reg_person)
        return JsonResponse(serializer.data)

    """
    Other methods
    """
    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = RegPersonSerializer(reg_person, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     reg_person.delete()
    #     return HttpResponse(status=204)

