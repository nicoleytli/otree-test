from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
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




class Results(Page):
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


page_sequence = [
    MyPage,
    # ResultsWaitPage,
    Results
]
