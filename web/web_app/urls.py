from django.conf.urls import url
from django.contrib import admin
from web_app import views

urlpatterns = [
    url(r'^', views.BaseView.as_view()),
]
