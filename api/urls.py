from django.urls import path, include
from .views import Formulario,Testing
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path("form",csrf_exempt(Formulario.as_view()),name="Formulario"),
    path("test",csrf_exempt(Testing.as_view()),name="Test")
]
