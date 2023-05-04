from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class Customer(AbstractUser):
    username = models.CharField(_('Username'), unique=True, max_length=32, blank=False)
    email = models.EmailField(_('email'), unique=True, blank=False)
    first_name =  models.CharField(_('Ime'), max_length=32, blank=False)
    last_name =  models.CharField(_('Prezime'), max_length=32, blank=False)
    broj_telefona = models.IntegerField(_('Broj telefona'), null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email
    
class Order(models.Model):
    order_id = models.CharField(max_length=100, default="")
    cutomer_name = models.ForeignKey(Customer,  related_name='customer_name', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    address = models.CharField(max_length= 50)
    city = models.CharField(max_length= 20)
    post_code = models.CharField(max_length= 5)
    mobile_number = models.CharField(max_length = 14)
    wedding = models.CharField(max_length = 13)
    price = models.FloatField(default=1)
    total_cost = models.FloatField(default=1)
    order_state_list = [
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('confirm', 'Confirm'),   
        ('delivered', 'Delivered'),    
        ]
    order_status = models.CharField(max_length=50, choices=order_state_list, default="pending")

    payment_state_list = [
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('confirm', 'Confirm') 
        ]
    payment_status = models.CharField(max_length=50, choices=payment_state_list, default="pending")
    transaction_id = models.CharField(max_length=100)