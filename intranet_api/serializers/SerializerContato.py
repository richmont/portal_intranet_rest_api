from rest_framework import serializers
from intranet_api.models import Contato


class SerializerContato(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'