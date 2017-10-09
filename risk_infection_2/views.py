from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class PA_1(Page):
    form_model = models.Player
    form_fields = ['choice']

    def is_displayed(self):
        return (self.player.role == 'A_dep' or self.player.role == 'A_ind') and self.round_number <= 30

    def vars_for_template(self):
        if self.session.vars['fluiditya_%s' % self.round_number] == 'L':
            fluidity = '低'
        else:
            fluidity = '高'
        return {'fluidity': fluidity}



class PA_2(Page):
    form_model = models.Player
    form_fields = ['choice']

    def is_displayed(self):
        return (self.player.role == 'A_dep' or self.player.role == 'A_ind') and self.round_number > 30

    def vars_for_template(self):
        if self.round_number == 1:
            fluidity = 'N'
        else:
            if self.player.role == 'A_dep':
                fluidity = self.session.vars['fluiditya_%s' % (self.round_number - 1)]
            else:
                fluidity = self.session.vars['fluidityb_%s' % (self.round_number - 1)]

        if fluidity == 'H':
            fluidity = '高'
        else:
            fluidity = '低'

        withdraw = self.session.vars['withdraw_B']
        hold = 3 - withdraw

        return {'fluidity': fluidity,
                'withdraw': withdraw,
                'hold': hold}


class WaitforA(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    # def is_displayed(self):
    #     return self.player.role == 'A_ind' or self.player.role == 'A_dep'


class PB_1(Page):
    form_model = models.Player
    form_fields = ['choice']

    def is_displayed(self):
        return (self.player.role == 'B_dep' or self.player.role == 'B_ind') and self.round_number <= 30

    def vars_for_template(self):
        if self.round_number == 1:
            fluidity = 'N'
        else:
            if self.player.role == 'B_dep':
                fluidity = self.session.vars['fluiditya_%s' % (self.round_number - 1)]
            else:
                fluidity = self.session.vars['fluidityb_%s' % (self.round_number - 1)]

        if fluidity == 'H':
            fluidity = '高'
        else:
            fluidity = '低'

        withdraw = self.session.vars['withdraw_A']
        hold = 6 - withdraw
        return {'fluidity': fluidity,
                'withdraw': withdraw,
                'hold': hold}


class PB_2(Page):
    form_model = models.Player
    form_fields = ['choice']

    def is_displayed(self):
        return (self.player.role == 'B_dep' or self.player.role == 'B_ind') and self.round_number > 30

    def vars_for_template(self):
        if self.session.vars['fluiditya_%s' % self.round_number] == 'L':
            fluidity = '低'
        else:
            fluidity = '高'
        return {'fluidity': fluidity}


class WaitforB(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    # def is_displayed(self):
    #     return self.player.role == 'B_dep' or self.player.role == 'B_ind'


class Cover_1(Page):
    def is_displayed(self):
        return self.round_number == 1


class Cover_2(Page):
    def is_displayed(self):
        return self.round_number == 31


class RA_1(Page):
    def is_displayed(self):
        return (self.player.role == 'A_dep' or self.player.role == 'A_ind') and self.round_number <= 30

    def before_next_page(self):
        num = self.round_number
        self.participant.vars['utility_%s' % num] = self.player.utility


class RB_1(Page):
    def is_displayed(self):
        return (self.player.role == 'B_dep' or self.player.role == 'B_ind') and self.round_number <= 30

    def before_next_page(self):
        num = self.round_number
        self.participant.vars['utility_%s' % num] = self.player.utility


class RA_2(Page):
    def is_displayed(self):
        return (self.player.role == 'A_dep' or self.player.role == 'A_ind') and self.round_number > 30

    def before_next_page(self):
        num = self.round_number
        self.participant.vars['utility_%s' % num] = self.player.utility


class RB_2(Page):
    def is_displayed(self):
        return (self.player.role == 'B_dep' or self.player.role == 'B_ind') and self.round_number > 30

    def before_next_page(self):
        num = self.round_number
        self.participant.vars['utility_%s' % num] = self.player.utility


class Result(Page):
    def vars_for_template(self):
        numlist = list(range(1, 61))
        choicelist = random.sample(list(range(1, 61)), 3)
        utility_list = []
        for i in range(1, 61):
            utility_list.append(self.participant.vars['utility_%s' % i])

        mylist1 = zip(numlist[0:30], utility_list[0:30])
        mylist2 = zip(numlist[30:60], utility_list[30:60])

        self.player.payoff = (utility_list[choicelist[0] - 1] + utility_list[choicelist[1] - 1] + utility_list[choicelist[2] - 1]) / 3

        # numlist = list(range(1, 3))
        # choicelist = random.sample(list(range(1, 3)), 2)
        # utility_list = []
        # for i in range(1, 3):
        #     utility_list.append(self.participant.vars['utility_%s' % i])
        #
        # mylist1 = zip(numlist[0:1], utility_list[0:1])
        # mylist2 = zip(numlist[1:2], utility_list[1:2])
        #
        # self.player.payoff = (utility_list[choicelist[0] - 1] + utility_list[choicelist[1] - 1]) / 2

        return {'mylist1': mylist1,
                'mylist2': mylist2,
                'n1': choicelist[0],
                'n2': choicelist[1],
                'n3': choicelist[2],
                'c1': utility_list[choicelist[0] - 1],
                'c2': utility_list[choicelist[1] - 1],
                'c3': utility_list[choicelist[2] - 1],
                'payoff': self.player.payoff}

    def is_displayed(self):
        return self.round_number == 60

page_sequence = [
    Cover_1,
    Cover_2,
    PA_1,
    WaitforA,
    RA_1,
    PB_1,
    WaitforB,
    RB_1,
    PA_2,
    WaitforA,
    RA_2,
    PB_2,
    WaitforB,
    RB_2,
    Result
]
