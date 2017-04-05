from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Welcome(Page):
    pass


class Wait(WaitPage):
    group_by_arrival_time = True
    players_per_group = 2

    def after_all_players_arrive(self):
        self.subsession.get_priming()


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




page_sequence = [
    Wait,
    Welcome,
    Priming,
    Introduction,
    # Eye1,
    # Eye2,
    # Eye3,
    # Eye4,
    # Eye5,
    # Eye6,
    # Eye7,
    # Eye8,
    # Eye9,
    # Eye10,
    # Eye11,
    # Eye12,
    # Eye13,
    # Eye14,
    # Eye15,
    # Eye16,
    # Eye17,
    # Eye18,
    # Eye19,
    # Eye20,
    # Eye21,
    # Eye22,
    # Eye23,
    # Eye24,
    # Eye25,
    # Eye26,
    # Eye27,
    # Eye28,
    # Eye29,
    # Eye30,
    # Eye31,
    # Eye32,
    # Eye33,
    # Eye34,
    # Eye35,
    Eye36,
    ResultWait
]
