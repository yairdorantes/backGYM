
from django.views import View
import json
from django.http import JsonResponse
from .models import Cliente
# import base64
# import cloudinary
# from django.contrib.auth import authenticate
# from cloudinary.uploader import upload
# from django.core.files.base import ContentFile


class Formulario(View):
    def get(self, request):
        return JsonResponse({"message": "nice"})

    def post(self, request):
        jd = json.loads(request.body)
        Cliente.objects.create(**jd)
        print(jd)
        return JsonResponse({"message": jd})


class Testing(View):

    def post(self, request):

        return JsonResponse({"message": "success"})
