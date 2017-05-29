from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Priming1(Page):
    form_model = models.Player
    form_fields = ['prime1', 'mouse_x', 'mouse_y', 'mouse_t']


    def before_next_page(self):
        mouse_t_temp = self.player.mouse_t.split(",")
        mouse_t = list(map(float, mouse_t_temp))
        self.player.time = sum(mouse_t)

    def is_displayed(self):
        return self.player.prime == 'prime 1'


class Priming2(Page):
    form_model = models.Player
    form_fields = ['prime2_dem_1', 'prime2_dem_2', 'prime2_dem_3', 'prime2_dem_4', 'prime2_dem_5',
                 'prime2_dem_6', 'prime2_dem_7', 'prime2_dem_8', 'prime2_dem_9', 'prime2_dem_10']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children', 'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants', 'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination', 'Send troops to fight ISIS']

        values = ['Strongly favor', 'Somewhat favor', 'Neutral', 'Somewhat oppose', 'Strongly oppose']

        names = ['prime2_dem_1', 'prime2_dem_2', 'prime2_dem_3', 'prime2_dem_4', 'prime2_dem_5',
                 'prime2_dem_6', 'prime2_dem_7', 'prime2_dem_8', 'prime2_dem_9', 'prime2_dem_10']

        mylist = zip(issues, names)

        return {
                'values': values,
                'mylist': mylist}

    def is_displayed(self):
        return self.player.prime == 'prime 2'


class Priming2_2(Page):
    form_model = models.Player
    form_fields = ['prime2_rep_1', 'prime2_rep_2', 'prime2_rep_3', 'prime2_rep_4', 'prime2_rep_5',
                'prime2_rep_6', 'prime2_rep_7', 'prime2_rep_8', 'prime2_rep_9', 'prime2_rep_10']

    def vars_for_template(self):
        issues = ['Reduce the difference in income', 'Pay women and men the same amount for the same work',
                  'Limit imports', 'Increase number of black students at universities',
                  'Paid leave for parents of new children', 'Build a wall on the US-Mexico border',
                  'Change access to citizenship for children of illegal immigrants', 'The death penalty for murder',
                  'Protect gays and lesbians against job discrimination', 'Send troops to fight ISIS']

        values = ['Strongly favor', 'Somewhat favor', 'Neutral', 'Somewhat oppose', 'Strongly oppose']

        names = ['prime2_rep_1', 'prime2_rep_2', 'prime2_rep_3', 'prime2_rep_4', 'prime2_rep_5',
                'prime2_rep_6', 'prime2_rep_7', 'prime2_rep_8', 'prime2_rep_9', 'prime2_rep_10']

        mylist = zip(issues, names)

        return {
                'values': values,
                'mylist': mylist}

    def is_displayed(self):
        return self.player.prime == 'prime 2'


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Priming1,
    Priming2,
    Priming2_2
]
