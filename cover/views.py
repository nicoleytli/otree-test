from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time

class MyPage(Page):
    def before_next_page(self):
        self.participant.vars['firsttime'] = time.time()


page_sequence = [
    MyPage,
]
