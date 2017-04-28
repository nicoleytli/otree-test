from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mouse'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.time_stamp_1a = 0
            p.time_stamp_1b = 0
            p.time_stamp_2a = 0
            p.time_stamp_2b = 0
            p.time_stamp_3a = 0
            p.time_stamp_3b = 0



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_1 = models.FloatField(
        blank=True
    )
    time_2 = models.FloatField(
        blank=True
    )
    time_3 = models.FloatField(
        blank=True
    )
    time_stamp_1a = models.IntegerField(
        blank=True
    )
    time_stamp_1b = models.IntegerField(
        blank=True
    )
    time_stamp_2a = models.IntegerField(
        blank=True
    )
    time_stamp_2b = models.IntegerField(
        blank=True
    )
    time_stamp_3a = models.IntegerField(
        blank=True
    )
    time_stamp_3b = models.IntegerField(
        blank=True
    )
    name = models.CharField()

