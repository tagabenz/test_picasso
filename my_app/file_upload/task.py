from celery import shared_task
from time import sleep

from file_upload.models import File
from . import serializers

@shared_task
def file_processing(data):
    sleep(5)
    # obj = File.objects.get(pk=data.get('id'))
    # obj.processed = True
    # return obj.save() 
    return data