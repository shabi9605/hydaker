
from django.urls import path
from . import views
app_name='orders'

urlpatterns = [
   
    path('create/',views.order_create,name="order_create"),
    path('process/',views.order_save,name="order_save"),
    path('orderview/',views.orderview,name='orderview'),
    path('orderitemview/<int:p_id>/',views.orderitemview,name='orderitemview'),
    path('neworder/',views.neworder,name="neworder"),
    path('update_order/<int:id>/',views.update_order,name="update_order"),
    path('delete_order/<int:id>/',views.delete_order,name="delete_order"),

    path('add_tracking/<int:id>',views.add_tracking,name='add_tracking'),
    path('view_my_tracking',views.view_my_tracking,name='view_my_tracking'),
    path('view_all_tracking',views.view_all_tracking,name='view_all_tracking'),

    path('update_tracking/<int:id>',views.update_tracking,name='update_tracking'),
    path('delete_tracking/<int:id>',views.delete_tracking,name='delete_tracking'),


    
]
