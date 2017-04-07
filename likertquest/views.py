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
        list_question = ['Reduce the difference in income', 'limit imports', 'Send troops to fight ISIS',
                         'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                         'Change access to citizenship for children of illegal immigrants', 'Build a wall on the US-Mexico border',
                         'Paid leave for parents of new children', 'Increase number of black students at universities',
                         'Pay women and men the same amount for the same work']
        random.shuffle(list_question)
        return list_question

    def care1o_choices(self):
        list_question = ['Reduce the difference in income', 'limit imports', 'Send troops to fight ISIS',
                         'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                         'Change access to citizenship for children of illegal immigrants',
                         'Build a wall on the US-Mexico border',
                         'Paid leave for parents of new children', 'Increase number of black students at universities',
                         'Pay women and men the same amount for the same work']
        random.shuffle(list_question)
        return list_question


class Care2(Page):
    form_model = models.Player
    form_fields = ['care2f', 'care2o']

    def care2f_choices(self):
        list_question = ['Reduce the difference in income', 'limit imports', 'Send troops to fight ISIS',
                         'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                         'Change access to citizenship for children of illegal immigrants', 'Build a wall on the US-Mexico border',
                         'Paid leave for parents of new children', 'Increase number of black students at universities',
                         'Pay women and men the same amount for the same work']

        list_temp = [self.player.care1f, self.player.care1o]

        list_new = list(set(list_question)-set(list_temp))

        random.shuffle(list_new)

        return list_new

    def care2o_choices(self):
        list_question = ['Reduce the difference in income', 'limit imports', 'Send troops to fight ISIS',
                         'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                         'Change access to citizenship for children of illegal immigrants',
                         'Build a wall on the US-Mexico border',
                         'Paid leave for parents of new children', 'Increase number of black students at universities',
                         'Pay women and men the same amount for the same work']

        list_temp = [self.player.care1f, self.player.care1o]

        list_new = list(set(list_question) - set(list_temp))

        random.shuffle(list_new)

        return list_new


class Care3(Page):
    form_model = models.Player
    form_fields = ['care3f', 'care3o']

    def care3f_choices(self):
        list_question = ['Reduce the difference in income', 'limit imports', 'Send troops to fight ISIS',
                         'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                         'Change access to citizenship for children of illegal immigrants',
                         'Build a wall on the US-Mexico border',
                         'Paid leave for parents of new children', 'Increase number of black students at universities',
                         'Pay women and men the same amount for the same work']

        list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]

        list_new = list(set(list_question) - set(list_temp))

        random.shuffle(list_new)

        return list_new

    def care3o_choices(self):
        list_question = ['Reduce the difference in income', 'limit imports', 'Send troops to fight ISIS',
                         'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                         'Change access to citizenship for children of illegal immigrants',
                         'Build a wall on the US-Mexico border',
                         'Paid leave for parents of new children', 'Increase number of black students at universities',
                         'Pay women and men the same amount for the same work']

        list_temp = [self.player.care1f, self.player.care1o, self.player.care2f, self.player.care2o]

        list_new = list(set(list_question) - set(list_temp))

        random.shuffle(list_new)

        return list_new


page_sequence = [
    # MyPage,
    # ResultsWaitPage,
    # Results
    Care1,
    Care2,
    Care3
]
