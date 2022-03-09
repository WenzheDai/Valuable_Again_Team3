from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from tools.mixin import LoginRequiredMixin
from apps.goods.models import Items
from Valuable_Again_Team3 import settings
import time

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'goods/index.html')

class AddItem(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'goods/addItem.html')

    def post(self, request):
        #receive the data
        goodsName = request.Post.get('goodsName')
        price = request.Post.get('goodsPrice')
        describe = request.Post.get('goodsDesc')

        #check the data
        if all([goodsName, price, describe]):
            return JsonResponse({'success': False, 'errmsg': 'Data Missing'})

            # return render(request, 'goods/addItem.html', {'errmsg': 'Data Missing'})

        #add the data to database
        Items.objects.create(itemsName=goodsName, price=price, describe=describe)

        return JsonResponse({'success':True})

        # return redirect(reverse('goods:index'))


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