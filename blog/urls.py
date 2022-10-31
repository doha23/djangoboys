from django.urls import path
# 장고함수인 path와 blog 애플리케이션에서 사용할 모든 views를 import함
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]