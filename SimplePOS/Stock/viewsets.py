from rest_framework import viewsets
from .models import Categoria
from .serializers import CategoríaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoríaSerializer