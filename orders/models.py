from django.db import models
from users.models import User
from goods.models import Products

class OrderItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT,verbose_name='User',default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True,verbose_name='Created at')
    phone_number =  models.CharField(max_length=20, verbose_name='Phone Number')
    requires_delivery = models.BooleanField(default=False,verbose_name='Required for delivery')
    delivery_address = models.TextField(null=True,blank=True,verbose_name='Delivery Address')
    payment_on_get = models.BooleanField(default=False,verbose_name='Payment on get')
    is_paid = models.BooleanField(default=False,verbose_name='Is paid')
    status = models.CharField(max_length=10, default='Pending',verbose_name='Status')

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'

    def __str__(self):
        return f'Order Number: {self.pk} | Buyer Name: {self.user.first_name} {self.user.last_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE,verbose_name='order',default=None)
    product = models.ForeignKey(to=Products,on_delete=models.SET_DEFAULT,null=True,verbose_name='product',default=None)
    name = models.CharField(max_length=150,verbose_name='Name')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Price')
    quantity = models.PositiveIntegerField(default=0,verbose_name='Quantity')
    created_timestamp = models.DateTimeField(auto_now_add=True,verbose_name='Created at')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Sold product'

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity,2)

    def __str__(self):
        return f'Product{self.name} | Order Number {self.order.pk}'