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

    conditions = ['1LG', '1QG', '1QNG', '1LP', '1QP', '1QNP', '1LD', '1QD', '1QND', '1LI', '1QI',
                  '1QNI', '1LM', '1QM', '1QNM', '2LG', '2QG', '2QNG', '2LP', '2QP', '2QNP', '2LD',
                  '2QD', '2QND', '2LI', '2QI', '2QNI', '2LM', '2QM', '2QNM', '3LG', '3QG', '3QNG',
                  '3LP', '3QP', '3QNP', '3LD', '3QD', '3QND', '3LI', '3QI', '3QNI', '3LM', '3QM', '3QNM']


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

    priming1 = models.CharField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )

    priming2_dem_1 = models.CharField()
    priming2_dem_2 = models.CharField()
    priming2_dem_3 = models.CharField()
    priming2_dem_4 = models.CharField()
    priming2_dem_5 = models.CharField()
    priming2_dem_6 = models.CharField()
    priming2_dem_7 = models.CharField()
    priming2_dem_8 = models.CharField()
    priming2_dem_9 = models.CharField()
    priming2_dem_10 = models.CharField()

    priming2_rep_1 = models.CharField()
    priming2_rep_2 = models.CharField()
    priming2_rep_3 = models.CharField()
    priming2_rep_4 = models.CharField()
    priming2_rep_5 = models.CharField()
    priming2_rep_6 = models.CharField()
    priming2_rep_7 = models.CharField()
    priming2_rep_8 = models.CharField()
    priming2_rep_9 = models.CharField()
    priming2_rep_10 = models.CharField()

    # condition
    condition = models.CharField()



