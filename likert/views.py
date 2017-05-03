from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import csv

class MyPage(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_1']

    def before_next_page(self):
        self.participant.vars['opinion_1'] = 'Indifferent'
        self.participant.vars['preference_1'] = 999



class MyPage2(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_2']

    def before_next_page(self):
        self.participant.vars['opinion_2'] = 'Indifferent'
        self.participant.vars['preference_2'] = 999


class MyPage3(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_3']

    def before_next_page(self):
        self.participant.vars['opinion_3'] = 'Indifferent'
        self.participant.vars['preference_3'] = 999


class MyPage4(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_4']

    def before_next_page(self):
        self.participant.vars['opinion_4'] = 'Indifferent'
        self.participant.vars['preference_4'] = 999


class MyPage5(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_5']

    def before_next_page(self):
        self.participant.vars['opinion_5'] = 'Indifferent'
        self.participant.vars['preference_5'] = 999

class MyPage6(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_6']

    def before_next_page(self):
        self.participant.vars['opinion_6'] = 'Indifferent'
        self.participant.vars['preference_6'] = 999

class MyPage7(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_7']

    def before_next_page(self):
        self.participant.vars['opinion_7'] = 'Indifferent'
        self.participant.vars['preference_7'] = 999

class MyPage8(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_8']

    def before_next_page(self):
        self.participant.vars['opinion_8'] = 'Indifferent'
        self.participant.vars['preference_8'] = 999

class MyPage9(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_9']

    def before_next_page(self):
        self.participant.vars['opinion_9'] = 'Indifferent'
        self.participant.vars['preference_9'] = 999

class MyPage10(Page):
    form_model = models.Player
    form_fields = ['submitted_answer_10']

    def before_next_page(self):
        self.participant.vars['opinion_10'] = 'Indifferent'
        self.participant.vars['preference_10'] = 999


class Likert(Page):
    form_model = models.Player
    form_fields = ['likert_1']

    def is_displayed(self):
        return self.player.submitted_answer_1 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_1'] = 'Agree'
        self.participant.vars['preference_1'] = self.player.likert_1

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


class Likertt(Page):
    form_model = models.Player
    form_fields = ['likert_1']

    def is_displayed(self):
        return self.player.submitted_answer_1 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_1'] = 'Disagree'
        self.participant.vars['preference_1'] = self.player.likert_1


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
    form_fields = ['likert_2']

    def is_displayed(self):
        return self.player.submitted_answer_2 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_2'] = 'Agree'
        self.participant.vars['preference_2'] = self.player.likert_2

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



class Likertt2(Page):
    form_model = models.Player
    form_fields = ['likert_2']

    def is_displayed(self):
        return self.player.submitted_answer_2 == 'Oppose'

    def before_next_page(self):
        self.participant.vars['opinion_2'] = 'Disagree'
        self.participant.vars['preference_2'] = self.player.likert_2


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

class Likert3(Page):
    form_model = models.Player
    form_fields = ['likert_3']

    def is_displayed(self):
        return self.player.submitted_answer_3 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_3'] = 'Agree'
        self.participant.vars['preference_3'] = self.player.likert_3

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



class Likertt3(Page):
    form_model = models.Player
    form_fields = ['likert_3']

    def is_displayed(self):
        return self.player.submitted_answer_3 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_3'] = 'Disagree'
        self.participant.vars['preference_3'] = self.player.likert_3


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

class Likert4(Page):
    form_model = models.Player
    form_fields = ['likert_4']

    def is_displayed(self):
        return self.player.submitted_answer_4 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_4'] = 'Agree'
        self.participant.vars['preference_4'] = self.player.likert_4

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


class Likertt4(Page):
    form_model = models.Player
    form_fields = ['likert_4']

    def is_displayed(self):
        return self.player.submitted_answer_4 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_4'] = 'Disagree'
        self.participant.vars['preference_4'] = self.player.likert_4


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


class Likert5(Page):
    form_model = models.Player
    form_fields = ['likert_5']

    def is_displayed(self):
        return self.player.submitted_answer_5 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_5'] = 'Agree'
        self.participant.vars['preference_5'] = self.player.likert_5

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


class Likertt5(Page):
    form_model = models.Player
    form_fields = ['likert_5']

    def is_displayed(self):
        return self.player.submitted_answer_5 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_5'] = 'Disagree'
        self.participant.vars['preference_5'] = self.player.likert_5


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


class Likert6(Page):
    form_model = models.Player
    form_fields = ['likert_6']

    def is_displayed(self):
        return self.player.submitted_answer_6 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_6'] = 'Agree'
        self.participant.vars['preference_6'] = self.player.likert_6

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


class Likertt6(Page):
    form_model = models.Player
    form_fields = ['likert_6']

    def is_displayed(self):
        return self.player.submitted_answer_6 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_6'] = 'Disagree'
        self.participant.vars['preference_6'] = self.player.likert_6


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


class Likert7(Page):
    form_model = models.Player
    form_fields = ['likert_7']

    def is_displayed(self):
        return self.player.submitted_answer_7 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_7'] = 'Agree'
        self.participant.vars['preference_7'] = self.player.likert_7

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


class Likertt7(Page):
    form_model = models.Player
    form_fields = ['likert_7']

    def is_displayed(self):
        return self.player.submitted_answer_7 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_7'] = 'Disagree'
        self.participant.vars['preference_7'] = self.player.likert_7


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


class Likert8(Page):
    form_model = models.Player
    form_fields = ['likert_8']

    def is_displayed(self):
        return self.player.submitted_answer_8 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_8'] = 'Agree'
        self.participant.vars['preference_8'] = self.player.likert_8

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


class Likertt8(Page):
    form_model = models.Player
    form_fields = ['likert_8']

    def is_displayed(self):
        return self.player.submitted_answer_8 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_8'] = 'Disagree'
        self.participant.vars['preference_8'] = self.player.likert_8


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


class Likert9(Page):
    form_model = models.Player
    form_fields = ['likert_9']

    def is_displayed(self):
        return self.player.submitted_answer_9 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_9'] = 'Agree'
        self.participant.vars['preference_9'] = self.player.likert_9

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


class Likertt9(Page):
    form_model = models.Player
    form_fields = ['likert_9']

    def is_displayed(self):
        return self.player.submitted_answer_9 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_9'] = 'Disagree'
        self.participant.vars['preference_9'] = self.player.likert_9


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


class Likert10(Page):
    form_model = models.Player
    form_fields = ['likert_10']

    def is_displayed(self):
        return self.player.submitted_answer_10 == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_10'] = 'Agree'
        self.participant.vars['preference_10'] = self.player.likert_10

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


class Likertt10(Page):
    form_model = models.Player
    form_fields = ['likert_10']

    def is_displayed(self):
        return self.player.submitted_answer_10 == 'Oppose'


    def before_next_page(self):
        self.participant.vars['opinion_10'] = 'Disagree'
        self.participant.vars['preference_10'] = self.player.likert_10


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


class Important(Page):
    form_model = models.Player
    form_fields = ['important_1']

    def vars_for_template(self):
        list1 = ['Extremely important', 'Very important', 'Somewhat important', 'Not too important',
                 'Not important at all']
        value1 = [1, 2, 3, 4, 5]
        list2 = ['Not important at all', 'Not too important', 'Somewhat important', 'Very important',
                 'Extremely important']
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


class Important2(Page):
    form_model = models.Player
    form_fields = ['important_2']

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


class Important3(Page):
    form_model = models.Player
    form_fields = ['important_3']

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



class Important4(Page):
    form_model = models.Player
    form_fields = ['important_4']

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


class Important5(Page):
    form_model = models.Player
    form_fields = ['important_5']

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


class Important6(Page):
    form_model = models.Player
    form_fields = ['important_6']

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


class Important7(Page):
    form_model = models.Player
    form_fields = ['important_7']

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


class Important8(Page):
    form_model = models.Player
    form_fields = ['important_8']

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


class Important9(Page):
    form_model = models.Player
    form_fields = ['important_9']

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



class Important10(Page):
    form_model = models.Player
    form_fields = ['important_10']

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

    def before_next_page(self):
        preference_list = []
        preference_3 = []
        preference_2 = []
        preference_1 = []
        for i in range(1, 11):
            preference_list.append(self.participant.vars['preference_%s' % i])
        for i, item in enumerate(preference_list):
            if item == 3:
                preference_3.append(i+1)
            elif item == 2:
                preference_2.append(i+1)
            elif item == 1:
                preference_1.append(i+1)
            else:
                pass

        if len(preference_1) != 0:
            self.participant.vars['issue'] = random.choice(preference_1)  # number of issue
            self.participant.vars['important'] = 'a great deal'
        else:
            if len(preference_2) != 0:
                self.participant.vars['issue'] = random.choice(preference_2)
                self.participant.vars['important'] = 'a moderate amount'
            else:
                if len(preference_3) != 0:
                    self.participant.vars['issue'] = random.choice(preference_3)
                    self.participant.vars['important'] = 'a little'
                else:
                    self.participant.vars['issue'] = 999



class Care1(Page):
    form_model = models.Player
    form_fields = ['care1f']

    def care1f_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        random.shuffle(list_question)
        return list_question



class Care1_2(Page):
    form_model = models.Player
    form_fields = ['care1o']

    def care1o_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1]]

        # list_new = list(set(list_question)-set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)
        return list_new


class Care2(Page):
    form_model = models.Player
    form_fields = ['care2f']

    def care2f_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1]]

        # list_new = list(set(list_question)-set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new



class Care2_2(Page):
    form_model = models.Player
    form_fields = ['care2o']

    def care2o_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1]]

        # list_new = list(set(list_question)-set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new



class Care3(Page):
    form_model = models.Player
    form_fields = ['care3f']

    def care3f_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1], list_question[int(self.player.care2o) - 1]]

        # list_new = list(set(list_question) - set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new


class Care3_2(Page):
    form_model = models.Player
    form_fields = ['care3o']

    def care3o_choices(self):
        list_question = [[1, 'Reduce the difference in income'],
                         [2, 'Pay women and men the same amount for the same work'],
                         [3, 'Limit imports'],
                         [4, 'Increase number of black students at universities'],
                         [5, 'Paid leave for parents of new children'],
                         [6, 'Build a wall on the US-Mexico border'],
                         [7, 'Change access to citizenship for children of illegal immigrants'],
                         [8, 'The death penalty for murder'],
                         [9, 'Protect gays and lesbians against job discrimination'],
                         [10, 'Send troops to fight ISIS']]

        # list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1], list_question[int(self.player.care2o) - 1],
                     list_question[int(self.player.care3f) - 1]]

        # list_new = list(set(list_question) - set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new

    def before_next_page(self):
        self.participant.vars['lot1'] = self.player.care1f
        self.participant.vars['lot2'] = self.player.care2f
        self.participant.vars['lot3'] = self.player.care3f
        self.participant.vars['little1'] = self.player.care1o
        self.participant.vars['little2'] = self.player.care2o
        self.participant.vars['little3'] = self.player.care3o



class Donation(Page):
    form_model = models.Player
    form_fields = ['donation', 'org', 'email']

    def vars_for_template(self):

        clot = [self.participant.vars['lot1'], self.participant.vars['lot2'], self.participant.vars['lot3']]
        clittle = [self.participant.vars['little1'], self.participant.vars['little2'], self.participant.vars['little3']]


        temp1 = random.choice(clot)
        temp2 = random.choice(clittle)
        temp3 = [i for i in clot if i != temp1]
        temp4 = [i for i in clittle if i != temp2]
        temp5 = random.choice(temp3 + temp4)
        if temp5 in clot:
            self.player.annotation = '2 lot'
        else:
            self.player.annotation = '2 little'

        org = [Constants.organization[temp1-1], Constants.organization[temp2-1], Constants.organization[temp5-1]]
        des = [Constants.description[temp1-1], Constants.description[temp2-1], Constants.description[temp5-1]]
        no = ['1', '2', '3']

        self.player.org_option1 = Constants.organization[temp1-1]
        self.player.org_option2 = Constants.organization[temp2-1]
        self.player.org_option3 = Constants.organization[temp5-1]

        mylist = zip(org, des, no)

        return {'list': mylist}


    # def is_displayed(self):
    #     return
               # (self.participant.vars['group'] == '1LD' or self.participant.vars['group'] == '1QD' or \
               # self.participant.vars['group'] == '1QND' or self.participant.vars['group'] == '2LD' or \
               # self.participant.vars['group'] == '2QD' or self.participant.vars['group'] == '2QND' or \
               # self.participant.vars['group'] == '3LD' or self.participant.vars['group'] == '3QD' or \
               # self.participant.vars['group'] == '3QND')


# class Donation2(Page):
#     form_model = models.Player
#     form_fields = ['email']
#
#     def is_displayed(self):
#         return
               # (self.participant.vars['group'] == '1LD' or self.participant.vars['group'] == '1QD' or \
               # self.participant.vars['group'] == '1QND' or self.participant.vars['group'] == '2LD' or \
               # self.participant.vars['group'] == '2QD' or self.participant.vars['group'] == '2QND' or \
               # self.participant.vars['group'] == '3LD' or self.participant.vars['group'] == '3QD' or \
               # self.participant.vars['group'] == '3QND')


class MyPageinfo(Page):
    form_model = models.Player
    form_fields = ['info1', 'info2', 'info3', 'info4', 'info5', 'info6', 'info7', 'info8', 'info9', 'info10', 'email_info']

    def vars_for_template(self):
        question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
                    'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                    'Change access to citizenship for children of illegal immigrants',
                    'Build a wall on the US-Mexico border',
                    'Paid leave for parents of new children', 'Increase number of black students at universities',
                    'Pay women and men the same amount for the same work']

        info = ['info1', 'info2', 'info3', 'info4', 'info5', 'info6', 'info7', 'info8', 'info9', 'info10']

        mylist = zip(question, info)

        return {'list': mylist}

    def is_displayed(self):
        return self.participant.vars['group'] == '1LI' or self.participant.vars['group'] == '1QI' or \
               self.participant.vars['group'] == '1QNI' or self.participant.vars['group'] == '2LI' or \
               self.participant.vars['group'] == '2QI' or self.participant.vars['group'] == '2QNI' or \
               self.participant.vars['group'] == '3LI' or self.participant.vars['group'] == '3QI' or \
               self.participant.vars['group'] == '3QNI'


class MyPagepetition(Page):
    form_model = models.Player
    form_fields = ['petition_1', 'petition_2', 'petition_3', 'petition_4', 'petition_5', 'petition_6', 'petition_7',
                        'petition_8', 'petition_9', 'petition_10']

    def vars_for_template(self):
        question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
                    'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                    'Change access to citizenship for children of illegal immigrants',
                    'Build a wall on the US-Mexico border',
                    'Paid leave for parents of new children', 'Increase number of black students at universities',
                    'Pay women and men the same amount for the same work']
        attitude = []
        for i in range(1, 11):
            attitude.append(self.participant.vars['opinion_%s' % i])

        petitionlist = ['petition_1', 'petition_2', 'petition_3', 'petition_4', 'petition_5', 'petition_6', 'petition_7',
                        'petition_8', 'petition_9', 'petition_10']

        mylist = zip(question, attitude, petitionlist)

        return {'list': mylist}

    def is_displayed(self):
        return self.participant.vars['group'] == '1LP' or self.participant.vars['group'] == '1QP' or \
               self.participant.vars['group'] == '1QNP' or self.participant.vars['group'] == '2LP' or \
               self.participant.vars['group'] == '2QP' or self.participant.vars['group'] == '2QNP' or \
               self.participant.vars['group'] == '3LP' or self.participant.vars['group'] == '3QP' or \
               self.participant.vars['group'] == '3QNP'

class Resultspetition(Page):
    def vars_for_template(self):
        question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
                    'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                    'Change access to citizenship for children of illegal immigrants',
                    'Build a wall on the US-Mexico border',
                    'Paid leave for parents of new children', 'Increase number of black students at universities',
                    'Pay women and men the same amount for the same work']

        link = ['https://talkpoverty.org/2015/06/10/solutions-economic-inequality/',
                'http://www.commercialdiplomacy.org/cd_dictionary/dictionary_legislation.htm',
                'http://www.cbsnews.com/isis/',
                'http://www.bbc.com/capital/story/20130617-are-gay-employees-protected',
                'https://deathpenaltyinfo.org/crimes-punishable-death-penalty',
                'http://cis.org/birthright-citizenship',
                'http://www.dailynews.com/social-affairs/20170205/building-trumps-wall-6-things-to-know-about-the-us-mexico-border',
                'http://edition.cnn.com/2015/10/29/health/paid-leave-benefits-to-children-research/',
                'https://nces.ed.gov/fastfacts/display.asp?id=667',
                'http://www.aauw.org/research/the-simple-truth-about-the-gender-pay-gap/']

        temp = [self.player.petition_1, self.player.petition_2, self.player.petition_3, self.player.petition_4,
                self.player.petition_5, self.player.petition_6, self.player.petition_7, self.player.petition_8,
                self.player.petition_9, self.player.petition_10]
        temp_l = []
        temp_q = []

        for i, item in enumerate(temp):
            if item == 'True':
                temp_q.append(question[i])
                temp_l.append(link[i])
            else:
                pass

        mylist = zip(temp_q, temp_l)

        return {'list': mylist}

    def is_displayed(self):
        return self.participant.vars['group'] == '1LP' or self.participant.vars['group'] == '1QP' or \
               self.participant.vars['group'] == '1QNP' or self.participant.vars['group'] == '2LP' or \
               self.participant.vars['group'] == '2QP' or self.participant.vars['group'] == '2QNP' or \
               self.participant.vars['group'] == '3LP' or self.participant.vars['group'] == '3QP' or \
               self.participant.vars['group'] == '3QNP'

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



class Partisanship1(Page):
    form_model = models.Player
    form_fields = ['partisanship1']

    def vars_for_template(self):
        ans = ['DEMOCRAT', 'REPUBLICAN']
        random.shuffle(ans)
        p1 = ans[0]
        p2 = ans[1]
        return {'partisanship1': p1,
                'partisanship2': p2}

    # def before_next_page(self):
    #     if self.player.partisanship1 == 1:
    #         self.participant.vars['partisanship'] = 'Democrat'
    #     elif self.player.partisanship1 == 2:
    #         self.participant.vars['partisanship'] = 'Republican'
    #     else:
    #         pass


class Partisanship2(Page):
    form_model = models.Player
    form_fields = ['partisanship2']

    def vars_for_template(self):
        if self.player.partisanship1 == 1:
            par = 'Democrat'
        else:
            par = 'Republican'

        return {'partisanship': par}

    def is_displayed(self):
        return self.player.partisanship1 == 1 or self.player.partisanship1 == 2


class Partisanship3(Page):
    form_model = models.Player
    form_fields = ['partisanship3']

    def vars_for_template(self):
        ans = ['Democratic', 'Republican']
        random.shuffle(ans)
        p1 = ans[0]
        p2 = ans[1]
        return {'par1': p1,
                'par2': p2}

    def is_displayed(self):
        return self.player.partisanship1 == 3 or self.player.partisanship1 == 5 or self.player.partisanship1 == 8

    def before_next_page(self):
        # if self.player.partisanship3 == 1:
        #     self.participant.vars['partisanship'] = 'Closer to Republican Party'
        # elif self.player.partisanship3 == 2:
        #     self.participant.vars['partisanship'] = 'Closer to Democratic Party'
        # else:
        #     self.participant.vars['partisanship'] = 'Independent'

        row = [self.player.id_in_subsession, self.player.submitted_answer_1, self.player.likert_1,
               self.player.submitted_answer_2, self.player.likert_2, self.player.submitted_answer_3,
               self.player.likert_3, self.player.submitted_answer_4, self.player.likert_4,
               self.player.submitted_answer_5, self.player.likert_5, self.player.submitted_answer_6,
               self.player.likert_6, self.player.submitted_answer_7, self.player.likert_7,
               self.player.submitted_answer_8, self.player.likert_8, self.player.submitted_answer_9,
               self.player.likert_9, self.player.submitted_answer_10, self.player.likert_10,
               self.player.org_option1, self.player.org_option2, self.player.org_option3, self.player.org,
               self.player.partisanship1, self.player.partisanship2, self.player.partisanship3]

        with open('data.csv', 'a+') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(row)


class MyPagetrust(Page):
    form_model = models.Player
    form_fields = ['partner']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children',
                  'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants',
                  'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination',
                  'Send troops to fight ISIS']

        issue = issues[self.participant.vars['issue'] - 1]
        level = self.participant.vars['important']
        if self.participant.vars['opinion_%s' % self.participant.vars['issue']] == 'Disagree':
            opinion = 'oppose'
        else:  #不可能有indifferent的情况
            opinion = 'favor'
        direction = self.player.preference_party

        return {'issue': issue,
                'level': level,
                'direction': direction,
                'opinion': opinion}

    def partner_choices(self):
        if self.player.preference_party == 'same':
            mylist = [[3, 'I play trust game against someone who reports same preference on this issue'],
                      [4, 'I play trust game against someone who reports being the same party']]
        else:
            mylist = [[1, 'I play trust game against someone who reports opposite preference on this issue'],
                      [2, 'I play trust game against someone who reports being the opposite party']]
        return mylist

    def is_displayed(self):
        return self.participant.vars['issue'] != 999




class MyPagetrust2(Page):
    form_model = models.Player
    form_fields = ['partner']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children',
                  'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants',
                  'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination',
                  'Send troops to fight ISIS']

        self.participant.vars['issue2'] = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        issue = issues[self.participant.vars['issue2'] - 1]
        direction = self.player.preference_party
        if direction == 'same':
            same_different = 'same'
        else:
            same_different = 'different'

        return {'issue': issue,
                'direction': direction,
                'same_different': same_different}


    def partner_choices(self):
        if self.player.preference_party == 'same':
            mylist = [[3, 'I play trust game against someone who reports same opinion on this issue'],
                      [4, 'I play trust game against someone who reports being the same party']]
        else:
            mylist = [[1, 'I play trust game against someone who reports different opinion on this issue'],
                      [2, 'I play trust game against someone who reports being the opposite party']]

        return mylist

    def is_displayed(self):
        return self.participant.vars['issue'] == 999


class Donation_party(Page):
    form_model = models.Player
    form_fields = ['donation_party']

    def before_next_page(self):
        if self.player.donation_party == 2:
            if self.player.partner == 1 or self.player.partner == 3:
                if self.participant.vars['issue'] != 999:
                    num = self.participant.vars['issue']
                    self_preference = self.participant.vars['preference_%s' % num]
                    direction = self.player.preference_party
                    if direction == 'same':
                        preference = self_preference
                    else:
                        if self_preference == 1:
                            preference = 3
                        elif self_preference == 2:
                            preference = random.choice([1, 3])
                        elif self_preference == 3:
                            preference = 1
                        else:
                            preference = random.randint(1, 3)

                    with open('likert/data.csv') as f:
                        all_objects = list(csv.DictReader(f))

                    dona_1 = []
                    dona_2 = []
                    dona_3 = []
                    dona_correct=[]
                    for i in range(len(all_objects)):
                        if all_objects[i]['opinion_%s' % num] == preference:
                            if all_objects[i]['donation_1'] != '':
                                dona_1.append(all_objects[i]['donation_1'])
                                dona_2.append(all_objects[i]['donation_2'])
                                dona_3.append(all_objects[i]['donation_3'])
                                dona_correct.append(all_objects[i]['donation_correct'])
                            else:
                                pass
                        else:
                            pass

                    if len(dona_1) == 0:
                        self.player.if_random = 1
                        self.player.donation1 = random.choice(Constants.organization)
                        list_temp_1 = [self.player.donation1]
                        list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                        self.player.donation2 = random.choice(list_new_1)
                        list_temp_2 = [self.player.donation1, self.player.donation2]
                        list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                        self.player.donation3 = random.choice(list_new_2)
                        self.player.donation_correct = 'None'
                        for i in range(10):
                            if Constants.organization[i] == self.player.donation1:
                                numb1 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb2 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb3 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb1]
                        self.player.description2 = Constants.description[numb2]
                        self.player.description3 = Constants.description[numb3]
                    else:
                        self.player.if_random = 0
                        self.player.donation1 = random.choice(dona_1)
                        for i in range(len(dona_1)):
                            if dona_1[i] == self.player.donation1:
                                numb4 = i
                        self.player.donation2 = dona_2[numb4]
                        self.player.donation3 = dona_3[numb4]
                        self.player.donation_correct = dona_correct[numb4]
                        for i in range(10):
                            if Constants.organization[i] == self.player.donation1:
                                numb5 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb6 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb7 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb5]
                        self.player.description2 = Constants.description[numb6]
                        self.player.description3 = Constants.description[numb7]

                else:
                    self.player.if_random = 1
                    self.player.donation1 = random.choice(Constants.organization)
                    list_temp_1 = [self.player.donation1]
                    list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                    self.player.donation2 = random.choice(list_new_1)
                    list_temp_2 = [self.player.donation1, self.player.donation2]
                    list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                    self.player.donation3 = random.choice(list_new_2)
                    self.player.donation_correct = 'None'
                    for i in range(10):
                        if Constants.organization[i] == self.player.donation1:
                            numb8 = i
                        elif Constants.organization[i] == self.player.donation2:
                            numb9 = i
                        elif Constants.organization[i] == self.player.donation3:
                            numb10 = i
                        else:
                            pass
                    self.player.description1 = Constants.description[numb8]
                    self.player.description2 = Constants.description[numb9]
                    self.player.description3 = Constants.description[numb10]
            else:
                if self.player.preference_party == 'same':
                    party1 = self.player.partisanship1
                    party2 = self.player.partisanship2
                    party3 = self.player.partisanship3
                else:
                    if self.player.partisanship1 == 1:
                        party1 = 2
                        if self.player.partisanship2 == 1:
                            party2 = 1
                        elif self.player.partisanship2 == 2:
                            party2 = 2
                        else:
                            party2 = 999
                    elif self.player.partisanship1 == 2:
                        party1 = 1
                        if self.player.partisanship2 == 1:
                            party2 = 1
                        elif self.player.partisanship2 == 2:
                            party2 = 2
                        else:
                            party2 = 999
                    else:
                        party1 = 999
                        if self.player.partisanship3 == 1:
                            party3 = 2
                        elif self.player.partisanship3 == 2:
                            party3 = 1
                        else:
                            party3 = 999

# 现在有一些疑问，第一，partisanship放在哪里合适，第二，如果这个player是中立的，那么选择和同一党派的人玩猜党派的游戏该怎么办。

        else:
            # 玩家选择猜相反的情况
            # if self.player.partisanship1 == 1:
            #     party1 = 2
            #     if self.player.partisanship2 == 1:
            #         party2 = 1
            #     elif self.player.partisanship2 == 2:
            #         party2 = 2
            #     else:
            #         party2 = 999
            # elif self.player.partisanship1 == 2:
            #     party1 = 1
            #     if self.player.partisanship2 == 1:
            #         party2 = 1
            #     elif self.player.partisanship2 == 2:
            #         party2 = 2
            #     else:
            #         party2 = 999
            # else:
            #     party1 = 999
            #     if self.player.partisanship3 == 1:
            #         party3 = 2
            #     elif self.player.partisanship3 == 2:
            #         party3 = 1
            #     else:
            #         party3 = 999
            #
            # with open('likert/data.csv') as f:
            #     all_objects = list(csv.DictReader(f))
            #
            # if self.player.preference_party == 'same':
            #
            #
            # party_1 = []
            # party_2 = []
            # party_3 = []
            # if party1 == 999:
            #     if party3 == 999:
            #         for i in range(len(all_objects)):
            #             if all_objects[i]['partisanship_1'] == 5 or all_objects[i]['partisanship_1'] == 8:
            #                 if all_objects[i]['partisanship_3'] == 3:
            #
            #
            #
            #
            # if len(party_1) != 0:
            #     real_party_1 = random.choice(party_1)
            #     for i in range(len(party_1)):
            #         if party_1[i] == real_party_1:
            #             num11 = i
            #         else:
            #             pass
            #     real_party_2 = party_2[num11]
            #     real_party_3 = party_3[num11]
            # else:
            #     real_party_1 = random.choice()
            pass



class Donation_trust(Page):
    form_model = models.Player
    form_fields = ['donation_choice']

    def is_displayed(self):
        return self.player.donation_party == 2


class Party_trust(Page):
    def is_displayed(self):
        return self.player.donation_party == 1



class End(Page):
    pass


page_sequence = [
    MyPage,
    Likert,
    Likertt,
    Important,
    MyPage2,
    Likert2,
    Likertt2,
    Important2,
    MyPage3,
    Likert3,
    Likertt3,
    Important3,
    MyPage4,
    Likert4,
    Likertt4,
    Important4,
    MyPage5,
    Likert5,
    Likertt5,
    Important5,
    MyPage6,
    Likert6,
    Likertt6,
    Important6,
    MyPage7,
    Likert7,
    Likertt7,
    Important7,
    MyPage8,
    Likert8,
    Likertt8,
    Important8,
    MyPage9,
    Likert9,
    Likertt9,
    Important9,
    MyPage10,
    Likert10,
    Likertt10,
    Important10,
    Care1,
    Care1_2,
    Care2,
    Care2_2,
    Care3,
    Care3_2,
    Partisanship1,
    Partisanship2,
    Partisanship3,
    Donation,
    MyPagetrust,
    MyPagetrust2,
    Donation_party,
    MyPageinfo,
    MyPagepetition,
    Resultspetition,
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
    Q13,
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
