from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def userlogin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bloghome/myDiary')
        else:
            messages.info(request,'Invalid credinteals')
            return redirect('/')

    return render(request,'registration/login.html')

    
def usersignup(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        username = request.POST.get('username')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        user = User()
        user.first_name=fname
        user.last_name=lname
        user.username=username
        user.email=email
        user.phone=phone
        user.password=cpassword
        user.save()

        user.set_password(password)
        user.save()
        messages.success(request,'Register Sucessfully...')
        return redirect('/')
        
    else:
        return render(request,'signup.html')

def userlogout(request):
    logout(request)
    return redirect('/')
    return HttpResponse("Return Logout functions")
