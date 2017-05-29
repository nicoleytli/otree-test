from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class Group_by_treatment(WaitPage):

    group_by_arrival_time = True
    players_per_group = 2

    def get_players_for_group(self, waiting_players):

        # since the list is ordered by arrival time, the last element is the newest player who just arrived
        newest_player = waiting_players[-1]

        # the players who were already waiting (each of them was newest_player a previous time this method was called)
        already_waiting = waiting_players[:-1]

        # check if any of the already waiting players have the same treatment as the newly arrived player
        possible_partners = [p for p in already_waiting if p.participant.vars['group'] == newest_player.participant.vars['group']]

        # if so, put them in a group together
        if possible_partners:
            return [possible_partners[0], newest_player]


class Introduction(Page):
    pass


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = models.Group
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplication_factor

        return {
                'tripled_amount': tripled_amount,
                'prompt':
                    'Please enter an amount from $0 to %s:' % tripled_amount}

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()



class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
        }




page_sequence = [
    Group_by_treatment,
    Introduction,
    Send,
    WaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
