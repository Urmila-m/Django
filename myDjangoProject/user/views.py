from django.shortcuts import render, redirect
from user.forms import UserRegistration


def register(request):
    if request.method=='POST':
        user = UserRegistration(request.POST)
        if user.is_valid():
            user.save()
            return redirect("../login")
        else:
            return render(request, "user/register.html", {'user': user})

    else:
        user = UserRegistration()
        return render(request, "user/register.html", {'user': user})

