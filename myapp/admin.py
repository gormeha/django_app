from django.contrib import admin
from django.db.models import F
from .models import Product, Category, Client, Order
# Register your models here.


admin.site.register(Category)
admin.site.register(Order)


def stock_update(modeladmin, request, queryset):
    queryset.update(stock = F('stock') + 50)


class ProductAdmin(admin.ModelAdmin):
    {
        'fields': ('name', 'price', 'category', 'stock', 'available', 'description', 'interested_in')
    }
    list_display = ('name', 'price', 'category', 'stock', 'available', 'description', 'interested_in')
    actions = [stock_update]


class ClientAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'city', 'interested_in')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)