from django.db import models
from django.conf import settings


class Task(models.Model):
    spider = models.CharField(max_length=30, choices=settings.SPIDERS)
    status = models.CharField(max_length=30, choices=settings.SPIDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}/{}'.format(self.spider, self.status)
