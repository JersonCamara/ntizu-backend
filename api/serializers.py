from rest_framework import serializers

from .models import CandidatoModel, EmpresaModel

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CandidatoModel
        fields = '__all__'

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmpresaModel
        fields = '__all__'