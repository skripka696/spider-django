from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import View
from web import settings
from web_app import forms
import redis
import json


class BaseView(View):
    success_url = '/'
    template_name = 'web_app/index.html'

    def __init__(self):
        super(BaseView, self).__init__()
        self.r = redis.Redis(host=settings.REDIS_HOST,
                             port=settings.REDIS_PORT)

    def post(self, request):
        spider_name = request.POST['spider']
        result_data = {'redis_key1': request.POST['redis_key1'],
                       'redis_key2': request.POST['redis_key2'],
                       'redis_key3': request.POST['redis_key3']}
        self.r.lpush('%s:start_urls' % (spider_name), json.dumps(result_data))

        return HttpResponse('success')

    def get(self, request):
        context = {'form': forms.StartSpiderForm()}
        return render(request, self.template_name, context)