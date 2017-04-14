from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


class Care1(Page):
    form_model = models.Player
    form_fields = ['care1f', 'care1o']

    def care1f_choices(self):
        list_question = [[1, 'Reduce the difference in income'], [2, 'limit imports'], [3, 'Send troops to fight ISIS'],
                         [4, 'Protect gays and lesbians against job discrimination'], [5, 'The death penalty for murder'],
                         [6, 'Change access to citizenship for children of illegal immigrants'], [7, 'Build a wall on the US-Mexico border'],
                         [8, 'Paid leave for parents of new children'], [9, 'Increase number of black students at universities'],
                         [10, 'Pay women and men the same amount for the same work']]
        random.shuffle(list_question)
        return list_question

    def care1o_choices(self):
        list_question = [[1, 'Reduce the difference in income'], [2, 'limit imports'], [3, 'Send troops to fight ISIS'],
                         [4, 'Protect gays and lesbians against job discrimination'], [5, 'The death penalty for murder'],
                         [6, 'Change access to citizenship for children of illegal immigrants'], [7, 'Build a wall on the US-Mexico border'],
                         [8, 'Paid leave for parents of new children'], [9, 'Increase number of black students at universities'],
                         [10, 'Pay women and men the same amount for the same work']]
        random.shuffle(list_question)
        return list_question


class Care2(Page):
    form_model = models.Player
    form_fields = ['care2f', 'care2o']

    def care2f_choices(self):
        list_question = [[1, 'Reduce the difference in income'], [2, 'limit imports'], [3, 'Send troops to fight ISIS'],
                         [4, 'Protect gays and lesbians against job discrimination'], [5, 'The death penalty for murder'],
                         [6, 'Change access to citizenship for children of illegal immigrants'], [7, 'Build a wall on the US-Mexico border'],
                         [8, 'Paid leave for parents of new children'], [9, 'Increase number of black students at universities'],
                         [10, 'Pay women and men the same amount for the same work']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1]]

        # list_new = list(set(list_question)-set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new

    def care2o_choices(self):
        list_question = [[1, 'Reduce the difference in income'], [2, 'limit imports'], [3, 'Send troops to fight ISIS'],
                         [4, 'Protect gays and lesbians against job discrimination'], [5, 'The death penalty for murder'],
                         [6, 'Change access to citizenship for children of illegal immigrants'], [7, 'Build a wall on the US-Mexico border'],
                         [8, 'Paid leave for parents of new children'], [9, 'Increase number of black students at universities'],
                         [10, 'Pay women and men the same amount for the same work']]

        # list_temp = [self.player.care1f, self.player.care1o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1]]


        # list_new = list(set(list_question) - set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]

        random.shuffle(list_new)

        return list_new


class Care3(Page):
    form_model = models.Player
    form_fields = ['care3f', 'care3o']

    def care3f_choices(self):
        list_question = [[1, 'Reduce the difference in income'], [2, 'limit imports'], [3, 'Send troops to fight ISIS'],
                         [4, 'Protect gays and lesbians against job discrimination'], [5, 'The death penalty for murder'],
                         [6, 'Change access to citizenship for children of illegal immigrants'], [7, 'Build a wall on the US-Mexico border'],
                         [8, 'Paid leave for parents of new children'], [9, 'Increase number of black students at universities'],
                         [10, 'Pay women and men the same amount for the same work']]

        # list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1], list_question[int(self.player.care2o) - 1]]


        # list_new = list(set(list_question) - set(list_temp))
        list_new = [i for i in list_question if i not in list_temp]


        random.shuffle(list_new)

        return list_new

    def care3o_choices(self):
        list_question = [[1, 'Reduce the difference in income'], [2, 'limit imports'], [3, 'Send troops to fight ISIS'],
                         [4, 'Protect gays and lesbians against job discrimination'], [5, 'The death penalty for murder'],
                         [6, 'Change access to citizenship for children of illegal immigrants'], [7, 'Build a wall on the US-Mexico border'],
                         [8, 'Paid leave for parents of new children'], [9, 'Increase number of black students at universities'],
                         [10, 'Pay women and men the same amount for the same work']]

        # list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]
        list_temp = [list_question[int(self.player.care1f) - 1], list_question[int(self.player.care1o) - 1],
                     list_question[int(self.player.care2f) - 1], list_question[int(self.player.care2o) - 1]]

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


page_sequence = [
    # MyPage,
    # ResultsWaitPage,
    # Results
    Care1,
    Care2,
    Care3
]
