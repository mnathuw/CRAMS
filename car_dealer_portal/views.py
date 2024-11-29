from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from car_dealer_portal.models import *
from customer_portal.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Vehicle, Area, CarDealer

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'car_dealer/login.html')
    else:
        return render(request, 'car_dealer/home_page.html')

def login(request):
    return render(request, 'car_dealer/login.html')


def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'car_dealer/home_page.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            car_dealer = CarDealer.objects.get(car_dealer = user)
        except:
            car_dealer = None
        if car_dealer is not None:
            auth.login(request, user)
            return render(request, 'car_dealer/home_page.html')
        else:
            return render(request, 'car_dealer/login_failed.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'car_dealer/login.html')

def register(request):
    return render(request, 'car_dealer/register.html')

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
        return render(request, 'car_dealer/registration_error.html')
    try:
        area = Area.objects.get(city = city, province = province)
    except:
        area = None
    if area is not None:
        car_dealer = CarDealer(car_dealer = user, mobile = mobile, area=area)
    else:
        area = Area(city = city, province = province)
        area.save()
        area = Area.objects.get(city = city, province = province)
        car_dealer = CarDealer(car_dealer = user, mobile = mobile, area=area)
    car_dealer.save()
    return render(request, 'car_dealer/registered.html')

@login_required
def add_vehicle(request):
    year_choice = Vehicle.year_choice
    province_choice = Vehicle.province_choice
    door_choices = Vehicle.door_choices
    features_choices = Vehicle.features_choices
    username = request.user
    user = User.objects.get(username=username)
    car_dealer = CarDealer.objects.get(car_dealer=user)  # Ensure you're using 'car_dealer'

    if request.method == 'POST':
        # Get form data
        car_name = request.POST['car_name']
        color = request.POST['color']
        city = request.POST['city'].lower()  # Convert city to lowercase
        province = request.POST.get('province')  # Selected province code
        description = request.POST['description']
        capacity = request.POST.get('capacity', None)  # Defaults to None if 'capacity' is missing
        model = request.POST['model']
        year = request.POST['year']  # Selected year
        condition = request.POST['condition']
        price = request.POST['price']
        body_style = request.POST['body_style']
        engine = request.POST['engine']
        transmission = request.POST['transmission']
        interior = request.POST['interior']
        milage = request.POST['milage']
        doors = request.POST['doors']  # Selected door count
        vin_no = request.POST['vin_no']
        fuel_type = request.POST['fuel_type']
        features = request.POST.getlist('features')  # Handle multi-select field
        car_photo = request.FILES['car_photo']  # Handle file upload

        # Get or create the Area instance based on city and province
        area, created = Area.objects.get_or_create(province=province, city=city)
        print(f"Area: {area}, Created: {created}")  # Debugging output

        # Create the vehicle instance
        car = Vehicle(
            car_name=car_name,
            color=color,
            description=description,
            capacity=capacity,
            model=model,
            year=year,  # Use the selected year
            condition=condition,
            price=price,
            body_style=body_style,
            engine=engine,
            transmission=transmission,
            interior=interior,
            milage=milage,
            doors=doors,  # Use the selected door count
            vin_no=vin_no,
            fuel_type=fuel_type,
            features=features,  # List of selected features
            car_photo=car_photo,
            area=area,  # Assign the area object here
            dealer=car_dealer,  # Assign the dealer object here (fixed the variable name)
        )

        # Save the vehicle to the database
        car.save()

        return render(request, 'car_dealer/vehicle_added.html', {'car': car})

    else:
        return render(request, 'car_dealer/vehicle_added.html', {
            'year_choice': year_choice,
            'province_choice': province_choice,
            'door_choices': door_choices,
            'features_choices': features_choices,
        })

@login_required
def manage_vehicles(request):
    # Ensure that the current user is associated with a CarDealer
    try:
        car_dealer = CarDealer.objects.get(car_dealer=request.user)
    except CarDealer.DoesNotExist:
        return HttpResponseForbidden("You are not a car dealer.")

    # Retrieve all vehicles related to this car dealer
    vehicles = Vehicle.objects.filter(dealer=car_dealer)

    # Render the 'manage_vehicles' page with the list of vehicles
    return render(request, 'car_dealer/manage.html', {'vehicle_list': vehicles})

@login_required
def order_list(request):
    username = request.user
    user = User.objects.get(username = username)
    car_dealer = CarDealer.objects.get(car_dealer = user)
    orders = Order.objects.filter(car_dealer = car_dealer)
    order_list = []
    for o in orders:
        if o.is_complete == False:
            order_list.append(o)
    return render(request, 'car_dealer/order_list.html', {'order_list':order_list})

@login_required
def complete(request):
    order_id = request.POST['id']
    order = Order.objects.get(id = order_id)
    vehicle = order.vehicle
    order.is_complete = True
    order.save()
    vehicle.is_available = True
    vehicle.save()
    return HttpResponseRedirect('/car_dealer_portal/order_list/')


@login_required
def history(request):
    user = User.objects.get(username = request.user)
    car_dealer = CarDealer.objects.get(car_dealer = user)
    orders = Order.objects.filter(car_dealer = car_dealer)
    order_list = []
    for o in orders:
        order_list.append(o)
    return render(request, 'car_dealer/history.html', {'wallet':car_dealer.wallet, 'order_list':order_list})

from django.contrib import messages

@login_required
def delete(request):
    veh_id = request.POST['id']

    try:
        vehicle = Vehicle.objects.get(id=veh_id)

        # Check if the vehicle is referenced in any orders
        if vehicle.order_set.exists():
            messages.error(request, "This vehicle is referenced in one or more orders and cannot be deleted.")
            return HttpResponseRedirect('/car_dealer_portal/manage_vehicles/')

        # If the vehicle is not referenced, delete it
        vehicle.delete()
        messages.success(request, "Vehicle deleted successfully.")

    except Vehicle.DoesNotExist:
        messages.error(request, "Vehicle not found.")

    return HttpResponseRedirect('/car_dealer_portal/manage_vehicles/')
