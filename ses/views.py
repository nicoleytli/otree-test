from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random




class Demographic(Page):
    form_model = models.Player
    form_fields = ['birth', 'educ', 'dip', 'duty', 'emptype', 'work']


class Demographic2(Page):
    form_model = models.Player
    form_fields = ['myclass']


class Demo3(Page):
    form_model = models.Player
    form_fields = ['whichclass']

    def is_displayed(self):
        return self.player.myclass == 1


class Demo4(Page):
    form_model = models.Player
    form_fields = ['chclass']

    def is_displayed(self):
        return self.player.myclass == 2


class Demo5(Page):
    form_model = models.Player
    form_fields = ['middle']

    def is_displayed(self):
        return self.player.whichclass == 2 or self.player.chclass == 1


class Demo6(Page):
    form_model = models.Player
    form_fields = ['working']

    def is_displayed(self):
        return self.player.whichclass == 3 or self.player.chclass == 2


class End(Page):
    pass


# class Partisanship1(Page):
#     form_model = models.Player
#     form_fields = ['partisanship1']
#
#     def vars_for_template(self):
#         ans = ['DEMOCRAT', 'REPUBLICAN']
#         random.shuffle(ans)
#         p1 = ans[0]
#         p2 = ans[1]
#         return {'partisanship1': p1,
#                 'partisanship2': p2}
#
#     def before_next_page(self):
#         if self.player.partisanship1 == 1:
#             self.participant.vars['partisanship'] = 'Democrat'
#         elif self.player.partisanship1 == 2:
#             self.participant.vars['partisanship'] = 'Republican'
#         else:
#             pass
#
#
# class Partisanship2(Page):
#     form_model = models.Player
#     form_fields = ['partisanship2']
#
#     def vars_for_template(self):
#         if self.player.partisanship1 == 1:
#             par = 'Democrat'
#         else:
#             par = 'Republican'
#
#         return {'partisanship': par}
#
#     def is_displayed(self):
#         return self.player.partisanship1 == 1 or self.player.partisanship1 == 2
#
#
# class Partisanship3(Page):
#     form_model = models.Player
#     form_fields = ['partisanship3']
#
#     def vars_for_template(self):
#         ans = ['Democratic', 'Republican']
#         random.shuffle(ans)
#         p1 = ans[0]
#         p2 = ans[1]
#         return {'par1': p1,
#                 'par2': p2}
#
#     def is_displayed(self):
#         return self.player.partisanship1 == 3 or self.player.partisanship1 == 5 or self.player.partisanship1 == 8
#
#     def before_next_page(self):
#         if self.player.partisanship3 == 1:
#             self.participant.vars['partisanship'] = 'Closer to Republican Party'
#         elif self.player.partisanship3 == 2:
#             self.participant.vars['partisanship'] = 'Closer to Democratic Party'
#         else:
#             self.participant.vars['partisanship'] = 'Independent'

page_sequence = [
    Demographic,
    Demographic2,
    Demo3,
    Demo4,
    Demo5,
    Demo6,
    # Partisanship1,
    # Partisanship2,
    # Partisanship3,
    End
]
