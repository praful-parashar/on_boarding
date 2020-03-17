from .models import *
from random import randrange

from django.db import transaction
@transaction.atomic()
def run():
    merchant = Merchant.objects.create(merchant_name="More Supermarket")
    location_names = ['Agra', 'Delhi', 'Chandigarh', 'Bangalore', 'Mumbai']
    for i in range(0, 5):
        store_name = "{}-{}".format(merchant, location_names[i])
        store = Store.objects.create(store_name=store_name, 
                                    store_address="Test store - No add",
                                    s_latitude=randrange(50, 150, 2),
                                    s_longitude=randrange(75, 160, 1),
                                    merchant=merchant)
    item_names = [
                
                'Show piece', 'Futon cushions', 'Cutlery', 'Signature blanket', 'Jute rope']    
    c = 0                                    
    for i in range(c, c+5):
        item = Item.objects.create(item_name=item_names[i],
                                    item_price=randrange(100, 3000, 1),
                                    merchant=merchant)
                                  
                                        

