from rest_framework import viewsets
from serializers.SerializerSetor import SerializerSetor
from models.Setor import Setor

class SetorViewSet(viewsets.ModelViewSet):

    queryset = Setor.objects.all()
    serializer_class = SerializerSetor
    #permission_classes = [IsAccountAdminOrReadOnly]