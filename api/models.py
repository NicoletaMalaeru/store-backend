from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank = True)
    email = models.CharField(max_length=200, null=True, blank = True)
    phone = models.CharField(max_length=200, null=True, blank = True)
    address_city = models.CharField(max_length=200, null=True, blank = True)
    address_street = models.CharField(max_length=200, null=True, blank = True)
    address_postal_code = models.CharField(max_length=200, null=True, blank = True)

    def __str__(self):
        return self.name

class Categories(models.Model):
    category = models.CharField(max_length=200, null=True, blank = True)

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=200)
    category =models.ForeignKey(Categories, null=True, blank = True, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=2000, null=True, blank = True)
    details = models.CharField(max_length=2000, null=True, blank=True)
    ingredients = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null = True, blank = True)
    number_sold = models.IntegerField()
    stoc = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Review(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank = True)
    mail =  models.CharField(max_length=200,null=True, blank = True)
    review = models.IntegerField(null=True, blank = True)
    comment = models.CharField(max_length=200,null=True, blank = True)

class Order(models.Model):
    status_options = (
        ('primita', 'Primita'),
        ('anulata', 'Anulata'),
        ('pregatire', 'In curs de pregatire'),
        ('in_livrare', 'Se livreaza'),
        ('livrata', 'Livrata'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 50, choices= status_options, default='primita')
    transaction_id = models.CharField(max_length=100, null=True)
    comments = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        print(orderitems)
        for item in orderitems:
            print(item)
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        print(orderitems)
        for item in orderitems:
            print(item)
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address