from django.test import TestCase
from django.urls import reverse

from apps.goods.models import Items
from apps.user.models import User
from django.test import Client


# Create your tests here.
class UserTestCase(TestCase):
    def test_user(self):
        self.username = 'test'
        self.password = 'password'
        self.email = 'test@gmail.com'

        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        self.user.save()

        self.client = Client(SERVER_NAME='localhost')

        # login test
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('')
        self.assertContains(response, 'Logout')

        # profile test
        response = self.client.get('/user/')
        self.assertContains(response, self.username)

        # edit profile test
        test_profile = {
            'name': 'test',
            'address': 'test_address',
            'postcode': 'G11 6QJ',
            'phone': '12345678909'
        }
        response = self.client.post(reverse('user:centerAddress'), data=test_profile, follow=True)
        self.assertContains(response, f'Phone: {test_profile["phone"]}')

        # logout test
        self.client.logout()
        response = self.client.get('')
        self.assertContains(response, 'Sign in')


class GoodsTestCase(TestCase):
    def test_user_goods(self):
        # create the test user
        self.username = 'test'
        self.password = 'password'
        self.email = 'test@gmail.com'

        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        self.user.save()

        self.client = Client(SERVER_NAME='localhost')
        self.client.login(username=self.username, password=self.password)

        # publish item test
        test_item = {
            'goodsName': 'test Goods',
            'goodsPrice': '5.0',
            'goodsCategory': 'test category',
            'goodsDesc': 'test description',
            'goodsImage': 'test img'
        }
        self.client.post(reverse('goods:addItem'), data=test_item, follow=True)
        response = self.client.get(reverse('user:myItems'))
        self.assertContains(response, test_item['goodsName'])
        self.assertContains(response, 'On sale')

        # search test
        response = self.client.get('/search?q=test')
        self.assertContains(response, '<h5 class="card-title">test')
        response = self.client.get('/search?q=test2')
        self.assertNotContains(response, '<h5 class="card-title">test2')

        # create a new client account to test book function
        user2 = User.objects.create_user(username='test2', password='test2')
        user2.save()
        self.client.login(username='test2', password='test2')
        self.client.post('/detail/bookGoods', {'id': '1'})
        response = self.client.get('/user/orders')
        self.assertContains(response, test_item['goodsName'])
