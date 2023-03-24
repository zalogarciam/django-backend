from django.urls import path

from .views import PruebaView

urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('otra_prueba/', PruebaView.as_view()),
]