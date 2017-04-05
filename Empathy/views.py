from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Introduction(Page):
    def before_next_page(self):
        self.group.get_treatment()


class Welcome(Page):
    def before_next_page(self):
        if self.player.condition == 'None':
            # Retrieve the condition assignments from each participant so far
            conditions_so_far = []
            for p in self.subsession.get_players():
                conditions_so_far.append(p.condition)

            # Count how often each condition has been run
            conditions_n = {}
            for c in Constants.conditions:
                conditions_n[c] = conditions_so_far.count(c)

            # Create a new array containing the conditions that have been run the least amount of times
            conditions = []
            for c, n in conditions_n.items():
                if n == min(conditions_n.values()):
                    conditions.append(c)

            # Randomly assign the participant to one of these conditions
            temp = random.choice(conditions)
            for p in self.group.get_players():
                p.condition = temp
        else:
            pass



class Wait(WaitPage):
    group_by_arrival_time = True
    players_per_group = 2


class ResultWait(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_scores()


class Priming(Page):
    form_model = models.Player
    form_fields = ['text']


class Eye1(Page):
    form_model = models.Player
    form_fields = ['option_1']



class Eye2(Page):
    form_model = models.Player
    form_fields = ['option_2']



class Eye3(Page):
    form_model = models.Player
    form_fields = ['option_3']



class Eye4(Page):
    form_model = models.Player
    form_fields = ['option_4']



class Eye5(Page):
    form_model = models.Player
    form_fields = ['option_5']



class Eye6(Page):
    form_model = models.Player
    form_fields = ['option_6']



class Eye7(Page):
    form_model = models.Player
    form_fields = ['option_7']



class Eye8(Page):
    form_model = models.Player
    form_fields = ['option_8']



class Eye9(Page):
    form_model = models.Player
    form_fields = ['option_9']



class Eye10(Page):
    form_model = models.Player
    form_fields = ['option_10']



class Eye11(Page):
    form_model = models.Player
    form_fields = ['option_11']



class Eye12(Page):
    form_model = models.Player
    form_fields = ['option_12']



class Eye13(Page):
    form_model = models.Player
    form_fields = ['option_13']



class Eye14(Page):
    form_model = models.Player
    form_fields = ['option_14']



class Eye15(Page):
    form_model = models.Player
    form_fields = ['option_15']



class Eye16(Page):
    form_model = models.Player
    form_fields = ['option_16']



class Eye17(Page):
    form_model = models.Player
    form_fields = ['option_17']



class Eye18(Page):
    form_model = models.Player
    form_fields = ['option_18']



class Eye19(Page):
    form_model = models.Player
    form_fields = ['option_19']



class Eye20(Page):
    form_model = models.Player
    form_fields = ['option_20']



class Eye21(Page):
    form_model = models.Player
    form_fields = ['option_21']



class Eye22(Page):
    form_model = models.Player
    form_fields = ['option_22']



class Eye23(Page):
    form_model = models.Player
    form_fields = ['option_23']



class Eye24(Page):
    form_model = models.Player
    form_fields = ['option_24']



class Eye25(Page):
    form_model = models.Player
    form_fields = ['option_25']



class Eye26(Page):
    form_model = models.Player
    form_fields = ['option_26']



class Eye27(Page):
    form_model = models.Player
    form_fields = ['option_27']



class Eye28(Page):
    form_model = models.Player
    form_fields = ['option_28']



class Eye29(Page):
    form_model = models.Player
    form_fields = ['option_29']



class Eye30(Page):
    form_model = models.Player
    form_fields = ['option_30']



class Eye31(Page):
    form_model = models.Player
    form_fields = ['option_31']



class Eye32(Page):
    form_model = models.Player
    form_fields = ['option_32']



class Eye33(Page):
    form_model = models.Player
    form_fields = ['option_33']


class Eye34(Page):
    form_model = models.Player
    form_fields = ['option_34']


class Eye35(Page):
    form_model = models.Player
    form_fields = ['option_35']


class Eye36(Page):
    form_model = models.Player
    form_fields = ['option_36']

    # def before_next_page(self):
    #     self.group.get_scores()

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def is_displayed(self):
        return self.player.is_4 == 0


class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    players_per_group = 2

    def after_all_players_arrive(self):
        self.subsession.get_treatment()

    def is_displayed(self):
        return self.player.is_4 == 0


class Player1(Page):
    form_model = models.Player
    form_fields = ['Message_12']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.player.is_4 == 0

    timeout_seconds = 480
    timeout_submission = {'Message_12': 'Message 1'}


class Player2(Page):
    form_model = models.Player
    form_fields = ['option_AB']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0

    timeout_seconds = 480
    timeout_submission = {'option_AB': 'Option A'}


class treatment_4(Page):
    form_model = models.Player
    form_fields = ['option4_1', 'option4_2']

    def before_next_page(self):
        self.player.payoff = 0.30

    def is_displayed(self):
        return self.player.is_4 == 1


class Result_123(Page):

    def vars_for_template(self):
        return {'task2': self.player.payoff - 0.20}


class Demographic(Page):
    form_model = models.Player
    form_fields = ['gender', 'age', 'religion', 'service'] #'getcode_1', 'getcode_2']



class WaitforP1(WaitPage):
    def is_displayed(self):
        return self.player.is_4 == 0


class Task3(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.is_4 == 0


page_sequence = [
    Wait,
    Welcome,
    Priming,
    Introduction,
    Eye1,
    Eye2,
    Eye3,
    Eye4,
    Eye5,
    Eye6,
    Eye7,
    Eye8,
    Eye9,
    Eye10,
    Eye11,
    Eye12,
    Eye13,
    Eye14,
    Eye15,
    Eye16,
    Eye17,
    Eye18,
    Eye19,
    Eye20,
    Eye21,
    Eye22,
    Eye23,
    Eye24,
    Eye25,
    Eye26,
    Eye27,
    Eye28,
    Eye29,
    Eye30,
    Eye31,
    Eye32,
    Eye33,
    Eye34,
    Eye35,
    Eye36,
    ResultWait,
    Player1,
    Task3,
    WaitforP1,
    Player2,
    treatment_4,
    Demographic,
    ResultsWaitPage,
    Result_123
]
