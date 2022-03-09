from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from tools.mixin import LoginRequiredMixin
from apps.goods.models import Items

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
