from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['time_stamp_1a', 'time_stamp_1b', 'time_stamp_2a', 'time_stamp_2b',
                   'time_stamp_3a', 'time_stamp_3b']

    def before_next_page(self):
        self.player.time_1 = (self.player.time_stamp_1b - self.player.time_stamp_1a) / 1000

        self.player.time_2 = (self.player.time_stamp_2b - self.player.time_stamp_2a) / 1000

        self.player.time_3 = (self.player.time_stamp_3b - self.player.time_stamp_3a) / 1000




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass



class Results(Page):
    form_model = models.Player
    form_fields = ['name', 'time_stamp_entered', 'time_stamp_click']


page_sequence = [
    MyPage,
    # ResultsWaitPage,
    # Results
]
