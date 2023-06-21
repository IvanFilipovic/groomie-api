# Generated by Django 4.1.7 on 2023-06-19 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueWedding',
            fields=[
                ('wedding_slug', models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expected_guests', models.SmallIntegerField(blank=True, null=True)),
                ('groom_fname', models.CharField(default='', max_length=16)),
                ('groom_lname', models.CharField(default='', max_length=16)),
                ('bride_fname', models.CharField(default='', max_length=16)),
                ('bride_lname', models.CharField(default='', max_length=16)),
                ('wedding_date', models.DateField()),
                ('response_date', models.DateField()),
                ('groom_gathering', models.CharField(blank=True, default='', max_length=64)),
                ('groom_gathering_time', models.TimeField(blank=True)),
                ('groom_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('groom_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('bride_gathering', models.CharField(blank=True, default='', max_length=64)),
                ('bride_gathering_time', models.TimeField(blank=True)),
                ('bride_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('bride_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('church_name', models.CharField(default='', max_length=48)),
                ('church_time', models.TimeField()),
                ('church_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('church_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('restaurant_name', models.CharField(default='', max_length=48)),
                ('restaurant_time', models.TimeField()),
                ('restaurant_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('restaurant_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('card_theme', models.CharField(blank=True, default='', max_length=28)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wedding_on_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UniqueGuest',
            fields=[
                ('guest_slug', models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('guest_fname', models.CharField(default='', max_length=16)),
                ('guest_lname', models.CharField(default='', max_length=16)),
                ('plusone_fname', models.CharField(blank=True, default='', max_length=16)),
                ('plusone_lname', models.CharField(blank=True, default='', max_length=16)),
                ('guest_type', models.CharField(choices=[('SOLO', 'Solo'), ('PAR', 'Par'), ('OBITELJ', 'Obitelj')], default='', max_length=7)),
                ('with_kids', models.BooleanField(default=False)),
                ('solo', models.BooleanField(default=False)),
                ('couple', models.BooleanField(default=False)),
                ('plusone', models.BooleanField(default=False)),
                ('coming', models.BooleanField(default=False)),
                ('not_coming', models.BooleanField(default=False)),
                ('kids', models.SmallIntegerField(blank=True, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=256)),
                ('wedding_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uniquewedding', to='groomie.uniquewedding')),
            ],
        ),
        migrations.CreateModel(
            name='BasicWedding',
            fields=[
                ('wedding_slug', models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expected_guests', models.SmallIntegerField(blank=True, null=True)),
                ('groom_fname', models.CharField(default='', max_length=16)),
                ('groom_lname', models.CharField(default='', max_length=16)),
                ('bride_fname', models.CharField(default='', max_length=16)),
                ('bride_lname', models.CharField(default='', max_length=16)),
                ('wedding_date', models.DateField()),
                ('response_date', models.DateField()),
                ('groom_gathering', models.CharField(blank=True, default='', max_length=64)),
                ('groom_gathering_time', models.TimeField(blank=True)),
                ('groom_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('groom_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('bride_gathering', models.CharField(blank=True, default='', max_length=64)),
                ('bride_gathering_time', models.TimeField(blank=True)),
                ('bride_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('bride_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('church_name', models.CharField(default='', max_length=48)),
                ('church_time', models.TimeField()),
                ('church_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('church_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('restaurant_name', models.CharField(default='', max_length=48)),
                ('restaurant_time', models.TimeField()),
                ('restaurant_latitude', models.FloatField(blank=True, default='0.1', max_length=90)),
                ('restaurant_longitude', models.FloatField(blank=True, default='0.1', max_length=180)),
                ('card_theme', models.CharField(blank=True, default='', max_length=28)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basicwedding', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasicGuest',
            fields=[
                ('guest_slug', models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('guest_fname', models.CharField(default='', max_length=16)),
                ('guest_lname', models.CharField(default='', max_length=16)),
                ('plusone_fname', models.CharField(blank=True, default='', max_length=16)),
                ('plusone_lname', models.CharField(blank=True, default='', max_length=16)),
                ('with_kids', models.BooleanField(default=False)),
                ('solo', models.BooleanField(default=False)),
                ('plusone', models.BooleanField(default=False)),
                ('coming', models.BooleanField(default=False)),
                ('not_coming', models.BooleanField(default=False)),
                ('kids', models.SmallIntegerField(blank=True, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=256)),
                ('wedding_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basicwedding', to='groomie.basicwedding')),
            ],
        ),
    ]
