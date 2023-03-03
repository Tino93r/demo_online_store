from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    ordering = ('name',)
    search_fields = ('name',)


class BasketAdminInline(admin.TabularInline):
    model = Product
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp', 'quantity')
    extra = 0
