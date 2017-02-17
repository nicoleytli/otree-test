from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    timeout_seconds = 60


class Welcome(Page):
    timeout_seconds = 60


class Priming(Page):
    form_model = models.Player
    form_fields = ['text']


class Eye1(Page):
    form_model = models.Player
    form_fields = ['option_1']

    timeout_seconds = 10


class Eye2(Page):
    form_model = models.Player
    form_fields = ['option_2']

    timeout_seconds = 10


class Eye3(Page):
    form_model = models.Player
    form_fields = ['option_3']

    timeout_seconds = 10


class Eye4(Page):
    form_model = models.Player
    form_fields = ['option_4']

    timeout_seconds = 10


class Eye5(Page):
    form_model = models.Player
    form_fields = ['option_5']

    timeout_seconds = 10


class Eye6(Page):
    form_model = models.Player
    form_fields = ['option_6']

    timeout_seconds = 10


class Eye7(Page):
    form_model = models.Player
    form_fields = ['option_7']

    timeout_seconds = 10


class Eye8(Page):
    form_model = models.Player
    form_fields = ['option_8']

    timeout_seconds = 10


class Eye9(Page):
    form_model = models.Player
    form_fields = ['option_9']

    timeout_seconds = 10


class Eye10(Page):
    form_model = models.Player
    form_fields = ['option_10']

    timeout_seconds = 10


class Eye11(Page):
    form_model = models.Player
    form_fields = ['option_11']

    timeout_seconds = 10


class Eye12(Page):
    form_model = models.Player
    form_fields = ['option_12']

    timeout_seconds = 10


class Eye13(Page):
    form_model = models.Player
    form_fields = ['option_13']

    timeout_seconds = 10


class Eye14(Page):
    form_model = models.Player
    form_fields = ['option_14']

    timeout_seconds = 10


class Eye15(Page):
    form_model = models.Player
    form_fields = ['option_15']

    timeout_seconds = 10


class Eye16(Page):
    form_model = models.Player
    form_fields = ['option_16']

    timeout_seconds = 10


class Eye17(Page):
    form_model = models.Player
    form_fields = ['option_17']

    timeout_seconds = 10


class Eye18(Page):
    form_model = models.Player
    form_fields = ['option_18']

    timeout_seconds = 10


class Eye19(Page):
    form_model = models.Player
    form_fields = ['option_19']

    timeout_seconds = 10


class Eye20(Page):
    form_model = models.Player
    form_fields = ['option_20']

    timeout_seconds = 10


class Eye21(Page):
    form_model = models.Player
    form_fields = ['option_21']

    timeout_seconds = 10


class Eye22(Page):
    form_model = models.Player
    form_fields = ['option_22']

    timeout_seconds = 10


class Eye23(Page):
    form_model = models.Player
    form_fields = ['option_23']

    timeout_seconds = 10


class Eye24(Page):
    form_model = models.Player
    form_fields = ['option_24']

    timeout_seconds = 10


class Eye25(Page):
    form_model = models.Player
    form_fields = ['option_25']

    timeout_seconds = 10


class Eye26(Page):
    form_model = models.Player
    form_fields = ['option_26']

    timeout_seconds = 10


class Eye27(Page):
    form_model = models.Player
    form_fields = ['option_27']

    timeout_seconds = 10


class Eye28(Page):
    form_model = models.Player
    form_fields = ['option_28']

    timeout_seconds = 10


class Eye29(Page):
    form_model = models.Player
    form_fields = ['option_29']

    timeout_seconds = 10


class Eye30(Page):
    form_model = models.Player
    form_fields = ['option_30']

    timeout_seconds = 10


class Eye31(Page):
    form_model = models.Player
    form_fields = ['option_31']

    timeout_seconds = 10


class Eye32(Page):
    form_model = models.Player
    form_fields = ['option_32']

    timeout_seconds = 10


class Eye33(Page):
    form_model = models.Player
    form_fields = ['option_33']

    timeout_seconds = 10


class Eye34(Page):
    form_model = models.Player
    form_fields = ['option_34']

    timeout_seconds = 10


class Eye35(Page):
    form_model = models.Player
    form_fields = ['option_35']

    timeout_seconds = 10


class Eye36(Page):
    form_model = models.Player
    form_fields = ['option_36']

    timeout_seconds = 10


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def is_displayed(self):
        return self.player.treatment != 4


class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    players_per_group = 2

    def after_all_players_arrive(self):
        self.group.get_treatment()


class Player1(Page):
    form_model = models.Player
    form_fields = ['Message_12']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.player.treatment != 4

    timeout_seconds = 120
    timeout_submission = {'Message_12': 'Message 1'}


class Player2(Page):
    form_model = models.Player
    form_fields = ['option_AB']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.treatment != 4

    timeout_seconds = 120
    timeout_submission = {'option_AB': 'Option A'}


class treatment_4(Page):
    form_model = models.Player
    form_fields = ['option4_1', 'option4_2']

    def before_next_page(self):
        self.player.payoff = 0.10
        self.player.total = 0.30

    def is_displayed(self):
        return self.player.treatment == 4


class Result_123(Page):

    def vars_for_template(self):
        return {'task2': self.player.payoff - 0.20}


class Demographic(Page):
    form_model = models.Player
    form_fields = ['gender', 'age', 'religion', 'service'] #'getcode_1', 'getcode_2']


class WaitforP1(WaitPage):
    def is_displayed(self):
        return self.player.treatment != 4


class Task3(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2 and self.player.treatment != 4


page_sequence = [
    MyWaitPage,
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
    Player1,
    Task3,
    WaitforP1,
    Player2,
    treatment_4,
    Demographic,
    ResultsWaitPage,
    Result_123
]
