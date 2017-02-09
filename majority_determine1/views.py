from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decide(Page):
    form_model = models.Player
    form_fields = ['decision']

class Decide2(Page):
    form_model = models.Player
    form_fields = ['option1', 'option2', 'option3', 'option4']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass


page_sequence = [
    Decide,
    Decide2,
    ResultsWaitPage,
    Results
]
