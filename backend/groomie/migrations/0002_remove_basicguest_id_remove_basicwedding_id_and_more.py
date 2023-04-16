# Generated by Django 4.1.7 on 2023-04-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groomie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicguest',
            name='id',
        ),
        migrations.RemoveField(
            model_name='basicwedding',
            name='id',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='id',
        ),
        migrations.RemoveField(
            model_name='uniquewedding',
            name='id',
        ),
        migrations.AlterField(
            model_name='basicguest',
            name='guest_slug',
            field=models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='basicwedding',
            name='wedding_slug',
            field=models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='guest_slug',
            field=models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='uniquewedding',
            name='wedding_slug',
            field=models.SlugField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
