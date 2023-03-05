from django.contrib import admin

from products.models import Product, Purchase

class PurchaseAdminInLine(admin.TabularInline):
    model = Purchase

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description", "created_at", "color",)
    fields = ("title", "price", "description", "created_at", "color",)
    readonly_fields = ("created_at",)
    search_fields = ("title", "description")
    inlines = (PurchaseAdminInLine,)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", "created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user", "products")
from django.contrib import admin

# Register your models here.
