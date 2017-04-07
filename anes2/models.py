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


class Subsession(BaseSubsession):
    pass



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



