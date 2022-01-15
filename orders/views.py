from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from .models import *
from cart1.models import Cart
from account.models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse,Http404

# Create your views here.


def order_save(request):
    cart = Cart.objects.get(user=request.user)
    address=request.POST.get('address')
    address_second=request.POST.get('address_secound')
    postal_code = request.POST.get('zip')
    country = request.POST.get('country')
    state = request.POST.get('state')
    stock="no"
    for item in cart.items.all():
        if item.quantity>item.product.stock:
            stock="yes"
            break
    
    if stock == 'yes':
        messages.success(request,'Some Product is out Of Stock')
        return redirect('cart:cart_detail')
    else:

        order = Order.objects.create(user=request.user,address=address,
        address_second=address_second,
        postal_code=postal_code,country=country,state=state,
        
        )   
        cart = Cart.objects.get(user=request.user)
        order.save()
        for item in cart.items.all():
            print(item.quantity)
            orderItem, created = OrderItem.objects.update_or_create(user=order.user,
                order=order, product=item.product, price=item.price, quantity=item.quantity,)
            order.order_items.add(orderItem)
        return render(request,'payment/process.html')
    
def order_create(request):
    profile = get_object_or_404(Register,user=request.user)
    cart = Cart.objects.get(user=request.user)
    return render(request, 'orders/order_list.html', {'cart': cart, 'profile': profile})

def orderview(request):
    # print(s)
    order=Order.objects.all().order_by('-id')
    print(order)
    print(request.user.id)
    return render(request,'order/order_view.html',{'order':order})

def orderitemview(request,p_id):
    p=Product.objects.get(id=p_id)
    order=OrderItem.objects.filter(product=p)
    return render(request,'order/orderitem_view.html',{'order':order})

def neworder(request):
    a=OrderItem.objects.filter(user=request.user)
    return render(request,'orders/our_orders.html',{'order':a})

def update_order(request,id):
    Update = Order.objects.get(id=id)
    print(Update)
    form= OrderFormUpdate(instance=Update)
    if request.method=='POST':
        form= OrderFormUpdate(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'order/order_edit.html',{'form':form,'product':Update})

def delete_order(request,id):
    deleteemp = OrderItem.objects.get(id=id)
    deleteemp.delete()
    messages.success(request,'Record deleted succefully')
    return redirect('dashboard/dashboard')



def add_tracking(request,id):
    order=Order.objects.get(id=id)
    if request.method=="POST":
        complaint_form=TrackingForm(request.POST)
        if complaint_form.is_valid():
            cp=Tracking(order=order,packed_date=complaint_form.cleaned_data['packed_date'],shipped_date=complaint_form.cleaned_data['shipped_date'],
            delivered_date=complaint_form.cleaned_data['delivered_date'])
            cp.save()
            return redirect('orders:view_all_tracking')
        else:
            return HttpResponse("Invalid form")
    complaint_form=TrackingForm()
    return render(request,'order/add_tracking.html',{'form':complaint_form})



def view_my_tracking(request):
    tracking=Tracking.objects.filter(order__user=request.user).order_by('-id')
    return render(request,'order/view_tracking.html',{'tracking':tracking})

def view_all_tracking(request):
    tracking=Tracking.objects.all().order_by('-id')
    return render(request,'order/view_tracking.html',{'tracking':tracking})



def update_tracking(request,id):
    Update = Tracking.objects.get(id=id)
    print(Update)
    form= TrackingForm(instance=Update)
    if request.method=='POST':
        form= TrackingForm(request.POST,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('orders:view_all_tracking')
    return render(request,'order/add_tracking.html',{'form':form})


def delete_tracking(request,id):
    Update = Tracking.objects.get(id=id)
    print(Update)
    Update.delete()
    return redirect('orders:view_all_tracking')
