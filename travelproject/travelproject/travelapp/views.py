from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Owners
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Owners.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
# def add(request):
#     num1=int(request.GET['num1'])
#     num2=int(request.GET['num2'])
#     res=num1+num2
#     return render(request,"about.html",{'result':res})