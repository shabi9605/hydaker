# Generated by Django 3.2.6 on 2022-01-10 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_customize_foam_material_polish_wood'),
    ]

    operations = [
        migrations.AddField(
            model_name='customize',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CustOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('address_second', models.CharField(blank=True, max_length=250, null=True)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kollam', 'Kollam'), ('Alappuzha', 'Alappuzha'), ('Pathanamthitta', 'Pathanamthitta'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), (' Ernakulam', ' Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), (' Kozhikode', ' Kozhikode'), ('Wayanadu', 'Wayanadu'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], default='Thrissur', max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customize',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.custorder'),
        ),
    ]