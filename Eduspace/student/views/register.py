from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from ..models.user import user_login
from django.contrib.auth.hashers import make_password



class Register(View):

    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        Rollno=request.POST.get('Rollno')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        c_pwd=request.POST.get('c_pwd')

        error_message=None
        user=user_login(email=email,password=pwd,Firstname=f_name,Lastname=l_name,Rollno=Rollno)
        if user.password!=c_pwd:
            print(user.password)
            print(c_pwd)
            error_message='confirm password shoud equal to password'
        error_message=self.validateUser(user,c_pwd)
        if not error_message:
            
            user.password = make_password(user.password)
            user.register()
            return redirect('homepage')
        else:

            return render(request, 'register.html', {'error': error_message})
    def validateUser(self, user,c_pwd):
        error_message = None;
        if (not user.Firstname):
            error_message = "First Name Required !!"
        elif len(user.Firstname) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not user.Lastname:
            error_message = 'Last Name Required'
        elif len(user.Lastname) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not user.Rollno:
            error_message = 'Roll Number required'
        elif len(user.Rollno) < 10:
            error_message = 'Roll Number must be 10 char Long'
        elif len(user.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(user.email) < 5:
            error_message = 'Email must be 5 char long'
        
        elif user.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
