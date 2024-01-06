from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
# def members(request):
#     return render(request,'members/welcome.html',{'today':datetime.today()})

# @login_required(login_url ='/admin')
# def authorized(request):
#     return render(request,'members/authorized.html',{})

# insted of function we want to make a class for views for that we have to import
# create a new class and we can comment the function members and create a new class MembersView
from django.views.generic import TemplateView
class MembersView(TemplateView):
    template_name='members/welcome.html'  # this is for view
    extra_context= {'today':datetime.today()} # this is for extra Variable
    #  after add this new code we have to chnage in url also


# for class auth
from django.contrib.auth.mixins import LoginRequiredMixin
class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name= 'members/authorized.html'
    login_url= '/admin'

