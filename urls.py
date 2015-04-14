from django.conf.urls import include, url
from django.contrib import admin

from imageboard import views

urlpatterns = [
    url(r'^', include('imageboard.urls', namespace="imageboard")),
    # Examples:
    # url(r'^$', 'ak_project.views.home', name='home'),
    # url(r'^ak_project/', include('ak_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'upload/', views.upload, name = 'jfu_upload' ),
    url(r'^delete/(?P<pk>\d+)$', views.upload_delete, name = 'jfu_delete' ),

]
