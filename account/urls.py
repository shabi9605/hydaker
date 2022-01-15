from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('password/',views.change_password,name="change_password"),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('howworks/',views.howwork,name='howwork'),
    path('about/',views.about,name='about'),
    path('add_feedback',views.add_feedback,name='add_feedback'),
    path('my_feedback',views.my_feedback,name='my_feedback'),
    path('view_all_feedback',views.view_all_feedback,name='view_all_feedback'),
 






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)