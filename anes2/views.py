from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Partisanship1(Page):
    form_model = models.Player
    form_fields = ['partisanship1']

    def vars_for_template(self):
        ans = ['DEMOCRAT', 'REPUBLICAN']
        random.shuffle(ans)
        p1 = ans[0]
        p2 = ans[1]
        if p1 == 'DEMOCRAT':
            self.player.order1 = 1
        else:
            self.player.order1 = 2
        return {'partisanship1': p1,
                'partisanship2': p2}


class Partisanship2(Page):
    form_model = models.Player
    form_fields = ['partisanship2']

    def vars_for_template(self):
        if self.player.partisanship1 == 1:
            par = 'Democrat'
        else:
            par = 'Republican'

        return {'partisanship': par}

    def is_displayed(self):
        return self.player.partisanship1 == 1 or self.player.partisanship1 == 2


class Partisanship3(Page):
    form_model = models.Player
    form_fields = ['partisanship3']

    def vars_for_template(self):
        ans = ['Democratic', 'Republican']
        random.shuffle(ans)
        p1 = ans[0]
        p2 = ans[1]
        if p1 == 'Democratic':
            self.player.order3 = 1
        else:
            self.player.order3 = 2
        return {'par1': p1,
                'par2': p2}

    def is_displayed(self):
        return self.player.partisanship1 == 3 or self.player.partisanship1 == 5 or self.player.partisanship1 == 8


class Priming1(Page):
    pass


class Priming2(Page):
    pass


class Control(Page):
    pass



class Results(Page):
    pass


page_sequence = [
    MyPage,
    Control,
    Priming1,
    Priming2,
    Partisanship1,
    Partisanship2,
    Partisanship3
]
