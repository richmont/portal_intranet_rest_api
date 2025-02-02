from rest_framework import serializers
from intranet_api.models import Loja


class SerializerLoja(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'