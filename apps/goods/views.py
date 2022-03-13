from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from tools.mixin import LoginRequiredMixin
from apps.goods.models import Items, ItemPicture
from apps.order.models import Orders
from Valuable_Again_Team3 import settings
import time


class Index(View):
    def get(self, request):
        item = Items.objects.all().values('itemsName', 'price','id', 'itempicture__itemPicture')
        return render(request, 'goods/index.html', {'items':item})


class IndexCategory(View):
    def get(self, request, category):
        item = Items.objects.filter(itemCategory=category).values('itemsName', 'price', 'id', 'itempicture__itemPicture')
        return render(request, 'goods/index.html', {'items':item})

class ItemDetial(View):
    def get(self, request, item_id):
        item = Items.objects.all().values('itemsName', 'itemCategory', 'price', 'status','id', 'describe','itempicture__itemPicture',
                                          'user__username', 'user__Profile_picture', 'user__address__Address',
                                          'user__email')
        detail = item.get(id=item_id)

        return render(request, 'goods/detail.html', {'item':detail})

    def post(self, request):
        """set the submit the order"""
        #check the user
        user = request.user
        #
        item_id = request.POST.get("id")

        item = Items.objects.get(id(item_id))
        if item is None:
            return JsonResponse({'success':False, 'errmsg':'No item'})

        try:
            good = item.objects.update(status="Booked")
            Orders.objects.create(seller=user, buyer=Items.user, tradGood=good)
        except:
            return JsonResponse({'success':False, 'errmsg':'Database error'})


        return JsonResponse({'success':True})

class AddItem(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'goods/addItem.html')

    def post(self, request):
        #receive the data
        user = request.user
        goodsName = request.POST.get('goodsName')
        price = request.POST.get('goodsPrice')
        category = request.POST.get('goodsCategory')
        describe = request.POST.get('goodsDesc')
        image = request.POST.get('goodsImage')

        #check the data
        if not all([goodsName, price, category, describe, image]):
            return JsonResponse({'success': False, 'errmsg': 'Data Missing'})

        #add the data to database
        item = Items.objects.create(user=user,itemsName=goodsName, price=price, describe=describe, itemCategory=category)
        ItemPicture.objects.create(item=item, itemPicture=image)


        return JsonResponse({'success':True})


class UpLoadGoodsImage(LoginRequiredMixin,View):
    def post(self, request):
        # get image file object
        img = request.FILES.get("file", None)

        # get user id
        userId = request.user.id

        # generate a unique file name: avatar-(userID)-(timestamp).(fileType)
        fileEnd = img.name.split('.')[-1]
        fileName = "image-" + str(userId) + '-' + str(int(time.time())) + "." + fileEnd

        save_path = '{}/goodsImages/{}'.format(settings.MEDIA_ROOT, fileName)
        success = False
        with open(save_path, 'wb') as f:
            for content in img.chunks():
                f.write(content)
                success = True

        if success:
            return JsonResponse({'success': True, 'name': fileName})
        else:
            return JsonResponse({'success': False, 'errmsg': "Image upload failed."})

