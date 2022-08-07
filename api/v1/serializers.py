from cpovc_registry.models import RegPerson
from rest_framework import serializers

class RegPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegPerson
        fields = ['id', 'first_name', 'surname', 'other_names',
                    'date_of_birth', 'created_by', 'created_at',
                    'is_void', ] 
        
