from django.urls import path

from .views import CategoriaView, PruebaView

urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('otra_prueba/', PruebaView.as_view()),
    path('categoria/', CategoriaView.as_view()),
]