from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['petition', 'email_petition']

    # def vars_for_template(self):
    #     question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
    #                 'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
    #                 'Change access to citizenship for children of illegal immigrants',
    #                 'Build a wall on the US-Mexico border',
    #                 'Paid leave for parents of new children', 'Increase number of black students at universities',
    #                 'Pay women and men the same amount for the same work']
    #     attitude = []
    #     for i in range(1, 11):
    #         attitude.append(self.participant.vars['opinion_%s' % i])
    #
    #     value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    #     mylist = zip(question, attitude, value)
    #
    #     return {'list': mylist}


class MyPage2(Page):
    form_model = models.Player
    form_fields = ['petition', 'email_petition']

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

        mylist = zip(question, attitude)

        return {'list': mylist}

    def is_displayed(self):
        return self.participant.vars['group'] == '1LP' or self.participant.vars['group'] == '1QP' or \
               self.participant.vars['group'] == '1QNP' or self.participant.vars['group'] == '2LP' or \
               self.participant.vars['group'] == '2QP' or self.participant.vars['group'] == '2QNP' or \
               self.participant.vars['group'] == '3LP' or self.participant.vars['group'] == '3QP' or \
               self.participant.vars['group'] == '3QNP'




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage2,
    # ResultsWaitPage,
    # Results
]
