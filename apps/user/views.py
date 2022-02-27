from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from apps.user.models import User
import re

# Create your views here.
def login(request):
    return render(request, 'user/login.html')
#
# def register(request):
#     return render(request, 'user/register.html')

# Dai:
# Use the Class View to distinguish the get request and post request
# html_name:name email password
class RegisterView(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        """handle the register"""

        #receive the data
        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username:
            return render(request, 'user/register.html', {'errmsg': '1'})
        if not password:
            return render(request, 'user/register.html', {'errmsg': '2'})
        if not email:
            return render(request, 'user/register.html', {'errmsg': '3'})

        # phone = request.POST.get('phone')

        #check the wholeness of data
        if not all([username, password, email]):
            return render(request, 'user/register.html', {'errmsg': 'Data missing'})

        #check the email
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'user/register.html', {'errmsg': 'Email format is not correctly'})


        #check the username whether to repeat
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            #the username is not in database
            user = None

        if user:
            # the username in the database
            return render(request, 'user/register.html', {'errmsg':'User name already exists'})

        #register in database
        user = User.objects.create_user(username, email, password)

        return redirect(reverse('goods:index'))


















