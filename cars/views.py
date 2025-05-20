from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from django.shortcuts import render, redirect, get_object_or_404
from .models import CarOrder, Car
from django.contrib.auth.decorators import login_required

from django.conf import settings

from django.db.models import Q


import razorpay
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car, CarOrder

from django.contrib import messages


# Create your views here.
def cars(request):
    cars_queryset = Car.objects.all().order_by('-created_date')
    paginator = Paginator(cars_queryset, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)



@login_required
def initiate_payment(request, id):
    car = get_object_or_404(Car, id=id)

    if car.is_sold:
        messages.error(request, "This car has already been sold.")
        return redirect('car_detail', id=car.id)


    # Razorpay test credentials
    client = razorpay.Client(auth=("rzp_test_6wZ986hRbPrnoS", "56gj07Rf6EL4i8Olc3Z1UyLn"))
    amount = min(car.price * 100, 50000000)

    data = {
        "amount": amount,  # amount in paise
        "currency": "INR",
        "receipt": f"order_rcptid_{car.id}"
    }

    payment = client.order.create(data=data)

    # Save initial order in DB with pending status
    order = CarOrder.objects.create(
        user=request.user,
        car=car,
        total_amount=car.price,
        payment_status="pending"
    )

    context = {
    "car": car,
    "order": order,
    "razorpay_order_id": payment['id'],  # Razorpay's order ID
    "razorpay_key": "rzp_test_6wZ986hRbPrnoS"
}


    return render(request, 'cars/payment.html', context)





@csrf_exempt
def payment_success(request):
    order_id = request.GET.get('order_id')
    if not order_id:
        return redirect('cars')  # or wherever you want to redirect if no order_id

    order = get_object_or_404(CarOrder, id=order_id, user=request.user)

    # Mark car as sold
    car = order.car
    car.is_sold = True
    car.save()

    # Update payment status
    order.payment_status = 'paid'
    order.save()

    # Send confirmation email to buyer
    subject = 'Purchase Confirmation - PrestigeCars'
    message = f"Dear {order.user.username},\n\nThank you for purchasing {car.car_title}.\nYour payment of ₹{order.total_amount} has been successfully received.\n\nRegards,\nPrestigeCars Team"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [order.user.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    return render(request, 'cars/payment_success.html', {'order': order, 'car': car})