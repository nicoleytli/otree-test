from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'erase'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    mouse_x = models.TextField(
        blank=True
    )
    mouse_y = models.TextField(
        blank=True
    )
    ratio = models.FloatField(
        blank=True
    )
    option = models.IntegerField(
        choices=[[1, 'Reduce the difference in income'],
                 [2, 'Limit imports'],
                 [3, 'Send troops to fight ISIS'],
                 [4, 'Protect gays and lesbians against job discrimination'],
                 [5, 'The death penalty for murder'],
                 [6, 'Change access to citizenship for children of illegal immigrants'],
                 [7, 'Build a wall on the US-Mexico border'],
                 [8, 'Paid leave for parents of new children'],
                 [9, 'Increase number of black students at universities'],
                 [10, 'Pay women and men the same amount for the same work']],
        blank=True
    )