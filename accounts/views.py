from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from cars.models import CarOrder


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not firstname.isalpha() or not lastname.isalpha():
            messages.error(request, 'First name and last name must contain only letters.')
            return redirect('register')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=username,
                    password=password
                )
                
                # Send confirmation email
                subject = 'Welcome to Prestige Wheels!'
                message = f"Hi {firstname},\n\nThank you for registering at Prestige Wheels.\n\nYou can now login to your dashboard to explore more.\n\nRegards,\nTeam Prestige Wheels"
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('dashboard')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')



@login_required(login_url = 'login')
def dashboard(request):
    user = request.user
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=user.id)
    purchased_cars = CarOrder.objects.filter(user=user, payment_status='paid').order_by('-order_date')

    context = {
        'inquiries': user_inquiry,
        'purchased_cars': purchased_cars,  
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

