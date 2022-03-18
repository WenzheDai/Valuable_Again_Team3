from django.shortcuts import render, redirect, reverse
from apps.goods.models import Items, ItemPicture
from apps.user.models import User
from apps.order.models import Orders
from django.views import View
from django.http import HttpResponse, JsonResponse

class FinishOrder(View):
    def post(self, request):
        #get the user
        user = request.user

        #get the order_id
        orderId = request.POST.get('order_id')

        #find zhe item and order
        try:
            order = Orders.objects.get(id=orderId)
            item = Items.objects.get(id=order.tradGood.id)
        except Orders.DoesNotExist:
            return JsonResponse({'success':False, 'errmsg':'Do not find the order'})

        #update the database
        order.status = 'Finished'
        order.save()
        item.status = 'Sold'
        item.save()

        #update the notices
        buyer = order.buyer
        buyer.notices = 'Your order status has been updated. Please go to the order page to check.'
        buyer.save()

        return JsonResponse({'success':True})


class CancelOrder(View):
    def post(self, request):
        #get the user
        user = request.user

        #get the order_id
        orderId = request.POST.get('order_id')

        #find zhe item and order
        try:
            order = Orders.objects.get(id=orderId)
            item = Items.objects.get(id=order.tradGood.id)
        except Orders.DoesNotExist:
            return JsonResponse({'success':False, 'errmsg':'Do not find the order'})

        #update the database
        order.status = 'Cancelled'
        order.save()
        item.status = 'On sale'
        item.save()

        #update the database
        seller = order.seller
        seller.notices = 'Your order status has been updated. Please go to the order page to check.'
        seller.save()

        return JsonResponse({'success':True})

















