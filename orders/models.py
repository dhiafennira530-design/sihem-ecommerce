from django.db import models
from products.models import Product

# كل عنصر في الطلب
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"

# الطلب النهائي
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    ]

    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True)
    customer_address = models.TextField(blank=True)
    items = models.ManyToManyField(OrderItem, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_email}"

