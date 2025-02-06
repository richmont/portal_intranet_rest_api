from rest_framework import serializers
from intranet_api.models import Contato


class SerializerContatoDetalhes(serializers.ModelSerializer):
    setor_nome = serializers.SerializerMethodField()
    #setor = serializers.StringRelatedField()
    loja_prefixo = serializers.SerializerMethodField()
    loja_codigo = serializers.SerializerMethodField()
    loja_nome = serializers.SerializerMethodField()
    #loja = serializers.StringRelatedField()

    def get_setor_nome(self, obj):
        return obj.setor.nome

    def get_loja_nome(self, obj):
        return obj.loja.nome

    def get_loja_codigo(self, obj):
        return obj.loja.codigo
    
    def get_loja_prefixo(self, obj):
        return obj.loja.prefixo_ramal
    
    class Meta:
        model = Contato
        #fields = '__all__'
        fields = ['nome', 'loja_prefixo', 'ramal', 'email', 'setor_nome', 'loja_codigo', 'loja_nome']