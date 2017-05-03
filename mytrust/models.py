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
    name_in_url = 'mytrust'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.preference_party = random.choice(['same', 'opposite'])



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    partner = models.IntegerField(
        widget=widgets.RadioSelect()
    )
    preference_party = models.CharField()
    donation_party = models.IntegerField(
        choices=[[1, 'I choose to guess his/her party identification'],
                 [2, 'I choose to guess his/her donation decision']],
        widget=widgets.RadioSelect()
    )
