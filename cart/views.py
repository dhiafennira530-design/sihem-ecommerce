from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Product

# Add to Cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity < 1:
        quantity = 1

    # أخذ session key
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart_item, created = CartItem.objects.get_or_create(session_key=session_key, product=product)
    cart_item.quantity = quantity
    cart_item.save()

    return redirect('cart_detail')


# Cart Detail
def cart_detail(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price() for item in items)

    return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})


# Update Cart
def update_cart(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                cart_item_id = int(key.split('_')[1])
                cart_item = get_object_or_404(CartItem, id=cart_item_id, session_key=session_key)
                try:
                    qty = int(value)
                    if qty < 1:
                        qty = 1
                except ValueError:
                    qty = 1
                cart_item.quantity = qty
                cart_item.save()
    return redirect('cart_detail')



