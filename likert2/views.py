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
        self.participant.vars['opinion_%s' % self.round_number] = 'Indifferent'
        self.participant.vars['preference_%s' % self.round_number] = 999



class Likert(Page):
    form_model = models.Player
    form_fields = ['likert']

    def is_displayed(self):
        return self.player.submitted_answer == 'Favor'

    def before_next_page(self):
        self.participant.vars['opinion_%s' % self.round_number] = 'Agree'
        self.participant.vars['preference_%s' % self.round_number] = self.player.likert

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


    def before_next_page(self):
        self.participant.vars['opinion_%s' % self.round_number] = 'Disagree'
        self.participant.vars['preference_%s' % self.round_number] = self.player.likert


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

    def before_next_page(self):
        if self.round_number == 10:
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

        else:
            pass


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

    def is_displayed(self):
        return self.round_number == 10


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

    def is_displayed(self):
        return self.round_number == 10


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

    def is_displayed(self):
        return self.round_number == 10


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

    def is_displayed(self):
        return self.round_number == 10


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

    def is_displayed(self):
        return self.round_number == 10

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

    def is_displayed(self):
        return self.round_number == 10


class Donation(Page):
    form_model = models.Player
    form_fields = ['donation', 'org', 'email']

    def vars_for_template(self):
        # cmiddle = []
        # biglist = []
        # temp = []
        # org = []
        # des = []

        # for i in range(1, 11):
        #     if self.participant.vars['care_%s' % i] == 1:
        #         clot.append([self.participant.vars['care_%s' % i], i])
        #     elif self.participant.vars['care_%s' % i] == 2:
        #         cmiddle.append([self.participant.vars['care_%s' % i], i])
        #     elif self.participant.vars['care_%s' % i] == 3:
        #         clittle.append([self.participant.vars['care_%s' % i], i])
        #     else:
        #         pass

        clot = [self.participant.vars['lot1'], self.participant.vars['lot2'], self.participant.vars['lot3']]
        clittle = [self.participant.vars['little1'], self.participant.vars['little2'], self.participant.vars['little3']]

        # if len(clot) == 0:
        #     if len(cmiddle) == 0 and len(clittle) != 0:
        #         self.player.annotation = 'only group 3'
        #         if len(clittle) <= 3:
        #             temp = random.sample(clittle, len(clittle))
        #         else:
        #             temp = random.sample(clittle, 3)
        #     elif len(cmiddle) != 0 and len(clittle) == 0:
        #         self.player.annotation = 'only group 2'
        #         if len(cmiddle) <= 3:
        #             temp = random.sample(cmiddle, len(cmiddle))
        #         else:
        #             temp = random.sample(cmiddle, 3)
        #     elif len(cmiddle) != 0 and len(clittle) != 0:
        #         self.player.annotation = 'no group 1'
        #         if len(cmiddle)+len(clittle) == 2:
        #             temp += random.sample(cmiddle, 1)
        #             temp += random.sample(clittle, 1)
        #         else:
        #             temp += random.sample(cmiddle, 1)
        #             temp += random.sample(clittle, 1)
        #             temp1 = [i for i in cmiddle if i not in temp]
        #             temp2 = [i for i in clittle if i not in temp]
        #             temp += random.sample(temp1 + temp2, 1)
        #     else:
        #         self.player.annotation = 'random'
        #         for i in range(1, 11):
        #             biglist.append([self.participant.vars['care_%s' % i], i])
        #         temp = random.sample(biglist, 3)
        # else:
        #     if len(cmiddle) == 0 and len(clittle) != 0:
        #         self.player.annotation = 'no group 2'
        #         if len(clittle)+len(clot) == 2:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(clittle, 1)
        #         else:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(clittle, 1)
        #             temp1 = [i for i in clot if i not in temp]
        #             temp2 = [i for i in clittle if i not in temp]
        #             temp += random.sample(temp1 + temp2, 1)
        #     elif len(cmiddle) != 0 and len(clittle) == 0:
        #         self.player.annotation = 'no group 3'
        #         if len(cmiddle)+len(clot) == 2:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(cmiddle, 1)
        #         else:
        #             temp += random.sample(clot, 1)
        #             temp += random.sample(cmiddle, 1)
        #             temp1 = [i for i in cmiddle if i not in temp]
        #             temp2 = [i for i in clot if i not in temp]
        #             temp += random.sample(temp1 + temp2, 1)
        #     elif len(cmiddle) != 0 and len(clittle) != 0:
        #         self.player.annotation = 'all groups'
        #         temp += random.sample(clot, 1)
        #         temp += random.sample(clittle, 1)
        #         temp1 = [i for i in clittle if i not in temp]
        #         temp2 = [i for i in clot if i not in temp]
        #         temp += random.sample(temp1 + temp2, 1)
        #     else:
        #         self.player.annotation = 'only group 1'
        #         if len(clot) <= 3:
        #             temp = random.sample(clot, len(clot))
        #         else:
        #             temp = random.sample(clot, 3)

        # if len(temp) == 1:
        #     self.player.org_option1 = Constants.organization[temp[0][1]]
        #     org.append(self.player.org_option1)
        #     no = ['1']
        #     des.append(Constants.description[temp[0][1]])
        # elif len(temp) == 2:
        #     self.player.org_option1 = Constants.organization[temp[0][1]]
        #     self.player.org_option2 = Constants.organization[temp[1][1]]
        #     org.append(self.player.org_option1)
        #     org.append(self.player.org_option2)
        #     no = ['1', '2']
        #     des.append(Constants.description[temp[0][1]])
        #     des.append(Constants.description[temp[1][1]])
        # else:
        #     self.player.org_option1 = Constants.organization[temp[0][1]]
        #     self.player.org_option2 = Constants.organization[temp[1][1]]
        #     self.player.org_option3 = Constants.organization[temp[2][1]]
        #     org.append(self.player.org_option1)
        #     org.append(self.player.org_option2)
        #     org.append(self.player.org_option3)
        #     no = ['1', '2', '3']
        #     des.append(Constants.description[temp[0][1]])
        #     des.append(Constants.description[temp[1][1]])
        #     des.append(Constants.description[temp[2][1]])

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


    def is_displayed(self):
        return self.round_number == 10 \
               # and (self.participant.vars['group'] == '1LD' or self.participant.vars['group'] == '1QD' or \
               # self.participant.vars['group'] == '1QND' or self.participant.vars['group'] == '2LD' or \
               # self.participant.vars['group'] == '2QD' or self.participant.vars['group'] == '2QND' or \
               # self.participant.vars['group'] == '3LD' or self.participant.vars['group'] == '3QD' or \
               # self.participant.vars['group'] == '3QND')


# class Donation2(Page):
#     form_model = models.Player
#     form_fields = ['email']
#
#     def is_displayed(self):
#         return self.round_number == 10 \
               # and (self.participant.vars['group'] == '1LD' or self.participant.vars['group'] == '1QD' or \
               # self.participant.vars['group'] == '1QND' or self.participant.vars['group'] == '2LD' or \
               # self.participant.vars['group'] == '2QD' or self.participant.vars['group'] == '2QND' or \
               # self.participant.vars['group'] == '3LD' or self.participant.vars['group'] == '3QD' or \
               # self.participant.vars['group'] == '3QND')

page_sequence = [
    MyPage,
    Likert,
    Likert2,
    Important,
    Care1,
    Care1_2,
    Care2,
    Care2_2,
    Care3,
    Care3_2,
    # Donation,
    # Donation2
]
