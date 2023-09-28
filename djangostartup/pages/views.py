from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args, **kwargs):
    return render(request, "home.html",{})# string of HTML Code

def contact_view(request, *args, **kwargs):
    return render (request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context ={
        "my_text":"This is about us",
        "my_number":123,
        "my_list":[123,3434,123123,"Abc"]
    }
    
    return render(request, "about.html", my_context)

  