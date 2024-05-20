from django.contrib import admin
from .models import CustomUser 

from .models import TypeJewelry, Jewelry, Basket, BasketJewelry


admin.site.register(CustomUser)

@admin.register(TypeJewelry)
class TypeJewelryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price')
    list_filter = ('type',)

class BasketJewelryInline(admin.TabularInline):
    model = BasketJewelry
    extra = 1

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at')
    inlines = (BasketJewelryInline,)
