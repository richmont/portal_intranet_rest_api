from rest_framework import serializers
from intranet_api.models.Setor import Setor


class SerializerSetor(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'