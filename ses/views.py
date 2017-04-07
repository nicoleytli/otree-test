from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants





class Demographic(Page):
    form_model = models.Player
    form_fields = ['birth', 'educ', 'dip', 'duty', 'emptype', 'work']


class Demographic2(Page):
    form_model = models.Player
    form_fields = ['myclass']


class Demo3(Page):
    form_model = models.Player
    form_fields = ['whichclass']

    def is_displayed(self):
        return self.player.myclass == 1


class Demo4(Page):
    form_model = models.Player
    form_fields = ['chclass']

    def is_displayed(self):
        return self.player.myclass == 2


class Demo5(Page):
    form_model = models.Player
    form_fields = ['middle']

    def is_displayed(self):
        return self.player.whichclass == 2 or self.player.chclass == 2


class Demo6(Page):
    form_model = models.Player
    form_fields = ['working']

    def is_displayed(self):
        return self.player.whichclass == 3 or self.player.chclass == 3

class End(Page):
    pass

page_sequence = [
    Demographic,
    Demographic2,
    Demo3,
    Demo4,
    Demo5,
    Demo6,
    End
]
