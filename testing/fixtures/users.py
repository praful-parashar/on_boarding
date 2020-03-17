import pytest
import json
from django.contrib.auth.models import *
from django.test import Client

client = Client()
test_password = 'test_password'
@pytest.fixture
def user(db):
    user = User.objects.create(username='test-user')
    user.set_password(test_password)
    user.save()

    return user

@pytest.fixture
def jwt_token(db, user):
    token_url = '/plan/api/token/'
    payload = {
        "username": user.username,
        "password": test_password
    }
    response = client.post(token_url, 
                        payload, 
                        content_type='application/json')  
    json_response = json.loads(response.content)
    return json_response               

    
    

