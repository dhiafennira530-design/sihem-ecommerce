from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order, OrderItem

def checkout(request):
    # التأكد من وجود session
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    # جمع عناصر السلة حسب session_key
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')

        if not cart_items:
            # إذا السلة فارغة، نرجع مباشرة للصفحة
            return render(request, 'orders/checkout.html', {
                'cart_items': cart_items,
                'total': total,
                'error': 'Votre panier est vide.'
            })

        # إنشاء Order
        order = Order.objects.create(
            customer_email=email,
            customer_phone=phone,
            customer_address=address,
            total_price=total
        )

        # إضافة عناصر الطلب
        for item in cart_items:
            order_item = OrderItem.objects.create(
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            order.items.add(order_item)

        # مسح السلة بعد الطلب
        cart_items.delete()

        return render(request, 'orders/checkout_success.html', {'order': order})

    # GET request => عرض الصفحة مع cart_items و total
    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

