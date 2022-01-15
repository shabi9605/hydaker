from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator 


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

# Create your models here.
customer='customer'
staff='staff'
user_types=[(customer,'customer'),(staff,'staff')]

class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField(blank=True)
    image=models.ImageField(upload_to='images',default='default.png')
    user_type=CharField(max_length=20,choices=user_types,default=customer)
    postal_code = models.CharField(max_length=20,blank=True,null=True)
    country =CountryField(default='india')    
    state=models.CharField(max_length=200,blank=True,null=True)
    district = models.CharField(max_length=100,choices=District_name,default=Thrissur)

    def __str__(self):
        return str(self.user.username)





class Exibition(models.Model):
    exibition_name=models.CharField(max_length=100)
    description=models.TextField()
    fisrt_price=models.PositiveIntegerField()
    second_price=models.PositiveIntegerField()
    last_date_exibition=models.DateField()
    image=models.ImageField(upload_to='exibition_image')
    created_date=models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.exibition_name)

class Exibition_Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    exibition_name=models.ForeignKey(Exibition,on_delete=models.CASCADE)
    product=models.ImageField()
    caption=models.CharField(max_length=200)
    description=models.TextField()
    created_date=models.DateField(default=timezone.now)
    winner=models.BooleanField(default=False)
    # paid_for_exibition=models.BooleanField(default=False)

    def __str__(self):
        return str(self.exibition_name)





class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=50)
    feedback=models.TextField()
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    def __str__(self):
        return str(self.user.username)

