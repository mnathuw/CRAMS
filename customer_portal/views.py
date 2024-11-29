from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from customer_portal.models import *
from django.contrib.auth.decorators import login_required
from car_dealer_portal.models import *
from django.http import HttpResponseRedirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.shortcuts import render

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'customer/login.html')
    else:
        return render(request, 'customer/home_page.html')

def login(request):
    return render(request, 'customer/login.html')

def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'customer/home_page.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            customer = Customer.objects.get(user = user)
        except:
            customer = None
        if customer is not None:
            auth.login(request, user)
            return render(request, 'customer/home_page.html')
        else:
            return render(request, 'customer/login_failed.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'customer/login.html')

def register(request):
    return render(request, 'customer/register.html')

def registration(request):
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    city = request.POST['city']
    city = city.lower()
    province = request.POST['province']
    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'customer/registration_error.html')
    try:
        area = Area.objects.get(city = city, province = province)
    except:
        area = None
    if area is not None:
        customer = Customer(user = user, mobile = mobile, area = area)
    else:
        area = Area(city = city, province = province)
        area.save()
        area = Area.objects.get(city = city, province = province)
        customer = Customer(user = user, mobile = mobile, area = area)

    customer.save()
    return render(request, 'customer/registered.html')

@login_required
def search(request):
    return render(request, 'customer/search.html')

@login_required
def search_results(request):
    city = request.POST.get('city', '').lower()  # Get city if provided
    vin = request.POST.get('vin', '').strip()  # Get VIN number if provided
    vehicles_list = []

    # If VIN is provided, filter by VIN
    if vin:
        vehicles = Vehicle.objects.filter(vin_no=vin)  # Use 'vin_no' to filter
        for car in vehicles:
            if car.is_available:
                vehicle_dictionary = {
                    'name': car.car_name,
                    'color': car.color,
                    'id': car.id,
                    'province': car.area.province,
                    'capacity': car.capacity,
                    'description': car.description,
                    'car_photo': car.car_photo.url if car.car_photo else None
                }
                vehicles_list.append(vehicle_dictionary)
    # Otherwise, filter by city
    elif city:
        area = Area.objects.filter(city=city)
        for a in area:
            vehicles = Vehicle.objects.filter(area=a)
            for car in vehicles:
                if car.is_available:
                    vehicle_dictionary = {
                        'name': car.car_name,
                        'color': car.color,
                        'id': car.id,
                        'province': car.area.province,
                        'capacity': car.capacity,
                        'description': car.description,
                        'car_photo': car.car_photo.url if car.car_photo else None
                    }
                    vehicles_list.append(vehicle_dictionary)

    # Store the list of vehicles in the session
    request.session['vehicles_list'] = vehicles_list
    return render(request, 'customer/search_results.html')

@login_required
def rent_vehicle(request):
    id = request.POST['id']
    vehicle = Vehicle.objects.get(id = id)
    cost_per_day = int(vehicle.capacity)*13
    days = int(request.POST.get('days', 1))
    rent = cost_per_day * days
    # Prepare PayPal form
    paypal_dict = {
        "business": "YOUR_PAYPAL_EMAIL",
        "amount": rent,
        "item_name": vehicle.car_name,
        "invoice": str(vehicle.id),
        "currency_code": "CAD",
        "return_url": "http://127.0.0.1:8000/customer_portal/confirmed/",
    }
    form = PayPalPaymentsForm(initial=paypal_dict)

    # return render(request, 'rent.html', {'form': form, 'vehicle': vehicle, 'cost_per_day': cost_per_day})
    return render(request, 'customer/confirmation.html', {'vehicle':vehicle, 'cost_per_day':cost_per_day})

@login_required
def confirm(request):
    vehicle_id = request.GET.get('id')
    days = request.GET.get('days')  # Now we get 'days' from the query parameters

    if not vehicle_id or not days:
        return HttpResponse("Vehicle ID or number of days is missing.", status=400)

    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
    except Vehicle.DoesNotExist:
        return HttpResponse("Vehicle not found.", status=404)

    username = request.user
    user = User.objects.get(username=username)

    if not days:
        return HttpResponse("Number of days not found.", status=400)

    if vehicle.is_available:
        # Process the rental details
        car_dealer = vehicle.dealer
        rent = (int(vehicle.capacity)) * 13 * int(days)

        # Update car dealer's wallet
        car_dealer.wallet += rent
        car_dealer.save()

        # Create or get the order
        try:
            order = Order(vehicle=vehicle, car_dealer=car_dealer, user=user, rent=rent, days=days)
            order.save()
        except:
            order = Order.objects.get(vehicle=vehicle, car_dealer=car_dealer, user=user, rent=rent, days=days)

        # Mark the vehicle as unavailable
        vehicle.is_available = False
        vehicle.save()

        # Return the confirmation page with the order details
        return render(request, 'customer/confirmed.html', {'order': order})
    else:
        # If the vehicle is not available, return the order_failed page
        return render(request, 'customer/order_failed.html')



@login_required
def manage(request):
    order_list = []
    user = User.objects.get(username = request.user)
    try:
        orders = Order.objects.filter(user = user)
    except:
        orders = None
    if orders is not None:
        for o in orders:
            if o.is_complete == False:
                order_dictionary = {'id':o.id,'rent':o.rent, 'vehicle':o.vehicle, 'days':o.days, 'car_dealer':o.car_dealer}
                order_list.append(order_dictionary)
    return render(request, 'customer/manage.html', {'od':order_list})

@login_required
def update_order(request):
    order_id = request.POST['id']
    order = Order.objects.get(id = order_id)
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
    car_dealer = order.car_dealer
    car_dealer.wallet -= int(order.rent)
    car_dealer.save()
    order.delete()
    cost_per_day = int(vehicle.capacity)*13
    return render(request, 'customer/confirmation.html', {'vehicle':vehicle}, {'cost_per_day':cost_per_day})

@login_required
def delete_order(request):
    order_id = request.POST['id']
    order = Order.objects.get(id = order_id)
    car_dealer = order.car_dealer
    car_dealer.wallet -= int(order.rent)
    car_dealer.save()
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
    order.delete()
    return HttpResponseRedirect('/customer_portal/manage/')

