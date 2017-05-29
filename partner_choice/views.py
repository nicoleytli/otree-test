from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MyPage(Page):
    form_model = models.Player
    form_fields = ['partner']

    def vars_for_template(self):
        issue = 'Reduce the difference in income'
        return {'direction': self.player.preference_party,
                'issue': issue}

    def partner_choices(self):
        if self.player.preference_party == 'same':
            mylist = [[3, 'I play trust game against someone who reports same preference on this issue'],
                      [4, 'I play trust game against someone who reports being the same party']]
        else:
            mylist = [[1, 'I play trust game against someone who reports opposite preference on this issue'],
                      [2, 'I play trust game against someone who reports being the opposite party']]
        return mylist

    def before_next_page(self):
        if self.player.partner == 1:
            if self.player.preference == 'Favor':
                self.participant.vars['group'] = 'O'
            else:
                self.participant.vars['group'] = 'F'
        elif self.player.partner == 3:
            if self.player.preference == 'Favor':
                self.participant.vars['group'] = 'F'
            else:
                self.participant.vars['group'] = 'O'
        elif self.player.partner == 2:
            if self.player.party == 'Democrat':
                self.participant.vars['group'] = 'R'
            else:
                self.participant.vars['group'] = 'D'
        else:
            if self.player.party == 'Democrat':
                self.participant.vars['group'] = 'D'
            else:
                self.participant.vars['group'] = 'R'


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
