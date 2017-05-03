from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPagetrust(Page):
    form_model = models.Player
    form_fields = ['partner']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children',
                  'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants',
                  'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination',
                  'Send troops to fight ISIS']

        issue = issues[self.participant.vars['issue'] - 1]
        level = self.participant.vars['important']
        if self.participant.vars['opinion_%s' % self.participant.vars['issue']] == 'Disagree':
            opinion = 'oppose'
        else:  #不可能有indifferent的情况
            opinion = 'favor'
        direction = self.player.preference_party

        return {'issue': issue,
                'level': level,
                'direction': direction,
                'opinion': opinion}

    def partner_choices(self):
        if self.player.preference_party == 'same':
            mylist = [[3, 'I play trust game against someone who reports same preference on this issue'],
                      [4, 'I play trust game against someone who reports being the same party']]
        else:
            mylist = [[1, 'I play trust game against someone who reports opposite preference on this issue'],
                      [2, 'I play trust game against someone who reports being the opposite party']]
        return mylist

    def is_displayed(self):
        return self.participant.vars['issue'] != 999




class MyPagetrust2(Page):
    form_model = models.Player
    form_fields = ['partner']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children',
                  'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants',
                  'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination',
                  'Send troops to fight ISIS']

        self.participant.vars['issue2'] = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        issue = issues[self.participant.vars['issue2'] - 1]
        direction = self.player.preference_party
        if direction == 'same':
            same_different = 'same'
        else:
            same_different = 'different'

        return {'issue': issue,
                'direction': direction,
                'same_different': same_different}


    def partner_choices(self):
        if self.player.preference_party == 'same':
            mylist = [[3, 'I play trust game against someone who reports same opinion on this issue'],
                      [4, 'I play trust game against someone who reports being the same party']]
        else:
            mylist = [[1, 'I play trust game against someone who reports different opinion on this issue'],
                      [2, 'I play trust game against someone who reports being the opposite party']]

        return mylist

    def is_displayed(self):
        return self.participant.vars['issue'] == 999


class Donation_party(Page):
    form_model = models.Player
    form_fields = ['donation_party']


page_sequence = [
    MyPagetrust,
    MyPagetrust2,
    Donation_party
]
