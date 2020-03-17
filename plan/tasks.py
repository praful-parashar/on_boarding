from celery import Celery
from celery.task import task
app = Celery('hello', broker='amqp://localhost')

@app.task
def hello():
    return 'hello world'

@task
def once_more():
    return 'Once More'
