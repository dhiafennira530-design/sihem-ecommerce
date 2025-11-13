# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

# Inline باش تظهر العناصر متاع الطلب داخل صفحة كل Order
class OrderItemInline(admin.TabularInline):
    model = Order.items.through  # ManyToMany relation
    extra = 0  # ما يظهرش أسطر زيادة فارغة

# تسجيل الـ Order في الـ admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_email', 'customer_phone', 'customer_address', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_email', 'customer_phone', 'customer_address')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at',)
