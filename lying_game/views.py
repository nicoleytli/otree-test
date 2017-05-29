from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    pass


class Results(Page):
    form_model = models.Player
    form_fields = ['match']

    def vars_for_template(self):
        number = random.randint(0, 10)
        return {'number': number}

    def before_next_page(self):
        self.group.set_payoffs()


page_sequence = [
    MyPage,
    Results
]
