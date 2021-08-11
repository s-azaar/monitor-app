import logging
from django.db import models

logger = logging.getLogger(__name__)

class CPU(models.Model):
    cpu_utilization = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=50)

    def __str__(self):
        return f'At {self.timestamp} the CPU utilization is {self.cpu_utilization}'

    def save(self, *args, **kwargs):
        queryset = CPU.objects.all()
        if queryset.count() >= 24:
            logger.info('It seems we have 24 records')
            queryset.delete()
            logger.info('Delete all records')
        super(CPU, self).save(*args, **kwargs)
        logger.info('Add new record to the CPU model')


class Memory(models.Model):
    used = models.CharField(max_length=20)
    free = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=50)

    def __str__(self):
        return f'At {self.timestamp} the free memory is {self.free} while the used memory is {self.used}'

    def save(self, *args, **kwargs):
        queryset = Memory.objects.all()
        if queryset.count() >= 24:
            logger.info('It seems we have 24 records')
            queryset.delete()
            logger.info('Delete all records')
        super(Memory, self).save(*args, **kwargs)
        logger.info('Add new record to the Memory model')


class Disk(models.Model):
    used = models.CharField(max_length=20)
    free = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=50)

    def __str__(self):
        return f'At {self.timestamp} the free disk is {self.free} while the used disk is {self.used}'

    def save(self, *args, **kwargs):
        queryset = Disk.objects.all()
        if queryset.count() >= 24:
            logger.info('It seems we have 24 records')
            queryset.delete()
            logger.info('Delete all records')
        super(Disk, self).save(*args, **kwargs)
        logger.info('Add new record to the Disk model')


