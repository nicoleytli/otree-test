from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'priming_treatment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.prime = random.choice(['prime 1', 'prime 2'])



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prime = models.CharField()
    prime1 = models.CharField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect()
    )

    prime2_dem_1 = models.CharField()
    prime2_dem_2 = models.CharField()
    prime2_dem_3 = models.CharField()
    prime2_dem_4 = models.CharField()
    prime2_dem_5 = models.CharField()
    prime2_dem_6 = models.CharField()
    prime2_dem_7 = models.CharField()
    prime2_dem_8 = models.CharField()
    prime2_dem_9 = models.CharField()
    prime2_dem_10 = models.CharField()

    prime2_rep_1 = models.CharField()
    prime2_rep_2 = models.CharField()
    prime2_rep_3 = models.CharField()
    prime2_rep_4 = models.CharField()
    prime2_rep_5 = models.CharField()
    prime2_rep_6 = models.CharField()
    prime2_rep_7 = models.CharField()
    prime2_rep_8 = models.CharField()
    prime2_rep_9 = models.CharField()
    prime2_rep_10 = models.CharField()

    mouse_x = models.TextField(
        blank=True
    )
    mouse_y = models.TextField(
        blank=True
    )
    mouse_t = models.TextField(
        blank=True
    )

    time = models.FloatField(
        blank=True
    )
