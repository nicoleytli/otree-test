from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class FirstPage(Page):
    form_model = models.Player
    form_fields = ['number']

    def before_next_page(self):
        for i in range(len(Constants.questions)):
            if self.player.number == Constants.questions[i]['Number']:
                self.player.name = Constants.questions[i]['Name']
                self.player.grade = Constants.questions[i]['Grade']
                self.player.major = Constants.questions[i]['Major']


class SecondPage(Page):
    pass


class ThirdPage(Page):
    pass


class Introduction(Page):
    pass


class Test(Page):
    form_model = models.Player
    form_fields = ['bankA', 'bankB', 'fluidityA', 'fluidityB', 'utility1', 'utility2',
                   'utility3', 'utility4', 'utility5', 'utility6', 'utility7', 'utility8',
                   'utility9', 'utility10', 'utility11', 'utility12']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    FirstPage,
    SecondPage,
    ThirdPage,
    Introduction,
    Test,
    ResultsWaitPage,
    Results
]
