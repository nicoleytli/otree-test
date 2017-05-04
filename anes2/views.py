from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    def before_next_page(self):
        # if self.player.condition == 'None':
            # Retrieve the condition assignments from each participant so far
        conditions_so_far = []
        for p in self.subsession.get_players():
            conditions_so_far.append(p.condition)

        # Count how often each condition has been run
        conditions_n = {}
        for c in Constants.conditions:
            conditions_n[c] = conditions_so_far.count(c)

        # Create a new array containing the conditions that have been run the least amount of times
        conditions = []
        for c, n in conditions_n.items():
            if n == min(conditions_n.values()):
                conditions.append(c)

        # Randomly assign the participant to one of these conditions
        temp = random.choice(conditions)
        # for p in self.group.get_players():
        #     p.condition = temp
        self.participant.vars['group'] = temp
        self.player.condition = temp
        # else:
        #     pass



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

    def before_next_page(self):
        if self.player.partisanship1 == 1:
            self.participant.vars['partisanship'] = 'Democrat'
        elif self.player.partisanship1 == 2:
            self.participant.vars['partisanship'] = 'Republican'
        else:
            pass


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
        if self.player.partisanship3 == 1:
            self.participant.vars['partisanship'] = 'Closer to Republican Party'
        elif self.player.partisanship3 == 2:
            self.participant.vars['partisanship'] = 'Closer to Democratic Party'
        else:
            self.participant.vars['partisanship'] = 'Independent'



class Priming1(Page):
    form_model = models.Player
    form_fields = ['priming1']

    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
               self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '1LP' or self.participant.vars['group'] == '1QP' or \
               self.participant.vars['group'] == '1QNP' or self.participant.vars['group'] == '1LD' or \
               self.participant.vars['group'] == '1QD' or self.participant.vars['group'] == '1QND' or \
               self.participant.vars['group'] == '1LI' or self.participant.vars['group'] == '1QI' or \
               self.participant.vars['group'] == '1QNI' or self.participant.vars['group'] == '1LM' or \
               self.participant.vars['group'] == '1QM' or self.participant.vars['group'] == '1QNM'


class Priming2(Page):
    form_model = models.Player
    form_fields = ['priming2_dem_1', 'priming2_dem_2', 'priming2_dem_3', 'priming2_dem_4', 'priming2_dem_5',
                 'priming2_dem_6', 'priming2_dem_7', 'priming2_dem_8', 'priming2_dem_9', 'priming2_dem_10']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children', 'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants', 'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination', 'Send troops to fight ISIS']

        values = ['Strongly favor', 'Somewhat favor', 'Neutral', 'Somewhat oppose', 'Strongly oppose']

        names = ['priming2_dem_1', 'priming2_dem_2', 'priming2_dem_3', 'priming2_dem_4', 'priming2_dem_5',
                 'priming2_dem_6', 'priming2_dem_7', 'priming2_dem_8', 'priming2_dem_9', 'priming2_dem_10']

        mylist = zip(issues, names)

        return {
                'values': values,
                'mylist': mylist}


    def is_displayed(self):
        return self.participant.vars['group'] == '2LG' or self.participant.vars['group'] == '2QG' or \
               self.participant.vars['group'] == '2QNG' or self.participant.vars['group'] == '2LP' or self.participant.vars['group'] == '2QP' or \
               self.participant.vars['group'] == '2QNP' or self.participant.vars['group'] == '2LD' or \
               self.participant.vars['group'] == '2QD' or self.participant.vars['group'] == '2QND' or \
               self.participant.vars['group'] == '2LI' or self.participant.vars['group'] == '2QI' or \
               self.participant.vars['group'] == '2QNI' or self.participant.vars['group'] == '2LM' or \
               self.participant.vars['group'] == '2QM' or self.participant.vars['group'] == '2QNM'


class Priming2_2(Page):
    form_model = models.Player
    form_fields = ['priming2_rep_1', 'priming2_rep_2', 'priming2_rep_3', 'priming2_rep_4', 'priming2_rep_5',
                'priming2_rep_6', 'priming2_rep_7', 'priming2_rep_8', 'priming2_rep_9', 'priming2_rep_10']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children', 'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants', 'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination', 'Send troops to fight ISIS']

        values = ['Strongly favor', 'Somewhat favor', 'Neutral', 'Somewhat oppose', 'Strongly oppose']

        names = ['priming2_rep_1', 'priming2_rep_2', 'priming2_rep_3', 'priming2_rep_4', 'priming2_rep_5',
                'priming2_rep_6', 'priming2_rep_7', 'priming2_rep_8', 'priming2_rep_9', 'priming2_rep_10']

        mylist = zip(issues, names)

        return {
                'values': values,
                'mylist': mylist}

    def is_displayed(self):
        return self.participant.vars['group'] == '2LG' or self.participant.vars['group'] == '2QG' or \
               self.participant.vars['group'] == '2QNG' or self.participant.vars['group'] == '2LP' or \
               self.participant.vars['group'] == '2QP' or \
               self.participant.vars['group'] == '2QNP' or self.participant.vars['group'] == '2LD' or \
               self.participant.vars['group'] == '2QD' or self.participant.vars['group'] == '2QND' or \
               self.participant.vars['group'] == '2LI' or self.participant.vars['group'] == '2QI' or \
               self.participant.vars['group'] == '2QNI' or self.participant.vars['group'] == '2LM' or \
               self.participant.vars['group'] == '2QM' or self.participant.vars['group'] == '2QNM'


class Control(Page):
    form_model = models.Player
    form_fields = ['priming1']

    def is_displayed(self):
        return self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
               self.participant.vars['group'] == '3QNG' or self.participant.vars['group'] == '3LP' or self.participant.vars['group'] == '3QP' or \
               self.participant.vars['group'] == '3QNP' or self.participant.vars['group'] == '3LD' or \
               self.participant.vars['group'] == '3QD' or self.participant.vars['group'] == '3QND' or \
               self.participant.vars['group'] == '3LI' or self.participant.vars['group'] == '3QI' or \
               self.participant.vars['group'] == '3QNI' or self.participant.vars['group'] == '3LM' or \
               self.participant.vars['group'] == '3QM' or self.participant.vars['group'] == '3QNM'




page_sequence = [
    MyPage,
    Control,
    Priming1,
    Priming2,
    Priming2_2,
    Partisanship1,
    Partisanship2,
    Partisanship3
]
