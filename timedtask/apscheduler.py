# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test1():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '你好1')


def aps_test2():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '你好2')


scheduler = BlockingScheduler()
job = scheduler.add_job(func=aps_test1, trigger='cron', second='*/5', id='1')
job = scheduler.add_job(func=aps_test2, trigger='cron', second='*/3', id='2')
scheduler.start()

# scheduler.modify_job(1, second='*/3')
