from datetime import time
from django.db import models, reset_queries
from pkg_resources import require
from product.models import Product
from account.models import User
from payment.models import *
from django_countries.fields import CountryField


Thiruvananthapuram = 'Thiruvananthapuram'
Kollam = 'Kollam'
Alappuzha= 'Alappuzha'
Pathanamthitta = 'Pathanamthitta'
Kottayam = 'Kottayam'
Idukki = 'Idukki'
Ernakulam = ' Ernakulam'
Thrissur= 'Thrissur'
Palakkad = 'Palakkad'
Malappuram = 'Malappuram'
Kozhikode = ' Kozhikode'
Wayanadu= 'Wayanadu'
Kannur = 'Kannur'
Kasaragod = 'Kasaragod'

District_name =(
    (Thiruvananthapuram , 'Thiruvananthapuram'),
    (Kollam , 'Kollam'),
    (Alappuzha , 'Alappuzha'),
    (Pathanamthitta , 'Pathanamthitta'),
    (Kottayam , 'Kottayam'),
    (Idukki , 'Idukki'),
    ( Ernakulam , ' Ernakulam'),
    (Thrissur, 'Thrissur'),
    (Palakkad , 'Palakkad'),
    (Malappuram , 'Malappuram'),
    (Kozhikode, ' Kozhikode'),
    (Wayanadu, 'Wayanadu'),
    (Kannur , 'Kannur'),
    (Kasaragod , 'Kasaragod')
)
pending='pending'
packed='packed'
shipped='shipped'
delivered='delivered'
delivery_statuses=[
        (pending,'pending'),
        (packed,'packed'),
        (shipped,'shipped'),
        (delivered,'delivered')
    ]
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=250)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20)
    country =CountryField()    
    state=models.CharField(max_length=200)
    district = models.CharField(max_length=100,choices=District_name,default=Thrissur)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20,choices=delivery_statuses,default=pending)
    deliverd_date=models.DateField(default=timezone.now)
    paid = models.BooleanField(default=False)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {} {}'.format(self.user, self.id,self.user)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())

   

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    order = models.ForeignKey(Order,
    related_name='order_items',
    on_delete=models.CASCADE,
    )
    product = models.ForeignKey(Product,
    related_name='order_products',
    on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


    def save(self,*args,**kwargs):
        s=OrderItem.objects.prefetch_related('product').all() 
        print(s)
        
        super().save(*args, **kwargs)




class Tracking(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    packed_date=models.DateField(default=timezone.now,null=True,blank=True)
    shipped_date=models.DateField(default=timezone.now,null=True,blank=True)
    delivered_date=models.DateField(default=timezone.now,null=True,blank=True)
    def __str__(self):
        return str(self.order.user.username)
