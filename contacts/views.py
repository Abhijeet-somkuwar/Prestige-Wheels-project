from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User



# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Check if user is authenticated and prevent duplicate inquiries
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/' + car_id)

        # Save the contact information to the database
        contact = Contact(
            car_id=car_id, car_title=car_title, user_id=user_id,
            first_name=first_name, last_name=last_name, customer_need=customer_need,
            city=city, state=state, email=email, phone=phone, message=message
        )

        # Get the superuser email
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # Construct a detailed email message
        message_body = f"""
New Car Inquiry Details:

Car Title: {car_title}
Car ID: {car_id}

Name: {first_name} {last_name}
Customer Need: {customer_need}

City: {city}
State: {state}
Email: {email}
Phone: {phone}

Message:
{message}

Please log in to the admin panel to view and respond to this inquiry.
"""

        # Send the email notification to the admin
        send_mail(
            subject='New Car Inquiry',
            message=message_body,
            from_email='abhijeet.idevifysolutions@gmail.com',  # Sender's email address
            recipient_list=[admin_email],  # Admin's email address
            fail_silently=False,  # Raise errors if sending fails
        )

        # Save the contact record in the database
        contact.save()

        # Notify the user that their inquiry has been submitted
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/' + car_id)

