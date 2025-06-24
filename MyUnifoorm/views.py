from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User,Product,Order,Review
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
# Create your views here.

def main(request):
    email = request.session.get('user_email')
    if request.user.is_authenticated:
        user = request.user
        print("User is authenticated:", user)  # Debug statement
    else:
        user = None
    return render(request, 'main.html', {'user': user})




def signup(request):
    user=User.objects.all().values()
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        name = request.POST.get('Name')
        phoneNumber = request.POST.get('PhoneNumber')
        address = request.POST.get('Address')

        user = User(Email=email, Password=password, Name=name, PhoneNumber=phoneNumber , Address = address)
        user.save()
        return redirect('login')  
    return render(request,'signup.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(Email=email, Password=password).first()
        if user:
            request.session['user_email'] = user.Email
            request.user = user  # Set the request.user object
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')


    

def profile(request, email):
    email = request.session.get('user_email')
    if email:
        try:
            user = User.objects.get(Email=email)

            if request.method == 'POST':
                password = request.POST.get('Password')
                name = request.POST.get('Name')
                phone_number = request.POST.get('PhoneNumber')
                address = request.POST.get('Address')

                if password and len(password) <= 12:
                    user.Password = password
                if name:
                    user.Name = name
                if phone_number and len(phone_number) <= 13:
                    user.PhoneNumber = phone_number
                if address:
                    user.Address = address

                user.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile', email=email)
            return render(request, 'profile.html', {'user': user})
        except User.DoesNotExist:
            return redirect('login')  # Redirect to login if user does not exist
    else:
        return redirect('login')

def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect('main')

def product_view(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def order(request, product_id):
    email = request.session.get('user_email')
    if not email:
        return redirect('login')  # Redirect to login if no email is found in session
    
    user = User.objects.get(Email=email)
    product = Product.objects.get(ProductID=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        
        if quantity > product.Quantity:
            return HttpResponse("Not enough stock available.")
        
        total_amount = quantity * product.Price
        order = Order(
            Email=user,
            ProductID=product,
            Qty=quantity,  # added this field
            OrderDate=datetime.date.today(),
            OrderStatus='Successful',
            TotalAmount=total_amount
        )
        order.save()
        
        # Reduce the product quantity
        product.Quantity -= quantity
        product.save()  # Save the updated product object
        

        return render(request, 'receipt.html', {'order': order, 'user': user, 'product': product})

    else:

        return render(request, 'order.html', {'user': user, 'product': product, })

def my_orders(request):
    orders = Order.objects.filter(Email=request.session.get('user_email'))
    return render(request, 'orderhistory.html', {'orders': orders})
def update_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    user = order.Email
    old_qty = order.Qty  # Store the old quantity to adjust stock later

    if request.method == 'POST':
        new_qty = int(request.POST.get('qty'))
        new_address = request.POST.get('address')

        # Update order quantity and total amount
        order.Qty = new_qty
        order.TotalAmount = order.ProductID.Price * new_qty
        
        # Update user's shipping address
        user.Address = new_address
        user.save()

        # Adjust stock
        product = order.ProductID
        product.Quantity += (old_qty - new_qty)  # Increase or decrease stock based on the new quantity
        product.save()

        # Save order changes
        order.save()

        messages.success(request, 'Order updated successfully')
        return redirect('my_orders')
    
    return render(request, 'update_order.html', {'order': order})

def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    product = order.ProductID

    # Adjust stock
    product.Quantity += order.Qty
    product.save()

    # Delete the order
    order.delete()

    messages.success(request, 'Order canceled successfully')
    return redirect('my_orders')
# views.py

def add_review(request, order_id):
    order = Order.objects.get(OrderID=order_id)
    user = User.objects.get(Email=request.session.get('user_email'))
    if request.method == 'POST':
        comment = request.POST.get('comment')
        review = Review(
            OrderID=order,
            Email=user,
            Comment=comment,
            ReviewDate=datetime.date.today()
        )
        review.save()
        # Redirect to the review page for this product
        return redirect('review', product_id=order.ProductID.ProductID)
    return render(request, 'review.html', {'order': order}) #add_review.html


def review(request, product_id):

    product = Product.objects.get(ProductID=product_id)
    reviews = Review.objects.filter(OrderID__ProductID=product)
    return render(request, 'review.html', {'reviews': reviews, 'product': product})


