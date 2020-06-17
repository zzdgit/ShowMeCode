from celery import Celery

redis = True

if redis:
    app = Celery('tasks', broker='redis://10.200.60.4/7')
else:
    app = Celery('tasks', broker='amqp://localhost')
