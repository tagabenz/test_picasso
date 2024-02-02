from celery import shared_task
from time import sleep


@shared_task
def file_processing(obj):
    sleep(5)
    obj.processed = True
    
    return obj.save()