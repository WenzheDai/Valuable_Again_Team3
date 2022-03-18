import time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from Valuable_Again_Team3 import settings
from apps.user.models import User, Address
from apps.goods.models import Items
from apps.order.models import Orders
from django.contrib.auth import authenticate, login, logout
from tools.mixin import LoginRequiredMixin
import re


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

        # return redirect(reverse('goods:index'))
        return render(request, 'user/login.html', {'registered':True, 'username': user.username})

class LoginView(View):
    """Login"""
    """
    username:Wenzhe   password:123
    username:Dai      password:forgotten
    """

    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        """check the login"""
        #receive the data
        username = request.POST.get('name')
        password = request.POST.get('password')

        #check the data
        if not all([username, password]):
            return render(request, 'user/login.html', {'errmsg':'Data missing'})

        #system checks the data
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                next_url = request.GET.get('next', reverse('goods:index'))
                return redirect(next_url)
        else:
            return render(request, 'user/login.html', {'errmsg':'The user name or password is incorrect'})

class LogoutView(View):
    """logout the status of login"""
    def get(self, request):
        #clear the information of session in user
        logout(request)
        return redirect(reverse('goods:index'))


class UserInfoView(LoginRequiredMixin, View):
    """User information"""
    def get(self, request):

        user = request.user


        #get the user profiles
        try:
            de_address = Address.objects.get(user=user, is_default=True)
        except Address.DoesNotExist:
            de_address = None


        return render(request, 'user/userProfile.html', {'de_address':de_address})

class AddressView(LoginRequiredMixin, View):
    """User address"""
    def get(self, request):

        user = request.user

        try:
            de_address = Address.objects.get(user=user, is_default=True)
        except Address.DoesNotExist:
            de_address = None

        return render(request, 'user/changeAddress.html', {'de_address':de_address})

    def post(self, request):
        # receive the data
        username = request.POST.get('name')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')

        # check the data
        if not all([username, address, postcode, phone]):
            return render(request, 'user/changeAddress.html', {'errmsg': 'Data Missing'})

        user = request.user

        try:
            de_address = Address.objects.get(user=user, is_default=True)
        except Address.DoesNotExist:
            de_address = None

        #if the user has default address, it should be cancelled default
        if de_address:
            Address.objects.update(is_default=False)

        # add the Address
        Address.objects.create(user=user, name=username, Address=address,
                               postcode=postcode, phone=phone, is_default=True)

        # return the reply
        return redirect(reverse('user:centerAddress'))


class UserItemsView(LoginRequiredMixin, View):
    """User's items"""
    def get(self, request):

        user = request.user


        #get the user's items
        try:
            itemList = Items.objects.filter(user=user).values('id', 'itemsName', 'price', 'create_time', 'status',
                                                              'describe', 'itemCategory', 'itempicture__itemPicture').order_by('-create_time')
        except Address.DoesNotExist:
            itemList = None

        #get the record of history

        return render(request, 'user/myItems.html', {'itemList':itemList})


class UserOrdersView(LoginRequiredMixin, View):
    """the orders"""
    def get(self, request):

        user = request.user


        sellOrderList = Orders.objects.filter(seller=user).values('id', 'tradGood__itemsName', 'tradGood__itempicture__itemPicture',
                                                                  'create_time', 'tradGood__price', 'status', 'tradGood_id',
                                                                  'buyer__Profile_picture', 'buyer__username').order_by('-create_time')
        buyOrderList = Orders.objects.filter(buyer=user).values('id', 'tradGood__itemsName', 'tradGood__itempicture__itemPicture',
                                                                  'create_time', 'tradGood__price', 'status', 'tradGood_id',
                                                                'seller__Profile_picture', 'seller__username').order_by('-create_time')

        return render(request, 'user/orders.html', {'sellOrderList': sellOrderList, 'buyOrderList': buyOrderList})



class UpLoadAvatar(LoginRequiredMixin,View):
    """# upload an avatar to media/avatars/ and return the file name"""
    def post(self, request):
        # get image file object
        img = request.FILES.get("file", None)

        # get user id
        userId = request.user.id

        # generate a unique file name: avatar-(userID)-(timestamp).(fileType)
        fileEnd = img.name.split('.')[-1]
        fileName = "avatar-" + str(userId) + '-' + str(int(time.time())) + "." + fileEnd

        save_path = '{}/avatars/{}'.format(settings.MEDIA_ROOT, fileName)
        success = False
        with open(save_path, 'wb') as f:
            for content in img.chunks():
                f.write(content)
                success = True

        if success:
            return JsonResponse({'success': True, 'name': fileName})
        else:
            return JsonResponse({'success': False, 'errmsg': "Image upload failed."})

class SaveAvatar(LoginRequiredMixin,View):
    def post(self, request):

        #check the user
        user = request.user

        #get the avatar name
        img = request.POST.get("avatarName")

        #update the database
        User.objects.update(Profile_picture=img)

        #check the update
        if User.objects.get(Profile_picture=img):
            return JsonResponse({'success':True, 'name':img})
        else:
            return JsonResponse({'success': False, 'errmsg': "Image upload failed."})




















