from django.conf.urls import url
from otree.urls import urlpatterns
from url_test import views as url_views
from url_test.views import MyPage

url(r'(\d+)/$', MyPage.as_view())
