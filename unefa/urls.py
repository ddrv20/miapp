from django.conf.urls import url
from django.contrib import admin
from api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', views.get_news, name="get_news"),
    url(r'^pppteg/', views.get_pppteg, name="get_pppteg"),
    url(r'^docs/', views.get_docs, name="get_docs"),
    url(r'^event/', views.get_event, name="get_event"),
    url(r'^login/$', views.set_user),
    #url(r'^login/(\w+)/(\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(\w+)/(\w+)/(\d+)/$', views.set_user),
]
