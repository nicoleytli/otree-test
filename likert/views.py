from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    form_model = models.Player
    form_fields = ['submitted_answer']

    def submitted_answer_choices(self):
        qd = self.player.current_question()
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
        ]

    def before_next_page(self):
    #     self.player.care()
        self.player.opinion()



class Likert(Page):
    form_model = models.Player
    form_fields = ['likert']

    def is_displayed(self):
        return self.player.submitted_answer == 'Favor'

    def likert_choices(self):
        my_list = [[1, 'a great deal'], [3, 'a little']]
        random.shuffle(my_list)
        ur_list = [2, 'a moderate amount']
        return [my_list[0], ur_list, my_list[1]]

    def before_next_page(self):
        self.participant.vars['opinion_%s' % self.round_number] = 'Agree'

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likert2(Page):
    form_model = models.Player
    form_fields = ['likert']

    def is_displayed(self):
        return self.player.submitted_answer == 'Oppose'

    def likert_choices(self):
        my_list = [[1, 'a great deal'], [3, 'a little']]
        random.shuffle(my_list)
        ur_list = [2, 'a moderate amount']
        return [my_list[0], ur_list, my_list[1]]

    def before_next_page(self):
        self.participant.vars['opinion_%s' % self.round_number] = 'Disagree'

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


page_sequence = [
    MyPage,
    Likert,
    Likert2
]
