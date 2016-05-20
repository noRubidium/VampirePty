from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(\d+)/$', views.page, name='index'),
    url(r'^(\d+)/$', views.detail, name='index'),
]
