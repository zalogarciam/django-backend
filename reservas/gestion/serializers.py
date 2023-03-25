from rest_framework import serializers
from math import ceil
from .models import Categoria, Producto

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField()

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

def paginationSerializer(totalItems, page, perPage):
    itemsPerPage = perPage if totalItems >= perPage else totalItems
    totalPages = ceil(totalItems/ itemsPerPage)  if itemsPerPage > 0 else None
    prevPage = page - 1 if page > 1 and page <= totalPages else None
    nextPage = page + 1 if totalPages > 1 and page < totalPages else None

    return {
        'itemsPerPage': itemsPerPage,
        'totalPages': totalPages,
        'prevPage': prevPage,
        'nextPage': nextPage
    }