from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class FirstPage(Page):
    form_model = models.Player
    form_fields = ['number']

    def before_next_page(self):
        for i in range(len(self.session.vars['info'])):
            if str(self.player.number) == self.session.vars['info'][i]['Number']:
                self.player.name = self.session.vars['info'][i]['Name']
                self.player.grade = self.session.vars['info'][i]['Grade']
                self.player.major = self.session.vars['info'][i]['Major']
        self.participant.vars['number'] = self.player.number


class SecondPage(Page):
    pass


class ThirdPage(Page):
    pass


class Introduction(Page):
    pass


class Test(Page):
    form_model = models.Player
    form_fields = ['bankA', 'bankB', 'fluidityA', 'fluidityB', 'utility1', 'utility2',
                   'utility3', 'utility4', 'utility5', 'utility6', 'utility7', 'utility8',
                   'utility9', 'utility10', 'utility11', 'utility12']

    def before_next_page(self):
        answer = [self.player.bankA, self.player.bankB, self.player.fluidityA, self.player.fluidityB, self.player.utility1,
                  self.player.utility2, self.player.utility3, self.player.utility4, self.player.utility5, self.player.utility6,
                  self.player.utility7, self.player.utility8, self.player.utility9, self.player.utility10, self.player.utility11,
                  self.player.utility12]

        correction = [6, 3, '相同', '不确定', 24, 0, 40, 100, 0, 109, 30, 0, 20, 80, 0, 63]

        filtered = filter(lambda x: x[0] == x[1], zip(answer, correction))

        self.player.score = len(list(filtered))


class Introduction2(Page):
    def is_displayed(self):
        return self.player.score != 16


class Test2(Page):
    form_model = models.Player
    form_fields = ['bankA_2', 'bankB_2', 'fluidityA_2', 'fluidityB_2', 'utility1_2', 'utility2_2',
                   'utility3_2', 'utility4_2', 'utility5_2', 'utility6_2', 'utility7_2', 'utility8_2',
                   'utility9_2', 'utility10_2', 'utility11_2', 'utility12_2']

    def before_next_page(self):
        answer = [self.player.bankA_2, self.player.bankB_2, self.player.fluidityA_2, self.player.fluidityB_2, self.player.utility1_2,
                  self.player.utility2_2, self.player.utility3_2, self.player.utility4_2, self.player.utility5_2, self.player.utility6_2,
                  self.player.utility7_2, self.player.utility8_2, self.player.utility9_2, self.player.utility10_2, self.player.utility11_2,
                  self.player.utility12_2]

        correction = [6, 3, '相同', '不确定', 24, 0, 40, 100, 0, 109, 30, 0, 20, 80, 0, 63]

        filtered = filter(lambda x: x[0] == x[1], zip(answer, correction))

        self.player.score_2 = len(list(filtered))

    def is_displayed(self):
        return self.player.score != 16


class ResultsWaitPage(WaitPage):
    pass


class FirstWaitPage(WaitPage):
    pass


page_sequence = [
    FirstWaitPage,
    FirstPage,
    SecondPage,
    ThirdPage,
    # Introduction,
    # Test,
    # Introduction2,
    # Test2,
    ResultsWaitPage,
    # Results
]
