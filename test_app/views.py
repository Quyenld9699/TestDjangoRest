from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from .models import TestModel
from django.forms.models import model_to_dict
from .serializers import SimpleviewSerializer, SimpleModalSerializer
# Create your views here.

@csrf_exempt
def simple(request):
    method = request.method.lower()
    if method == "get":
        return JsonResponse({"data": [1,2,3,4,5]})
    elif method == "post":
        return JsonResponse({"data": "Added data successfully"})
    elif method == "put":
        return JsonResponse({"data": "Update data successfully!"})
    return JsonResponse({"error": "method not allowed"})

#----------------------------------------------------------------------

class Simpleview(APIView):
    def post(self, request):
        serializer = SimpleviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # new_test_content = TestModel.objects.create(
        #     name = request.data["name"],
        #     description = request.data["description"],
        #     phone = request.data["phone"],
        #     is_live = request.data["is_live"],
        #     amount = request.data["amount"],
        # )
        # return JsonResponse({"data": SimpleviewSerializer(new_test_content).data})
        return JsonResponse({"data": serializer.data})

    def get(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            content = TestModel.objects.all()
            return JsonResponse({"data": SimpleviewSerializer(content, many=True).data})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist!"})
        
        return JsonResponse({"data": SimpleviewSerializer(instance).data})

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT not allowed"})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist!"})

        serializer = SimpleviewSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})

class SimpleView2(APIView):

    def post(self, request):
        serializer = SimpleModalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})

    def get(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            content = TestModel.objects.all()
            return JsonResponse({"data": SimpleModalSerializer(content, many=True).data})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist!"})
        
        return JsonResponse({"data": SimpleModalSerializer(instance).data})

    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT not allowed"})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "Object does not exist!"})

        serializer = SimpleModalSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})


class SimpleGenerics(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleModalSerializer

class SimpleGenericsUpdate(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleModalSerializer
    lookup_field = "id"

class SimpleViewset(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleModalSerializer