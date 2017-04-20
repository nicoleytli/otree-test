from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'anes2'
    players_per_group = None
    num_rounds = 1

    conditions = ['1LG', '1QG', '1QNG', '1LP', '1QP', '1QNP', '1LD', '1QD', '1QND','1LI', '1QI',
                  '1QNI','2LG', '2QG', '2QNG', '2LP', '2QP', '2QNP', '2LD', '2QD', '2QND', '2LI',
                  '2QI', '2QNI', '3LG', '3QG', '3QNG', '3LP', '3QP', '3QNP','3LD', '3QD', '3QND',
                  '3LI', '3QI', '3QNI']


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.condition = 'None'



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    partisanship1 = models.IntegerField(
        choices=[[1, 'Democrat'],
                 [2, 'Republican'],
                 [3, 'Independent'],
                 [5, 'Other party'],
                 [8, 'Do not know']],
        widget=widgets.RadioSelect()
    )

    order1 = models.IntegerField()

    partisanship2 = models.IntegerField(
        choices=[[1, 'Strong'],
                 [2, 'Not very strong'],
                 [5, 'Inapplicable'],
                 [8, 'Do not know']],
        widget=widgets.RadioSelect()
    )

    partisanship3 = models.IntegerField(
        choices=[[1, 'Closer to Republican'],
                 [2, 'Closer to Democratic'],
                 [3, 'Neither']],
        widget=widgets.RadioSelect()
    )

    order3 = models.IntegerField()

    priming1 = models.CharField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )

    priming2 = models.CharField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )

    # condition
    condition = models.CharField()



