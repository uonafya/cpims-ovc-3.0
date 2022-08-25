from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from cpovc_registry.models import RegOrgUnit


class RegOrgUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegOrgUnit
        fields  = "__all__"