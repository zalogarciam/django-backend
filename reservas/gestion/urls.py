from django.urls import path

from .views import CategoriaView, ProductosGenericView, ProductosView, PruebaView, UnProductoView, UnaCategoriaView

urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('otra_prueba/', PruebaView.as_view()),
    path('categoria/', CategoriaView.as_view()),
    path('categoria/<int:id>', UnaCategoriaView.as_view()),
    path('productos/', ProductosView.as_view()),
    path('productos-generic/', ProductosGenericView.as_view()),
    path('producto/<int:id>', UnProductoView.as_view()),
]