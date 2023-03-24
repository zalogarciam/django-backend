from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import CategoriaSerializer, PruebaSerializer
from .models import Categoria
class PruebaView(APIView):
    def get(self, request):
        data = [
            {
            'nombre': 'diversion',
            'id': 1
            },
            {
            'nombre': 'entretenimiento',
            'id': 2
            }
        ]

        return Response(data = data)
    
    def post(self, request):
        print(request.data)
        data = request.data
        data_serializada = PruebaSerializer(data =data)
        result = data_serializada.is_valid()
        if result is True:
            return Response(data = {
                'message': 'Se recibio la prueba'
            })
        else:
            return Response(data = {
                'message': 'La data es invalida',
                'content': data_serializada.errors
            })
    
class CategoriaView(APIView):
    def post(self, request:Request):
        data = request.data
        data_serializada = CategoriaSerializer(data = data)
        resultado = data_serializada.is_valid()
        if resultado:
            categoria = Categoria(**data_serializada.validated_data)
            # save()
            categoria.save()
            return Response(data = {
                'message': 'Categoria creada'
            })
        else:
            return Response(data = {
                'message': 'Error al crear la categoria',
                'content': data_serializada.errors
            })
    
    def get(self, request:Request):
        categorias = Categoria.objects.all()
        data_serializada = CategoriaSerializer(instance = categorias, many= True)

        return Response(data = {
                'content': data_serializada.data
            })
    
class UnaCategoriaView(APIView):
    def get(self, request:Request, id):
        categoria = Categoria.objects.filter(id = id).first()
        data_serializada = CategoriaSerializer(instance = categoria)

        return Response(data ={
            'content': data_serializada.data
        })