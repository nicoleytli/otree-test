from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def is_displayed(self):
        return self.player.is_4 == 0


class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    players_per_group = 2

    def after_all_players_arrive(self):
        self.group.get_treatment()

    def is_displayed(self):
        return self.player.is_4 == 0


class Player1(Page):
    form_model = models.Player
    form_fields = ['Message_12']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.player.is_4 == 0

    timeout_seconds = 240
    timeout_submission = {'Message_12': 'Message 1'}


class Player2(Page):
    form_model = models.Player
    form_fields = ['option_AB']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0

    timeout_seconds = 240
    timeout_submission = {'option_AB': 'Option A'}


class treatment_4(Page):
    form_model = models.Player
    form_fields = ['option4_1', 'option4_2']

    def before_next_page(self):
        self.player.payoff = 0.30

    def is_displayed(self):
        return self.player.is_4 == 1


class Result_123(Page):

    def vars_for_template(self):
        return {'task2': self.player.payoff - 0.20}


class Demographic(Page):
    form_model = models.Player
    form_fields = ['gender', 'age', 'religion', 'service'] #'getcode_1', 'getcode_2']


class WaitforP1(WaitPage):
    def is_displayed(self):
        return self.player.is_4 == 0


class Task3(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0


page_sequence = [
    MyWaitPage,
    Player1,
    Task3,
    WaitforP1,
    Player2,
    treatment_4,
    Demographic,
    ResultsWaitPage,
    Result_123
]
