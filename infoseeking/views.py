from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['info1', 'info2', 'info3', 'info4', 'info5', 'info6', 'info7', 'info8', 'info9', 'info10']

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

        temp = [self.player.info1, self.player.info2, self.player.info3, self.player.info4, self.player.info5,
                self.player.info6, self.player.info7, self.player.info8, self.player.info9, self.player.info10]
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
        return self.participant.vars['group'] == '1LI' or self.participant.vars['group'] == '1QI' or \
               self.participant.vars['group'] == '1QNI' or self.participant.vars['group'] == '2LI' or \
               self.participant.vars['group'] == '2QI' or self.participant.vars['group'] == '2QNI' or \
               self.participant.vars['group'] == '3LI' or self.participant.vars['group'] == '3QI' or \
               self.participant.vars['group'] == '3QNI'


page_sequence = [
    MyPage,
    Results
]
