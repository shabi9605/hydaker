# Generated by Django 3.2.9 on 2021-11-16 15:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='category_image')),
                ('category_type', models.CharField(choices=[('paintings', 'paitings'), ('accessories', 'accessories')], default='paintings', max_length=20)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(max_length=200)),
                ('photo', models.ImageField(upload_to='product_image/%Y/%m/%d')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='product_image/%Y/%m/%d')),
                ('price', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('dimensions', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(max_length=200)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('is_available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.register')),
            ],
            options={
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
