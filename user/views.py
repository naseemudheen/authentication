from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View

# from django.auth.models import User
from .forms import UserAuthenticationForm,UserRegistrationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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
            return HttpResponse("<p>crendentials authentication  failed</p>")

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
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            form.save()
            messages.success(request,f'Your Account has created you can Login now!')
            return redirect('user:register')
        else:
            print(form.errors)
            # messages.warning(request,form.errors)
            return redirect('user:register')
