from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import CategoriaSerializer, ProductoSerializer, PruebaSerializer
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

        if not categoria:
            return Response(data= {
                'content': 'Categoria no existe'
            }, status=404)

        data_serializada = CategoriaSerializer(instance = categoria)

        return Response(data ={
            'content': data_serializada.data
        })
    
    def put(self, request:Request, id):
        categoria = Categoria.objects.filter(id = id).first()

        if not categoria:
            return Response(data= {
                'content': 'Categoria no existe'
            }, status=404)

        data = request.data
        data_serializada = CategoriaSerializer(data = data)

        if data_serializada.is_valid():
            categoria.nombre = data_serializada.validated_data.get('nombre')
            categoria.habilitado = data_serializada.validated_data.get('habilitado')
            categoria.save()
            return Response(data ={
                'content': "Categoria actualizada"
            })
        else:
            return Response(data ={
                'message': "Categoria no actualizada",
                'content': data_serializada.errors
            })
    
    def delete(self, request: Request, id):
        categoria = Categoria.objects.filter(id = id).first()

        if not categoria:
            return Response(data= {
                'content': 'Categoria no existe'
            }, status=404)

        resultado = Categoria.objects.filter(id = id).delete()
        print(resultado)
        return Response(data ={
            'content': "Categoria eliminada"
        })
    
class ProductosView(APIView):
    def post(self, request:Request):
        data = request.data

    
        data_serializada = ProductoSerializer(data = data)
        print(data_serializada)
        if data_serializada.is_valid():
            data_serializada.save()

            return Response(data = {
                'message': 'Producto creado'
            })
        else:
            return Response(data = {
                'message': 'Error al crear Producto',
                'content': data_serializada.errors
            })