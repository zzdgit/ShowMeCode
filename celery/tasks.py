import time
from celery_conf import app

@app.task
def add(x, y):
    time.sleep(3)
    print(x + y)
    return x + y
