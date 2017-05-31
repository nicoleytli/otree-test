from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'url_test'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    # def before_session_starts(self):
    #     for p in self.get_players():
    #         p.participant.label = p.label
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    participant_label = models.CharField()
    url = models.CharField()
