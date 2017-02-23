from django.conf.urls import url
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$',views.index,name ='index'),
    url(r'^todos/getlist/', views.getlist.as_view()),
    url(r'^todos/getlist2/', views.getlist2.as_view()),
    url(r'^todos/getlistitem/(?P<pk>\d+)/', views.getlistitem.as_view()),
    url(r'^todos/updateview/(?P<pk>\d+)/', views.updateview.as_view()),
    url(r'^todos/deleteview/(?P<pk>\d+)/', views.deleteview.as_view()),

    url(r'^details/(?P<pk>[0-9]+)/$', views.details, name='details'),
    url(r'^add/$', views.add, name='add'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
