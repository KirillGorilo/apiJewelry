from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TypeJewelryViewSet, JewelryViewSet, BasketViewSet, BasketJewelryViewSet
from base.views import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'typejewelry', TypeJewelryViewSet)
router.register(r'jewelry', JewelryViewSet)
router.register(r'basket', BasketViewSet)
router.register(r'basketjewelry', BasketJewelryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]