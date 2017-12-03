from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    ### url/music/
    url(r'^$',views.index,name='index'),

    ###url/music/[some_id]
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail')
]
