import json
import logging

from django.http.response import HttpResponse

from .models import CPU, Disk, Memory

logger = logging.getLogger(__name__)


def store_cpu_usages(request):
    if request.method == 'POST':
        logger.info("New CPU's usage has arrived")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cpu_utilization = body['cpu_utilization']
        timestamp = body['timestamp']
        CPU.objects.create(cpu_utilization=cpu_utilization, timestamp=timestamp)
        res = HttpResponse('The status has been stored correctly')
        res.status_code = 302
        return res


def store_memory_usages(request):
    if request.method == 'POST':
        logger.info("New Memory's usage has arrived")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        free = body['free']
        used = body['used']
        timestamp = body['timestamp']
        Memory.objects.create(free=free, used=used, timestamp=timestamp)
        res = HttpResponse('The status has been stored correctly')
        res.status_code = 302
        return res


def store_disk_usages(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        logger.info("New Disk's usage has arrived")
        body = json.loads(body_unicode)
        free = body['free']
        used = body['used']
        timestamp = body['timestamp']
        Disk.objects.create(free=free, used=used, timestamp=timestamp)
        res = HttpResponse('The status has been stored correctly')
        res.status_code = 302
        return res
