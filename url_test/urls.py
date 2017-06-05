from django.conf.urls import url
from otree.urls import urlpatterns

import url_test.views

urlpatterns.append(
    url(r'^redirect／$', 'url_test.views.get_redir', name="redirection",)
)
