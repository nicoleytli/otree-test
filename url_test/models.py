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

    current_url = models.TextField()

    datastring = models.CharField()

    treat = models.CharField()
    qv_id = models.CharField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()

