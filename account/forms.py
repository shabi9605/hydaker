
from django import forms
from django.db.models import fields
from django.forms.widgets import PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','email','password1','password2')


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model=Register
        fields=('phone','image',)

class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')

    class Meta:
        model=User
        fields=('username','email','first_name','last_name')

class UpdateProfileForm(forms.ModelForm):
    address=forms.Textarea()
    image=forms.ImageField()
    class Meta:
        model=Register
        fields=('phone','image','country','state','district','postal_code')



class ExibitionForm(forms.ModelForm):

    class Meta:
        model=Exibition_Register
        fields=('exibition_name','product','caption','description')




class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('title','feedback','rating')