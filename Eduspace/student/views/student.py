from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..models import *

def student(request):
    a=request.session['rollno']
    
   # image=user.objects.filter(rollno=a)
    image=user.objects.filter(rollno=a)
    data={'images':image}
    print(image)


    return render(request,'dashboard.html',data)
