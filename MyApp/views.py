# from email.mime import message
# from pyexpat import model
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# from .models import Car, Order, Contact
from .models import Contact

def index(request):
	return render(request,'index.html')

def about(request):
    return render(request,'about.html ')

def signout(request):
        logout(request)
        # messages.success(request,"Successfully logged out!")
        return redirect('home')

    # return HttpResponse('signout')


def contact(request):
    form_submitted = False  # Flag to track if form is submitted

    if request.method == "POST":
        contactname = request.POST.get('contactname', '')
        contactemail = request.POST.get('contactemail', '')
        contactnumber = request.POST.get('contactnumber', '')
        contactmsg = request.POST.get('contactmsg', '')

        # Create and save the contact entry
        contact = Contact(name=contactname, email=contactemail, phone_number=contactnumber, message=contactmsg)
        contact.save()

        form_submitted = True  # Set flag to true after successful submission

    return render(request, 'contact.html', {'form_submitted': form_submitted})
