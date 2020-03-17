import pytest
from django.test import Client
from plan.models import *

client = Client()

def test_item_crud(jwt_token, merchant, store):
    list_url = '/plan/items/'
    detail_url = '/plan/items/{}/'

    create_payload = {
        "item_name": "test-item",
        "item_price": 120,
        "item_description": "Test description, just to check it out",
        "merchant": merchant.pk
    }
    response = client.post(list_url, 
                        create_payload,
                        content_type='application/json')
    assert response.status_code == 201
    item = Item.objects.get(item_name='test-item')
    if item:
        assert True

    update_payload = {
        "item_name": "new-test-item",
        "merchant": merchant.pk
    }
    detail_url = detail_url.format(item.pk)                        
    response = client.put(detail_url, 
                        update_payload,
                        content_type='application/json')
    new_item = Item.objects.get(pk=item.pk)
    assert response.status_code == 200
    assert new_item.item_name == 'new-test-item'

    response = client.delete(detail_url, 
                            content_type='application/json')                        
    try:
        item = Item.objects.get(pk=item.pk) 
        assert False
    except Exception:
        assert True
                            
                                              
                      
