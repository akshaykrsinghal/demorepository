from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from ..models.user import user_login
from django.contrib.auth.hashers import check_password
from ..models import admin_login
class Login(View):
    return_url=None
        
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request, 'login.html')
    def post(self,request):
        print(request.POST)
        if ('admin_login' in request.POST):
            print("admin")
            email = request.POST.get('email')
            password = request.POST.get('pwd')
            admin = admin_login.get_admin_by_email(email)
            
            #print("user",user)
            error_message = None
            if admin:
                flag = password==admin.password
                if flag:
                    request.session['customer'] = admin.id
                    request.session['email'] =admin.email

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                    return redirect('admin')
                else:
                    error_message = 'Email or Password1 invalid !!'
            else:
                error_message = 'Email or Password2 invalid !!'


            return render(request, 'login.html', {'error': error_message})
        else:
            email = request.POST.get('email')
            password = request.POST.get('pwd')
            user = user_login.get_user_by_email(email)
            #print("user",user)
            error_message = None
            if user:
                flag = password==user.password
                if flag:
                    request.session['customer'] = user.id
                    request.session['rollno'] =user.Rollno

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                    return redirect('student')
                else:
                    error_message = 'Email or Password invalid1 !!'
            else:
                error_message = 'Email or Password invalid2 !!'


            return render(request, 'login.html', {'error': error_message})
        


        
def logout(request):
    request.session.clear()
    return redirect('login')