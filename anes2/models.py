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

    conditions = ['1LG', '1QG', '1QNG', '1LS', '1QS', '1QNS', '1LP', '1QP', '1QNP', '2LG', '2QG', '2QNG', '2LS', '2QS',
                 '2QNS', '2LP', '2QP', '2QNP', '3LG', '3QG', '3QNG', '3LS', '3QS', '3QNS', '3LP', '3QP', '3QNP']


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

    priming1 = models.TextField()

    priming2 = models.CharField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )

    # condition
    condition = models.CharField()



