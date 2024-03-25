from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import ContactMessage
from .models import phpgallery,LinuxGallery,SaseGallery,StatisticsGallery,DaaGallery

from authapp.models import phpgallery

import re
# Create your views here.
def Home(request):
    return render(request,"index.html")
    
def faq(request):
    return render(request,"faq.html")

def subjects(request):
    return render(request,"products.html")

def about(request):
    return render(request,"about.html")

def php(request):
    posts=phpgallery.objects.all()
    context={"posts":posts}
    return render(request,"php.html",context)

def linux(request):
    posts=LinuxGallery.objects.all()
    context={"posts":posts}
    return render(request,"linux.html",context)

def sase(request):
    posts=SaseGallery.objects.all()
    context={"posts":posts}
    return render(request,"sase.html",context)

def statistics(request):
    posts=StatisticsGallery.objects.all()
    context={"posts":posts}
    return render(request,"statistics.html",context)

def daa(request):
    posts=DaaGallery.objects.all()
    context={"posts":posts}
    return render(request,"daa.html",context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact message to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Add a success message
        messages.success(request, 'Your message has been submitted successfully!')

        # Redirect back to the contact page
        return redirect('contact')

    return render(request, 'contact.html')
   

def custom_logout(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('signin')

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, "Password is not Matching")
            return redirect('/signup')
        
        # Password strength validation
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$", pass1):
            messages.error(request, "Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long")
            return redirect('/signup')

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is Taken")
                return redirect('/signup')

        except User.DoesNotExist:
            # Create the user with the email as username
            myuser = User.objects.create_user(username=email, email=email, password=pass1)
            myuser.save()
            messages.success(request, "User is Created. Please Login")
            return redirect('/signin')

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=email, password=pass1)
        if myuser is not None:
            login(request, myuser)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/signin')
    return render(request, "signin.html")