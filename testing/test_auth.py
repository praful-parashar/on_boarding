import pytest
from django.contrib.auth.models import User
from django.test import Client
from plan.models import *

client = Client()
token_url = '/plan/api/token/'

def test_authenticated_user(user):
    payload = {
        "username": user.username,
        "password": 'test_password'
    }
    response = client.post(token_url,
                        payload,
                        content_type='application/json')
    assert response.status_code == 200 


def test_unauthenticated_user(user, jwt_token):
    payload = {
        "username": "test-unauth-user",
        "password": "test_unauth_pass"
    }                    
    response = client.post(token_url,
                        payload,
                        content_type='application/json')
    assert response.status_code == 401                    
                           