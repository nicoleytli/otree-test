from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from urllib.parse import urlencode

class MyPage(Page):

    def vars_for_template(self):
        url = self.player.participant._start_url()
        id = url.split('/', 3)
        self.player.participant_label = id[2]

        params = {'participant_label': self.player.participant_label}
        base_url = 'http://159.203.82.211/surveys/-KkJ0pght7x5b2XV6gKE/sections/0'
        url = base_url + '?' + urlencode(params)

        self.player.url = url

        return {'link': url}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    # ResultsWaitPage,
    # Results
]
