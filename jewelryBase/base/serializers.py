from .models import CustomUser, TypeJewelry, Jewelry, Basket, BasketJewelry
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class TypeJewelrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeJewelry
        fields = ('id', 'name')

class JewelrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = ('id', 'name', 'type', 'price', 'description')

class BasketJewelrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketJewelry
        fields = ('id', 'basket', 'jewelry', 'quantity')

class BasketSerializer(serializers.ModelSerializer):
    jewelries = BasketJewelrySerializer(many=True, read_only=True, source='basketjewelry_set')
    
    class Meta:
        model = Basket
        fields = ('id', 'user', 'jewelries', 'created_at', 'updated_at')





