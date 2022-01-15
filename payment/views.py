from django.contrib import messages
from .models import *
from django.shortcuts import render
import razorpay
from .forms import PaymentForm
from cart1.models import *
from orders.models import *

def payment(request):
    t=request.user.cart.total_amount
    cart=Cart.objects.get(user=request.user)
    # print(order.amount)

    if request.method == "POST":
        # name = request.POST.get('name')
        # amount1=request.POST.get('amount')
        amount = t *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        print(request.user.cart.total_amount)
        t=request.user.cart.total_amount
        
        if order_status == 'created':
            payment = Payment(
                amount=t,
                order_id=order_id,
                total_amount=t,
                user=request.user,
                
            )
          
        payment.save()
        response_payment['user'] = request.user
        cart=Cart.objects.get(user=request.user)
        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment.html', {'form':form,'payment': response_payment,'cart':cart})

    form = PaymentForm()
    return render(request, 'payment/payment.html', {'form': form,'amount':t,'cart':cart})





def add_advance_payment(request):
    #t=request.user.cart.total_amount
    #cart=Cart.objects.get(user=request.user)
    # print(order.amount)
    amount1=5000
    cust=request.session['cust']
    if request.method == "POST":
        # name = request.POST.get('name')
        amount1=5000
        amount = amount1 *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        print(request.user.cart.total_amount)
        t=request.user.cart.total_amount
        customer=Register.objects.get(user=request.user)
        customize=Customize.objects.get(id=cust)
        if order_status == 'created':
            payment = AdvancePayment(
                adv_amount=amount1,
                order_id=order_id,
                customer=customer,
                customize=customize,
                user=request.user,
                
            )
          
        payment.save()
        response_payment['user'] = request.user
        cart=Cart.objects.get(user=request.user)
        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment2.html', {'form':form,'payment': response_payment,'cart':cart,'amount':amount1})

    form = PaymentForm()
    return render(request, 'payment/payment2.html', {'form': form,'amount':amount1})





def payment_status(request):
    response = request.POST
    params_dict = {

       'razorpay_order_id': response['razorpay_order_id'],
       'razorpay_payment_id': response['razorpay_payment_id'],
       'razorpay_signature': response['razorpay_signature'],
     
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
    

    try:
        try:
            status = client.utility.verify_payment_signature(params_dict)
            payment = Payment.objects.get(order_id=response['razorpay_order_id'])
            payment.payment_id = response['razorpay_payment_id']

            payment.is_paid = True
            payment.save()
            return render(request, 'payment/payment_status.html', {'status': True,'payment_id':payment.payment_id})
        except:
            pass
        try:
            status = client.utility.verify_payment_signature(params_dict)
            payment = AdvancePayment.objects.get(order_id=response['razorpay_order_id'])
            payment.payment_id = response['razorpay_payment_id']

            payment.is_paid = True
            payment.save()
            return render(request, 'payment/payment_status.html', {'status': True,'payment_id':payment.payment_id})
        except:
            pass

    except:
        return render(request, 'payment/payment_status.html', {'status': False})

    


def allpayments(request):
    payall=Payment.objects.all()
    return render(request,'payment/allpayment.html',{'payall':payall})

def userpaymentview(request):
    userpay=Payment.objects.filter(user=request.user)
    return render(request,'payment/userpayment.html',{'userpay':userpay})



def view_my_adv_payment(request):
    adv_payment=AdvancePayment.objects.filter(user=request.user,is_paid=True).order_by('-id')
    return render(request,'payment/view_advance_payment.html',{'adv_payment':adv_payment})


def view_all_advance_payment(request):
    adv_payment=AdvancePayment.objects.filter(is_paid=True).order_by('-id')
    return render(request,'payment/view_advance_payment.html',{'adv_payment':adv_payment})
    