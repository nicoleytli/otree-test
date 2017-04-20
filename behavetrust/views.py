from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class FirstWait(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG'



class Introduction(Page):

    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG'

    def before_next_page(self):
        self.player.fchoice()


class SecondWait(WaitPage):

    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG'


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = models.Group
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1 and (self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG')

    def vars_for_template(self):
        other = self.player.get_others_in_group()[0]

        return {'counter': other.choice}


class Sendback(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2 and (self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG')

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplication_factor
        other = self.player.get_others_in_group()[0]
        counter = other.choice

        return {
                'tripled_amount': tripled_amount,
                'prompt': 'Please enter a number from 0 to %s:' % tripled_amount,
                'counter': counter
        }

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG'


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
        }

    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG'

class ThirdWait(WaitPage):
    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
               self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
               self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG'

page_sequence = [
    FirstWait,
    Introduction,
    SecondWait,
    Send,
    ThirdWait,
    Sendback,
    ResultsWaitPage,
    Results,
]
