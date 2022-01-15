from os import name
from django.urls import path
from .import views

app_name = 'payment'
urlpatterns = [
    path('payment/',views.payment,name='payment'),
    path('payment-status', views.payment_status, name='payment-status'),
    path('allpayment',views.allpayments,name='allpayment'),
    path('userpayment',views.userpaymentview,name='userpayment'),

    path('add_advance_payment',views.add_advance_payment,name='add_advance_payment'),

    path('view_my_adv_payment',views.view_my_adv_payment,name='view_my_adv_payment'),
    path('view_all_advance_payment',views.view_all_advance_payment,name='view_all_advance_payment'),


    
]
