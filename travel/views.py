from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about2.html")
def category(request):
    return render(request,"category.html")
def contact(request):
    return render(request,"contact.html")