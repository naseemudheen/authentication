from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View

# from django.auth.models import User
from .forms import UserAuthenticationForm,UserRegistrationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import MyUser

# Create your views here.

class LoginPageView(View):
    form_class = UserAuthenticationForm
    template_name = 'user/login.html'

    def get(self,request):
        # form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':self.form_class})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        # <process form cleaned data>
        user = authenticate(username=username, password=password)
        if user is not None:
            # return render(request,'user/index.html')
                login(request, user)
                return redirect("/")
        else:
            messages.info(request,f'Invalid Username/Password')
            return redirect('user:login')



class LogoutPageView(View):
    template_name = 'user/logout.html'

    def get(self,request):
        logout(request)
        return redirect('/')


class HomePageView(LoginRequiredMixin,View):
    form_class = UserAuthenticationForm
    template_name = 'user/index.html'
    

    def get(self,request):
        # form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':self.form_class})

class RegisterPageView(View):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'

    def get(self,request):
        user = request.user
        if user.is_authenticated: 
            logout(request)
        return render(request,self.template_name,{'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form =self.form_class(request.POST)

        username = request.POST['username']
        # print(form['password1'])
        # print(form['password2'])
        
        if (request.POST['password1']==request.POST['password2']):
            if (MyUser.objects.filter(username=username)):
                messages.warning(request,f'Username Already exists.')
            else:
                if form.is_valid():
                    form.save()
                    messages.success(request,f'Your Account has created you can Login now!')
                else:
                    messages.warning(request,form.errors)
        else:
            messages.warning(request,f'Password Mismatch')
        return redirect('user:register')
  
