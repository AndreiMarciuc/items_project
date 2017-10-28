from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^new$',views.new),
    url(r'^create$',views.create),
    url(r'^add/(?P<id>\d+)$',views.addItem),
    url(r'^remove/(?P<id>\d+)$',views.removeItem),
    url(r'^show/(?P<id>\d+)$',views.show),
    
]
