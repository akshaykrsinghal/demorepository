from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..models import admindata
from ..models import admin_login
def admin(request):
    a=request.session['email']
    
    image=admindata.objects.filter(emailid="ad")
    print(image)
    return render(request,'admin_dashboard.html')
