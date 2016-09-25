from django.conf.urls import url
from django.contrib import admin
from api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', views.get_news, name="get_news")
]
