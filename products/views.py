from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# الصفحة الرئيسية: عرض جميع المنتجات
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})

# صفحة تفاصيل المنتج
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

