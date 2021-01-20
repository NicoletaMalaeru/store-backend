from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import authentication, permissions, exceptions
from rest_framework.decorators import permission_classes, authentication_classes
from rest_auth.views import LogoutView

from .serializers import *
from .models import *
import urllib.parse
from datetime import date
from django.db.models import Q

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductsSerializer(products, many = True)
    return Response(serializer.data)
