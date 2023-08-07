from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def registeredUser(request):
    if(request.method == 'POST'):
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        firstname = request.POST.get("firstname")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        print(username,email,firstname,lastname,password,confirmpassword)
        if password == confirmpassword:
            user =User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
                password=password

            )
            user.save()
            return redirect('crud:home')
        else:
            print("password validation failed")

    # 
    return render(request, "user/register.html")

def loginUser(request):
    print(request.user)
    return render(request, "users/login.html")

def logoutUser(request):
    print(request.user)
    return render("crud;home")
