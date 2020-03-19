import structlog
from celery import Celery
from celery.task import task
from django.apps import apps
app = Celery('hello', broker='amqp://localhost')

logger = structlog.getLogger(__name__)
@app.task
def hello():
    return 'hello world'

@task
def once_more():
    return 'Once More'

@task
def create_txs(tx_data):
    tx_model = apps.get_model(app_label='plan', model_name='Transaction')
    merc_model = apps.get_model(app_label='plan', model_name='Merchant')
    store_model = apps.get_model(app_label='plan', model_name='Store')
    try:
        merchant = merc_model.objects.get(pk=tx_data['merchant'])
        store = store_model.objects.get(pk=tx_data['store'])
        instance = tx_model()
        instance.merchant = merchant
        instance.store = store
        instance.save()
        items = tx_data['items']
        for i in range(0, len(items)):
            instance.items.add(items[i])
        instance.save()
        logger.info("transaction_object", tx=instance.pk)
        return "Done"
    except Exception as e:
        logger.info("exception_occured_in_tx_creation", exception=str(e))
        return str(e)
    

        
