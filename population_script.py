import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Valuable_Again_Team3.settings')

import django
django.setup()

from apps.user.models import User, Address
from apps.goods.models import Items, ItemPicture


def populate():

    # address
    aparto_address = [{'name': 'Wenzhe Dai',
                       'Address': 'Aparto Glasgow West End, 145 Kelvinhaugh St, Glasgow',
                       'postcode': 'G3 8PX',
                       'phone': '31345413854',
                       'is_default': True}]

    village_address = [{'name': 'Chaoran Ma',
                        'Address': 'West Village, 1 Beith St, Glasgow',
                        'postcode': 'G11 6PS',
                        'phone': '51564532123',
                        'is_default': True}]

    view_address = [{'name': 'Xinrong He',
                     'Address': 'West View, 2 Beith St, Glasgow',
                     'postcode': 'G11 6EH',
                     'phone': '4532414214',
                     'is_default': True}]

    vita_address = [{'name': 'Tianyuan Wang',
                     'Address': 'Vita, 21 Beith St, Glasgow',
                     'postcode': 'G11 6BZ',
                     'phone': '51354561531',
                     'is_default': True}]

    dm_address = [{'name': 'Shunyu yang',
                   'Address': 'Dunaskin Mill, 5 Dunaskin St, Glasgow',
                   'postcode': 'G11 6QJ',
                   'phone': '15645611352',
                   'is_default': True}]


    # item, itemPicture
    # itemPicture = [{'itemPicture': }]
    # item
    tableware_items = [{'itemName': 'Royal Albert Cups',
                        'price': 5.00,
                        'describe': 'Two A celebration of the Old Country Roses Gardens well used 1 slightly damaged\
                         on the base',
                        'itemCategory': 'Tableware',
                        'image': 'tableware_items.png'},
                       {'itemName': ' modern simple manager desk supervisor desk  ',
                        'price': 310.00,
                        'describe': 'a tableware suite used for a year, new 80%, with the original goods picture',
                        'itemCategory': 'Tableware',
                        'image': 'table.png'}
                       ]

    food_items = [{'itemName': 'KitchenAid Food Processor',
                   'price': 45.00,
                   'describe': 'Grab this fantastic food processor, which has loyally been helping us create\
                       delicious food in our family for the past 10 years. Works perfectly and comes with all\
                        attachments, as per the photos. There is a small crack in the main bowl but it still\
                         works fine. Collection only please.',
                   'itemCategory': 'Food',
                   'image': 'food_items.png'},
                  {'itemName': 'Your Super Moon Balance Superfood Mix',
                   'price': 23.99,
                   'describe': 'IMPROVE HORMONE HEALTH: Naturally supports mood, quality of sleep, ability to focus,\
                    skin & hair health, weight and cognitive function HEALTHY HORMONES, HAPPY YOU: Superfoods powder\
                     to balance weight gain, hot flashes, bloating, stress, depression, indigestion, acne, muscle and\
                      joint pain POWERFUL ORGANIC INGREDIENTS: Naturally dried ingredients to preserve all\
                       micronutrients; tested by 3rd party labs to ensure high quality standards NO SWEETENERS OR\
                       FILLERS EVER: No stevia, thickeners or artificial flavoring – Made with 6 nutrient-rich\
                        recovering superfoods, nothing more EASY TO USE: Add one teaspoon to water, smoothies,\
                         breakfast or snacks. For best results, use daily. Tart lemonade taste',
                   'itemCategory': 'Food',
                   'image': 'superfood_mix.jpg'}
                  ]

    device_items = [{'itemName': 'XBOX ONE S console with HDMI cable and POWER cable',
                     'price': 130.00,
                     'describe': 'Normal good working order Xbox one s , hdmi and power cable , collection only\
                       tho sorry , my cars broken down and needs replacing hence the sale',
                     'itemCategory': 'Device',
                     'image': 'device_items.png'},
                    {'itemName': 'ZyXEL 5G NR 2 Gbps Mobile WiFi',
                     'price': 352.52,
                     'describe': 'NR2101 5G, Empower the Future 5G is here! Explore the speed of 5G network\
                      technology and rethink what’s possible in the future. We’ve created the Zyxel 5G NR Mobile WiFi\
                       (NR2101) to bring you into the 5G world. Faster. Stronger. Better. Take control of it.\
                        Cool things happen when you just act on it!',
                     'itemCategory': 'Device',
                     'image': 'WIFI.jpg'}
                    ]

    furniture_items = [{'itemName': 'Gorgeous Garden Furniture',
                        'price': 150.00,
                        'describe': 'Very high quality outdoor furniture Tall bar stools and tall table set\
                       of 4 chairs and table .... 150 Set Several 1meter x 1meter dining tables at 50 Each\
                        Add a touch of class to your outdoor space',
                        'itemCategory': 'Furniture',
                        'image': 'furniture_items.png'},
                       {'itemName': 'Mercers Furniture Trade Corona 2 Door 2 Drawer Sideboard Light Fiesta Wax',
                        'price': 45.00,
                        'describe': 'Free Premium Shipping \nDimensions: Height - 76cm Width - 87cm\n Depth - 40cm\
                        Solid Pine Flat Pack for Easy Home Assembly',
                        'itemCategory': 'Furniture',
                        'image': 'sideboard.jpg'}
                       ]

    clothing_items = [{'itemName': 'Huge Bundle of Childrens Clothes',
                       'price': 25.00,
                       'describe': 'Huge bundle of children\'s clothes age 4-6 includes t-shirts, jeans, pjs, shorts,\
                        casual shirts, jumpers, onesie, hoodies etc. Fatface, Lego, Marvel. Star Wars, Adidas, Next \
                        etc. More items than that shown in the photos which shows a selection Loads of items all in\
                         fantastic, clean condition, many items not even worn. From a smoke free home',
                       'itemCategory': 'Clothing',
                       'image': 'clothing_items.png'},
                      {'itemName': 'Winthome Lengthen Oversized Blanket',
                       'price': 20.50,
                       'describe': 'SOFT SHERPA lining to make you feel warm and pampered Enables you to move freely\
                        and rest easily in any position, never too tight or too short Machine Wash MACHINE WASH\
                         30°c to easily remove stains DO NOT MISS the opportunity to enjoy The Fluffle feeling\
                          with your family and pets! Love it or return within 90 days for your money back without\
                           question.',
                       'itemCategory': 'Clothing',
                       'image': 'blanket.jpg'}
                      ]

    users = {'Wenzhe Dai': {'address': aparto_address, 'items': tableware_items, 'email': '2628148d@student.gla.ac.uk',
                            'Profile_picture': 'Wenzhe Dai.jpg',
                        'password': 'pbkdf2_sha256$120000$WFTo7No5Rzb0$2wbqRcQci49Vt4XDoq4HbHB9UAx2LiDpIM3+eIqhj4I='},
        'Chaoran Ma': {'address': village_address, 'items': food_items, 'email': '2639687m@student.gla.ac.uk',
                       'Profile_picture': 'Chaoran Ma.jpg',
                       'password': 'pbkdf2_sha256$120000$WFTo7No5Rzb0$2wbqRcQci49Vt4XDoq4HbHB9UAx2LiDpIM3+eIqhj4I='},
        'Xinrong He': {'address': view_address, 'items': device_items, 'email': '2515527h@student.gla.ac.uk',
                       'Profile_picture': 'Xinrong He.jpg',
                       'password': 'pbkdf2_sha256$120000$WFTo7No5Rzb0$2wbqRcQci49Vt4XDoq4HbHB9UAx2LiDpIM3+eIqhj4I='},
        'Tianyuan Wang': {'address': vita_address, 'items': furniture_items, 'email': '2521798w@student.gla.ac.uk',
                          'Profile_picture': 'Tianyuan Wang.jpg',
                          'password': 'pbkdf2_sha256$120000$WFTo7No5Rzb0$2wbqRcQci49Vt4XDoq4HbHB9UAx2LiDpIM3+eIqhj4I='},
        'Shunyu Yang': {'address': dm_address, 'items': clothing_items, 'email': '2627664y@student.gla.ac.uk',
                        'Profile_picture': 'Shunyu Yang.jpg',
                        'password': 'pbkdf2_sha256$120000$WFTo7No5Rzb0$2wbqRcQci49Vt4XDoq4HbHB9UAx2LiDpIM3+eIqhj4I='}}

    # goods data

    # populate users
    for user, user_data in users.items():
        c = add_users(user, user_data['password'], user_data['email'], user_data['Profile_picture'])
        for p in user_data['address']:
            add_address(c, p['name'], p['Address'], p['postcode'], p['phone'], p['is_default'])
        for f in user_data['items']:
            z = add_items(c, f['itemName'], f['price'], f['describe'], f['itemCategory'])
            add_itemsPicture(z, f['image'])

    # populate goods

    # populate order

def add_address(user, name, address, postcode, phone, is_default):
    p = Address.objects.get_or_create(user=user, name=name)[0]
    p.Address = address
    p.postcode = postcode
    p.phone = phone
    p.is_default = is_default
    p.save()
    return p


def add_users(username, password, email, profile_picture):
    c = User.objects.get_or_create(username=username)[0]
    c.password = password
    c.email = email
    c.Profile_picture = profile_picture
    c.save()
    return c

def add_items(user, itemsName, price ,describe, itemCategory):
    f = Items.objects.create(user=user)
    f.itemsName = itemsName
    f.price = price
    f.describe = describe
    f.itemCategory = itemCategory
    f.save()
    return f

def add_itemsPicture(item, itemPicture):
    g = ItemPicture.objects.get_or_create(item=item)[0]
    g.itemPicture = itemPicture
    g.save()
    return g

 # Start execution here!
if __name__ == '__main__':
    print('Starting VAT population script...')
    populate()