from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    form_model = models.Player
    form_fields = ['party_donation']

    def vars_for_template(self):
        issue = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children',
                  'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants',
                  'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination',
                  'Send troops to fight ISIS']

        preference = ['Favor', 'Oppose', 'Favor', 'Favor', 'Favor', 'Oppose', 'Oppose', 'Neither Favor nor oppose', 'Favor', 'Favor']

        mylist = zip(issue, preference)
        return {'mylist': mylist}


class Donation(Page):
    form_model = models.Player
    form_fields = ['donation_choice']

    def is_displayed(self):
        return self.player.party_donation == 2


class PartyID(Page):
    form_model = models.Player
    form_fields = ['party_choice']

    def is_displayed(self):
        return self.player.party_donation == 1



class Results(Page):
    def vars_for_template(self):
        if self.player.party_donation == 1:
            answer = random.choice(['Strong Democrat', 'Weak Democrat', 'Lean Democrat', 'Independent', 'Lean Republican',
                                    'Weak Republican', 'Strong Republican'])
            mylist = ['Strong Democrat', 'Weak Democrat', 'Lean Democrat', 'Independent', 'Lean Republican', 'Weak Republican',
                        'Strong Republican']
            choice = mylist[self.player.party_choice - 1]
        else:
            answer = random.choice(['organization 1', 'organization 2', 'organization 3', 'organization 4', 'organization 5',
                                    'organization 6', 'organization 7', 'organization 8', 'organization 9', 'organization 10'])
            mylist = ['organization 1', 'organization 2', 'organization 3', 'organization 4', 'organization 5',
                    'organization 6', 'organization 7', 'organization 8', 'organization 9', 'organization 10']
            choice = mylist[self.player.donation_choice - 1]

        return {'answer': answer,
                'choice': choice}

page_sequence = [
    MyPage,
    Donation,
    PartyID,
    Results
]
