from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class Customer(AbstractUser):
    username = models.CharField(_('Username'), unique=True, max_length=32, blank=False)
    email = models.EmailField(_('email'), unique=True, blank=False)
    first_name =  models.CharField(_('Ime'), max_length=32, blank=False)
    lastname_name =  models.CharField(_('Prezime'), max_length=32, blank=False)
    broj_telefona = models.IntegerField(_('Broj telefona'), null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email