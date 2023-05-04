from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Order
from groomie.models import UniqueWedding, BasicWedding

admin.site.register(Order)
admin.site.register(Customer, UserAdmin)
UserAdmin.fieldsets +=  (('Extra Fields', {'fields': ('broj_telefona', )}),)