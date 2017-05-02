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

    # def likert_choices(self):
    #     my_list = [[1, 'a great deal'], [3, 'a little']]
    #     random.shuffle(my_list)
    #     ur_list = [2, 'a moderate amount']
    #     return [my_list[0], ur_list, my_list[1]]

    def before_next_page(self):
        self.participant.vars['opinion_%s' % self.round_number] = 'Agree'

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert


class Likert2(Page):
    form_model = models.Player
    form_fields = ['likert']

    def is_displayed(self):
        return self.player.submitted_answer == 'Oppose'

    # def likert_choices(self):
    #     my_list = [[1, 'a great deal'], [3, 'a little']]
    #     random.shuffle(my_list)
    #     ur_list = [2, 'a moderate amount']
    #     return [my_list[0], ur_list, my_list[1]]

    def before_next_page(self):
        self.participant.vars['opinion_%s' % self.round_number] = 'Disagree'

    def vars_for_template(self):
        list1 = ['a great deal', 'a moderate amount', 'a little']
        value1 = [1, 2, 3]
        list2 = ['a little', 'a moderate amount', 'a great deal']
        value2 = [3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

    # def before_next_page(self):
    #     self.participant.vars['care_%s' % self.round_number] = self.player.likert
    #     self.player.cares = self.player.likert

class Important(Page):
    form_model = models.Player
    form_fields = ['important']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important', 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important', 'Extremely important']
        value2 = [5, 4, 3, 2, 1]

        choose = random.randint(1, 2)
        if choose == 1:
            mylist = list1
            myvalue = value1
        else:
            mylist = list2
            myvalue = value2

        return {
            'names': mylist,
            'values': myvalue,
        }

page_sequence = [
    MyPage,
    Likert,
    Likert2,
    Important
]
