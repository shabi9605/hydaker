from django.db import models
from datetime import datetime

from django.db.models.fields import NullBooleanField
from account.models import *
from django.urls import reverse



# Create your models here.
sofa='sofa'
bed='bed'
shelves='shelves'
chair='chair'
table='table'
category_types=[(sofa,'sofa'),(bed,'bed'),(shelves,'shelves'),(chair,'chair'),(table,'table')]
# color


#foam

pu_foam='PU foam'
rubber_foam='rubber foam'
foam_types=[(pu_foam,'PU foam'),(rubber_foam,'rubber foam')]

#material
cloth='cloth'
rexine='rexine'
leather='leather'

materials_types=[(cloth,'cloth'),(rexine,'rexine'),(leather,'leather')]


class Category(models.Model):
    name=models.CharField(max_length=50,db_index=True)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='category_image')
    category_type=models.CharField(max_length=20,choices=category_types,default=sofa)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])
class Color(models.Model):
    color=models.CharField(max_length=50)

    def __str__(self):
        return str(self.color)
   
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    photo=models.ImageField(upload_to='product_image/%Y/%m/%d')
    photo1=models.ImageField(upload_to='product_image/%Y/%m/%d',blank=True,null=True)
    photo2=models.ImageField(upload_to='product_image/%Y/%m/%d',blank=True,null=True)
    photo3=models.ImageField(upload_to='product_image/%Y/%m/%d',blank=True,null=True)
    price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    dimensions=models.CharField(max_length=200,blank=True,null=True)
    warrenty=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField()
    contact_number=PhoneNumberField(blank=True,null=True)
    basic_color=models.ForeignKey(Color,blank=True,null=True,on_delete=models.CASCADE)
    materials=models.CharField(max_length=30,blank=True,null=True,choices=materials_types,default=leather)
    foam=models.CharField(max_length=30,blank=True,null=True,choices=foam_types,default=pu_foam)
    wood_name=models.CharField(max_length=50,blank=True,null=True)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('account:product_detail', args=[self.id, self.slug])



    # def save(self,*args,**kwargs):
    #     print('hr')
    #     m = PaymentSeller.objects.filter(user=self.user)  
    #     print(m)
    #     super().save(*args, **kwargs)


class Wood(models.Model):
    wood_type=models.CharField(max_length=50)
    def __str__(self):
        return str(self.wood_type)


class Material(models.Model):
    material_type=models.CharField(max_length=50)
    def __str__(self):
        return str(self.material_type)


class Foam(models.Model):
    foam_type=models.CharField(max_length=50)
    def __str__(self):
        return str(self.foam_type)


class Polish(models.Model):
    polish_type=models.CharField(max_length=50)
    def __str__(self):
        return str(self.polish_type)


class CustOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=250)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20)
    country =CountryField()    
    state=models.CharField(max_length=200)
    district = models.CharField(max_length=100,choices=District_name,default=Thrissur)
    def __str__(self):
        return str(self.user.username)



class Customize(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    customer=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    order=models.ForeignKey(CustOrder,on_delete=models.CASCADE,null=True,blank=True)
    wood=models.ForeignKey(Wood,on_delete=models.CASCADE,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    material=models.ForeignKey(Material,on_delete=models.CASCADE,null=True,blank=True)
    dimension=models.CharField(max_length=50)
    polish=models.ForeignKey(Polish,on_delete=models.CASCADE,null=True,blank=True)
    foam=models.ForeignKey(Foam,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.user.username)



    


    
