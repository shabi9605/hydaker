# Generated by Django 3.2.6 on 2022-01-10 06:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderitem_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packed_date', models.DateField(default=django.utils.timezone.now)),
                ('shipped_date', models.DateField(default=django.utils.timezone.now)),
                ('delivered_date', models.DateField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]