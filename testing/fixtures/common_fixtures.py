import pytest
from plan.models import *

@pytest.fixture
def merchant(db):
    merchant = Merchant.objects.create(merchant_name='test-merchant')
    return merchant

@pytest.fixture
def store(db, merchant):
    store = Store.objects.create(store_name='test-store',
                                store_address='test-add',
                                s_latitude=100.0,
                                s_longitude=120.1,
                                merchant=merchant)
    return store                                