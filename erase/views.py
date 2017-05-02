from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['option']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    form_model = models.Player
    form_fields = ['mouse_x', 'mouse_y', 'ratio']

    def vars_for_template(self):
        question = ['Reduce the difference in income', 'Limit imports', 'Send troops to fight ISIS',
                    'Protect gays and lesbians against job discrimination', 'The death penalty for murder',
                    'Change access to citizenship for children of illegal immigrants',
                    'Build a wall on the US-Mexico border',
                    'Paid leave for parents of new children', 'Increase number of black students at universities',
                    'Pay women and men the same amount for the same work']
        issue = question[self.player.option - 1]
        return {'issue': issue}

    def before_next_page(self):
        mouse_x_temp = self.player.mouse_x.split(",")
        mouse_y_temp = self.player.mouse_y.split(",")

        mouse_x = list(map(int, mouse_x_temp))
        mouse_y = list(map(int, mouse_y_temp))

        radius = 30
        width = 690
        height = 600
        area = []

        for i in range(len(mouse_x)):
            if i == 0:
                area.append((radius * 2)*(radius * 2))
            else:
                if abs(mouse_x[i]-mouse_x[i-1]) <= radius and abs(mouse_y[i]-mouse_y[i-1]) <= radius:
                    area.append(2*(abs(mouse_x[i]-mouse_x[i-1]))*radius + 2*(abs(mouse_y[i]-mouse_y[i-1]))*radius - \
                        abs(mouse_y[i]-mouse_y[i-1])*abs(mouse_x[i]-mouse_x[i-1]))
                else:
                    area.append((radius * 2)*(radius * 2))

        if sum(area) <= width*height:
            self.player.ratio = sum(area) / (width*height)
        else:
            self.player.ratio = 1





page_sequence = [
    MyPage,
    # ResultsWaitPage,
    Results
]