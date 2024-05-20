from django.shortcuts import render
from rest_framework import permissions, viewsets
from base.serializers import UserSerializer
from .models import TypeJewelry, Jewelry, Basket, BasketJewelry, CustomUser
from .serializers import TypeJewelrySerializer, JewelrySerializer, BasketSerializer, BasketJewelrySerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class TypeJewelryViewSet(viewsets.ModelViewSet):
    queryset = TypeJewelry.objects.all()
    serializer_class = TypeJewelrySerializer


class JewelryViewSet(viewsets.ModelViewSet):
    queryset = Jewelry.objects.all()
    serializer_class = JewelrySerializer


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketJewelryViewSet(viewsets.ModelViewSet):
    queryset = BasketJewelry.objects.all()
    serializer_class = BasketJewelrySerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = CustomUser.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]