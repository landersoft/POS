from rest_framework import serializers
from .models import Categoria


class CategoríaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'