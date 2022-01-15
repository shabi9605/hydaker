from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from product.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from staff.models import *
# Create your views here.
def index(request):
    # categories = Category.objects.all()
    categories=Category.objects.filter(category_type='paintings')
    cate=Category.objects.filter(category_type='accessories')

    print(categories)
        
    listings = Product.objects.order_by('-created').filter(is_available=True)[:6]
  
    context = {
        'listings':listings,  
        'categories':categories,
        'cate':cate,
        }
    return render(request,'index.html',context)

def register(request):
    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form=ProfileForm(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            messages.success(request,'Thank You For Registering')
            return redirect('signin')
        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
       
    return render(request,'account/register.html',{'user_form':user_form,'profile_form':profile_form})

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('dashboard')
            elif user.is_staff and user.register.user_type == 'customer':
                login(request,user)
                return redirect('dashboard')
            else:
                return HttpResponse('not active')
        else:
            messages.error(request,'invalid username or password')
            return redirect('signin')
    else:
        return render(request, 'account/login.html', {})
    


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    # today=datetime.now()
    # total_product=Product.objects.count()
    # today_product=Product.objects.filter(created=today).count()
    # customer=Register.objects.filter(user_type='customer').count()

    # context = {
    #     'product':total_product,
    #     'today_product':today_product,
    #     'customer':customer,
    # }
    return render(request,'dashboard/dashboard.html')


def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCEFULLY UPDATED")
            return render(request,'account/change_password.html')
        else:
            messages.error(request,'PLEASE CORRECT ERROR')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'account/change_password.html',{'form':form})


def update_profile(request):

    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        
        update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.register)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_profile_form=UpdateProfileForm(instance=request.user.register)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'account/update_profile.html',context)

def howwork(request):
    return render(request, 'howitworks.html')

def about(request):
    return render(request, 'about-us.html')



def add_feedback(request):
    if request.method=="POST":
        complaint_form=FeedbackForm(request.POST)
        if complaint_form.is_valid():
            cp=Feedback(user=request.user,title=complaint_form.cleaned_data['title'],feedback=complaint_form.cleaned_data['feedback'],
            rating=complaint_form.cleaned_data['rating'])
            cp.save()
            return redirect('my_feedback')
        else:
            return HttpResponse("Invalid form")
    complaint_form=FeedbackForm()
    return render(request,'account/add_feedback.html',{'form':complaint_form})


def my_feedback(request):
    feedback=Feedback.objects.filter(user=request.user).order_by('-id')
    return render(request,'account/view_feedback.html',{'feedback':feedback})



def view_all_feedback(request):
    feedback=Feedback.objects.all().order_by('-id')
    return render(request,'account/view_feedback.html',{'feedback':feedback})
