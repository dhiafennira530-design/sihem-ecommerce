from django.contrib import admin
from .models import Category, Product

# تسجيل الأصناف
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

# تسجيل المنتجات
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')

