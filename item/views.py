from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Q1(Page):
    form_model = models.Player
    form_fields = ['Q1']


class Q2(Page):
    form_model = models.Player
    form_fields = ['Q2']

    def is_displayed(self):
        return self.player.Q1 == 1


class Q3(Page):
    form_model = models.Player
    form_fields = ['Q3']

    def Q3_choices(self):
        if self.player.Q2 == 1:
            ans1 = 'I voted to express my support for Hillary Clinton and her policies'
            ans2 = 'I voted to express my opposition to Trump and his policies'
        elif self.player.Q2 == 2:
            ans1 = 'I voted to express my support for Donald Trump and his policies'
            ans2 = 'I voted to express my opposition to Hillary Clinton and her policies'
        return [[1, ans1],
                [2, ans2]]

    def is_displayed(self):
        return self.player.Q2 != 3 and self.player.Q1 == 1


class Q4(Page):
    form_model = models.Player
    form_fields = ['Q4']


class Q41(Page):
    form_model = models.Player
    form_fields = ['Q4_2']

    def is_displayed(self):
        return self.player.Q4 == 1


class Q42(Page):
    form_model = models.Player
    form_fields = ['Q4_3']

    def is_displayed(self):
        return self.player.Q4_2 == 3 and self.player.Q4 == 1


class Q5(Page):
    form_model = models.Player
    form_fields = ['Q5']


class Q6(Page):
    form_model = models.Player
    form_fields = ['Q6']

    def is_displayed(self):
        return self.player.Q5 == 99 or self.player.Q5 == 4


class Q7(Page):
    form_model = models.Player
    form_fields = ['Q7']


class Q8(Page):
    form_model = models.Player
    form_fields = ['Q8']


class Q9(Page):
    form_model = models.Player
    form_fields = ['Q9']


class Q10(Page):
    form_model = models.Player
    form_fields = ['Q10']


class Q11(Page):
    form_model = models.Player
    form_fields = ['Q11']


class Q12(Page):
    form_model = models.Player
    form_fields = ['Q12']


class Q13(Page):
    form_model = models.Player
    form_fields = ['Q13']


page_sequence = [
    Q1,
    Q2,
    Q3,
    Q4,
    Q41,
    Q42,
    Q5,
    Q6,
    Q7,
    Q8,
    Q9,
    Q10,
    Q11,
    Q12,
    Q13
]
