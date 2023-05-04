from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
import random, string
from customers.models import Customer

User = settings.AUTH_USER_MODEL
# Create your models here.
GUEST_TYPE = (
    ('SOLO', 'Solo'),
    ('PAR', 'Par'),
    ('OBITELJ', 'Obitelj'),
)

class UniqueWedding(models.Model):
    wedding_slug = models.SlugField(primary_key=True, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        while not self.wedding_slug:
            slug = [random.sample(string.ascii_letters, 4),random.sample(string.digits, 3), random.sample(string.ascii_letters, 2)]
            random.shuffle(slug)
            newslug = ''.join(''.join(l) for l in slug)
            if not UniqueWedding.objects.filter(pk=newslug).exists():
                self.wedding_slug = newslug

        super().save(*args, **kwargs)

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, related_name='wedding_on_customer')
    created = models.DateTimeField(auto_now_add=True)
    expected_guests = models.SmallIntegerField(null=True, blank=True)
    groom_fname = models.CharField(max_length=16, blank=False, default='')
    groom_lname = models.CharField(max_length=16, blank=False, default='')
    bride_fname = models.CharField(max_length=16, blank=False, default='')
    bried_lname = models.CharField(max_length=16, blank=False, default='')

    wedding_date = models.DateField(blank=False)
    response_date = models.DateField(blank=False)

    groom_gathering = models.CharField(max_length=64, blank=True, default='')
    groom_gathering_time = models.TimeField(blank=True)
    groom_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    groom_longitude = models.FloatField(blank=True, max_length=180, default='0.1')
    bride_gathering = models.CharField(max_length=64, blank=True, default='')
    bride_gathering_time = models.TimeField(blank=True)
    bride_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    bride_longitude = models.FloatField(blank=True, max_length=180, default='0.1')
    church_name = models.CharField(max_length=48, blank=False, default='')
    church_time = models.TimeField(blank=False)
    church_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    church_longitude = models.FloatField(blank=True, max_length=180, default='0.1')
    restaurant_name = models.CharField(max_length=48, blank=False, default='')
    restaurant_time = models.TimeField(blank=False)
    restaurant_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    restaurant_longitude = models.FloatField(blank=True, max_length=180, default='0.1')

    def __str__(self):
        return f'{self.groom_fname} & {self.bride_fname} {self.groom_lname}'


class UniqueGuest(models.Model):
    guest_slug = models.SlugField(primary_key=True, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        while not self.guest_slug:
            slug = [random.sample(string.ascii_letters, 4),random.sample(string.digits, 3), random.sample(string.ascii_letters, 4)]
            random.shuffle(slug)
            newslug = ''.join(''.join(l) for l in slug)
            if not UniqueGuest.objects.filter(pk=newslug).exists():
                self.guest_slug = newslug

        super().save(*args, **kwargs)

    wedding_owner = models.ForeignKey(UniqueWedding, on_delete=models.CASCADE, null=True, related_name='uniquewedding')
    email = models.EmailField(unique=True, blank=True, default='')
    guest_fname = models.CharField(max_length=16, blank=False, default='')
    guest_lname = models.CharField(max_length=16, blank=False, default='')

    plusone_fname = models.CharField(max_length=16, blank=True, default='')
    plusone_lname = models.CharField(max_length=16, blank=True, default='')

    guest_type = models.CharField(blank=False,
                max_length=7,
                choices=GUEST_TYPE,
                default='')

    with_kids = models.BooleanField(default=False)
    couple = models.BooleanField(default=False)
    plusone = models.BooleanField(default=False)
    coming = models.BooleanField(default=False)
    not_coming =models.BooleanField(default=False)
    kids = models.SmallIntegerField(null=True, blank=True)

    message = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return f'{self.wedding_owner}, {self.guest_fname} {self.guest_lname}'


class BasicWedding(models.Model):
    wedding_slug = models.SlugField(primary_key=True, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        while not self.wedding_slug:
            slug = [random.sample(string.ascii_letters, 4),random.sample(string.digits, 3), random.sample(string.ascii_letters, 4)]
            random.shuffle(slug)
            newslug = ''.join(''.join(l) for l in slug)
            if not BasicWedding.objects.filter(pk=newslug).exists():
                self.wedding_slug = newslug

        super().save(*args, **kwargs)

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, related_name='basicwedding')
    created = models.DateTimeField(auto_now_add=True)
    expected_guests = models.SmallIntegerField(null=True, blank=True)
    groom_fname = models.CharField(max_length=16, blank=False, default='')
    groom_lname = models.CharField(max_length=16, blank=False, default='')
    bride_fname = models.CharField(max_length=16, blank=False, default='')
    bried_lname = models.CharField(max_length=16, blank=False, default='')

    wedding_date = models.DateField(blank=False)
    response_date = models.DateField(blank=False)

    groom_gathering = models.CharField(max_length=64, blank=True, default='')
    groom_gathering_time = models.TimeField(blank=True)
    groom_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    groom_longitude = models.FloatField(blank=True, max_length=180, default='0.1')
    bride_gathering = models.CharField(max_length=64, blank=True, default='')
    bride_gathering_time = models.TimeField(blank=True)
    bride_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    bride_longitude = models.FloatField(blank=True, max_length=180, default='0.1')
    church_name = models.CharField(max_length=48, blank=False, default='')
    church_time = models.TimeField(blank=False)
    church_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    church_longitude = models.FloatField(blank=True, max_length=180, default='0.1')
    restaurant_name = models.CharField(max_length=48, blank=False, default='')
    restaurant_time = models.TimeField(blank=False)
    restaurant_latitude = models.FloatField(blank=True, max_length=90, default='0.1')
    restaurant_longitude = models.FloatField(blank=True, max_length=180, default='0.1')

    def __str__(self):
        return f'{self.groom_fname} & {self.bride_fname} {self.groom_lname}'

class BasicGuest(models.Model):
    guest_slug = models.SlugField(primary_key=True, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        while not self.guest_slug:
            slug = [random.sample(string.ascii_letters, 4),random.sample(string.digits, 3), random.sample(string.ascii_letters, 2)]
            random.shuffle(slug)
            newslug = ''.join(''.join(l) for l in slug)
            if not BasicGuest.objects.filter(pk=newslug).exists():
                self.guest_slug = newslug

        super().save(*args, **kwargs)

    wedding_owner = models.ForeignKey(BasicWedding, on_delete=models.CASCADE, null=True, related_name='basicwedding')
    email = models.EmailField(unique=True, blank=True, default='')
    guest_fname = models.CharField(max_length=16, blank=False, default='')
    guest_lname = models.CharField(max_length=16, blank=False, default='')

    plusone_fname = models.CharField(max_length=16, blank=True, default='')
    plusone_lname = models.CharField(max_length=16, blank=True, default='')

    with_kids = models.BooleanField(default=False)
    plusone = models.BooleanField(default=False)
    coming = models.BooleanField(default=False)
    not_coming =models.BooleanField(default=False)
    kids = models.SmallIntegerField(null=True, blank=True)

    message = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return f'{self.wedding_owner}, {self.guest_fname} {self.guest_lname}'