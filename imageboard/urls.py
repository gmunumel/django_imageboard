#from django.conf.urls.defaults import include, url
from django.conf.urls import url, include
#from django.conf import settings
'''
from imageboard.views import (
    PictureCreateView, PictureListView, PictureDeleteView
    )
'''

from . import views

urlpatterns = [
    # index images
    url(r'^$', views.index, name = 'image_index'),
    url(r'^imageboard/$', views.index, name = 'image_index'),

    # index search
    url(r'^search/$', include('haystack.urls')),

    # tags urls
    url(r'^tags/$', views.tags, name = 'tag_index'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.detail_tags, name = 'tag_details'),

    # images urls
    url(r'^imageboard/(?P<image_id>[0-9]+)/$', views.detail, name = 'image_details'),

    # big image urls
    url(r'^imageboard/ib-large/(?P<image_id>[0-9]+)/$', views.ib_large, name = 'image_big_index'),

    # images without tags urls
    url(r'^imageboard/wo-tags/$', views.images_wo_tags, name = 'image_wo_tags_index'),
    url(r'^imageboard/wo-tags/list-tags/$', views.list_tags, name = 'image_wo_tags_list'),

    # ajax ajax_save_tags
    url(r'^imageboard/wo-tags/ajax-save-tags/$', views.ajax_save_tags, name = 'ajax_save_tags'),

    # To create files uploaded
    #url(r'^image/add/$', views.PictureCreateView.as_view(), name='upload-new'),
    #url(r'^image/delete/(?P<pk>\d+)$', views.PictureDeleteView.as_view(), name='upload-delete'),
    #url(r'^admin/imageboard/image/add/$', PictureCreateView.as_view(), name='upload-new'),

    # To view images uploaded
    url(r'^admin/imageboard/image/view/$', views.PictureListView.as_view(), name='upload-view'),

    # To delete a image
    url(r'^admin/imageboard/image/delete/(?P<pk>\d+)$', views.PictureDeleteView.as_view(), name='upload-delete'),

]

