from rest_framework import serializers
from intranet_api.models import Contato


class SerializerContatoDetalhes(serializers.ModelSerializer):
    setor_nome = serializers.SerializerMethodField()
    #setor = serializers.StringRelatedField()
    loja_nome = serializers.SerializerMethodField()
    #loja = serializers.StringRelatedField()

    def get_setor_nome(self, obj):
        return obj.setor.nome

    def get_loja_nome(self, obj):
        return obj.loja.nome
    
    class Meta:
        model = Contato
        #fields = '__all__'
        fields = ['nome', 'ramal', 'email', 'setor_nome', 'loja_nome']