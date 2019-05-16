from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from forms import GetFeedback
from myWebsiteApp.models import MyModel
from user.forms import UserRegistration


def Home(request):
    return render(request, 'myWebsiteApp/userInput.html')

def about(request):
    return render(request, 'myWebsiteApp/about.html')

def chinese(request):
    return render(request, 'myWebsiteApp/chinese.html')

def indian(request):
    return render(request, 'myWebsiteApp/indian.html')

@login_required
def feedback(request):
    if request.method== 'POST':
        myModel= MyModel()
        getFeedbackObject = GetFeedback(request.POST)
        if getFeedbackObject.is_valid():
            myModel.name = getFeedbackObject.cleaned_data['name']
            myModel.item = getFeedbackObject.cleaned_data['item']
            myModel.address = getFeedbackObject.cleaned_data['address']
            myModel.email = getFeedbackObject.cleaned_data['email']
            myModel.gender = getFeedbackObject.cleaned_data['gender']
            myModel.password = getFeedbackObject.cleaned_data['password']
            myModel.quantity = getFeedbackObject.cleaned_data['quantity']
            myModel.suggestion = getFeedbackObject.cleaned_data['suggestion']

            myModel.save()
            messages.success(request, f'Form registered successfully with name {myModel.name}!')
            return redirect('../myWebsite')

        else:
            error = getFeedbackObject.errors.as_data()
            return HttpResponse(error)

    else:
        return render(request, 'myWebsiteApp/feedback.html')

def newari(request):
    return render(request, 'myWebsiteApp/newari.html')

def myWebsite(request):
    return render(request, 'myWebsiteApp/myWebsite.html')

def myNextAttempt(request):
    return HttpResponse("this is the second attempt to understand adding urls and views")