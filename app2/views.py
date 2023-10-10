from django.shortcuts import render
from django.shortcuts import redirect
from .models import registerdetails
# Create your views here.

def registerpage(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        registerdetails(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            dateofbirth=request.POST.get('dob'),
            password=request.POST.get('password'),
        ).save()
        return render(request,'register.html')
