from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View

from user.models import feed
from django.core import serializers
# from django.auth.models import User
from .forms import AccountAuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class LoginPageView(View):
    form_class = AccountAuthenticationForm
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


class HomePageView(LoginRequiredMixin,View):
    form_class = AccountAuthenticationForm
    template_name = 'user/index.html'
    

    def get(self,request):
        # form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':self.form_class})

def getdata(request):
	results=feed.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)