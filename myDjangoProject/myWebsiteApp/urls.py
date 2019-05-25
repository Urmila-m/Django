import views
from django.urls import path
from myWebsiteApp import views

urlpatterns = [
    path('', views.Home, name="myWebsiteApp_home"), #path is empty as we want it to be loaded as default home page i.e localhost:8000
    path('myWebsite/', views.myWebsite, name="myWebsiteApp_myWebsite"),
    path('feedback/', views.feedback, name="myWebsiteApp_feedback"),
    path('indian/', views.indian, name="myWebsiteApp_indian"),
    path('newari/', views.newari, name="myWebsiteApp_newari"),
    path('about/', views.about, name="myWebsiteApp_about"),
    path('chinese/', views.chinese, name="myWebsiteApp_chinese"),
    path('myFilledForms/', views.getMyFilledForms, name="myFilledForms"),
    path('uploadImageAndFile/', views.uploadImageAndFile, name="uploadImageAndFile"),
    path('test/', views.myNextAttempt, name="jpt")
]

