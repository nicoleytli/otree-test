from __future__ import division
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from urllib.parse import urlencode
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect


class FirstPage(Page):
    form_model = models.Player
    form_fields = ['current_url']
    # def index(request):
    #     return render_to_response(
    #         'url_test/FirstPage.html',
    #         # {'title': 'User profile'},
    #         context_instance=RequestContext(request)
    #     )


class MyPage(Page):
    form_model = models.Player
    form_fields = ['now_url', 'datastring']

    def vars_for_template(self):
        url = self.player.participant._start_url()
        id = url.split('/', 3)
        self.player.participant_label = id[2]

        params = {'participant_label': self.player.participant_label}
        base_url = 'http://159.203.82.211/surveys/-KkJ0pght7x5b2XV6gKE/sections/0'
        url = base_url + '?' + urlencode(params)

        return {'link': url}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass









page_sequence = [
    FirstPage,
    # ResultsWaitPage,
    MyPage,
    Results
]
