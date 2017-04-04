import os
import sys
import json
import scrapy
import django
from selenium import webdriver
from scrapy_redis.spiders import RedisSpider
from django.utils.functional import cached_property
from spider.settings import DRIVER_PATH, SPIDER_STATUS, BASE_DIR
from scrapy_redis.utils import bytes_to_str

script_path = os.path.join(BASE_DIR, 'web')
sys.path.append(script_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings'
django.setup()

from web_app.models import Task


class BaseSpider(RedisSpider):
    WEB_DRIVER_USED = False

    @cached_property
    def driver(self):
        self.WEB_DRIVER_USED = True
        return webdriver.Firefox(executable_path=DRIVER_PATH)

    def set_status(self, status):
        task, created = Task.objects.get_or_create(spider=self.name)
        task.status = status
        task.save()

    def make_request_from_data(self, data):
        """
        This method will be called when we receive a request.
        :param data: JSON serialized
        """

        self.params = json.loads(bytes_to_str(data, self.redis_encoding))
        self.set_status(SPIDER_STATUS['Processing'])
        return self.make_requests_from_url(self.start_url)

    def close(spider, reason):
        spider.set_status(SPIDER_STATUS['Success finished'])
        if spider.WEB_DRIVER_USED:
            spider.driver.quit()