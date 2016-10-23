from django.conf.urls import url
from django.contrib import admin
from api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', views.get_news, name="get_news"),
    url(r'^pppteg/', views.get_pppteg, name="get_pppteg"),
    url(r'^docs/', views.get_docs, name="get_docs"),
    url(r'^event/', views.get_event, name="get_event")
]
