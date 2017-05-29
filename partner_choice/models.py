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
    name_in_url = 'partner_choice'
    players_per_group = None
    num_rounds = 1

    party_list = ['Democrat', 'Republican']
    preference_list = ['Favor', 'Oppose']


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.party = random.choice(Constants.party_list)
            p.preference = random.choice(Constants.preference_list)
            p.preference_party = random.choice(['same', 'opposite'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    party = models.CharField()
    preference = models.CharField()
    partner = models.IntegerField(
        widget=widgets.RadioSelect()
    )
    preference_party = models.CharField()
