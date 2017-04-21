from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'infoseeking'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    info1 = models.CharField(
        blank=True
    )
    info2 = models.CharField(
        blank=True
    )
    info3 = models.CharField(
        blank=True
    )
    info4 = models.CharField(
        blank=True
    )
    info5 = models.CharField(
        blank=True
    )
    info6 = models.CharField(
        blank=True
    )
    info7 = models.CharField(
        blank=True
    )
    info8 = models.CharField(
        blank=True
    )
    info9 = models.CharField(
        blank=True
    )
    info10 = models.CharField(
        blank=True
    )

    email_info = models.CharField()

