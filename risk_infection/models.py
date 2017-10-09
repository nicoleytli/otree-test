from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'risk_infection'
    players_per_group = 9
    num_rounds = 1

    with open('risk_infection/info.csv') as f:
        info = list(csv.DictReader(f))


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['info'] = Constants.info


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number = models.IntegerField()
    name = models.CharField()
    grade = models.IntegerField()
    major = models.CharField()
    bankA = models.IntegerField()
    bankB = models.IntegerField()
    fluidityA = models.CharField(
        choices=['相同', '不相同', '不确定']
    )
    fluidityB = models.CharField(
        choices=['相同', '不相同', '不确定']
    )
    utility1 = models.IntegerField()
    utility2 = models.IntegerField()
    utility3 = models.IntegerField()
    utility4 = models.IntegerField()
    utility5 = models.IntegerField()
    utility6 = models.IntegerField()
    utility7 = models.IntegerField()
    utility8 = models.IntegerField()
    utility9 = models.IntegerField()
    utility10 = models.IntegerField()
    utility11 = models.IntegerField()
    utility12 = models.IntegerField()
    score = models.IntegerField()

    bankA_2 = models.IntegerField()
    bankB_2 = models.IntegerField()
    fluidityA_2 = models.CharField(
        choices=['相同', '不相同', '不确定']
    )
    fluidityB_2 = models.CharField(
        choices=['相同', '不相同', '不确定']
    )
    utility1_2 = models.IntegerField()
    utility2_2 = models.IntegerField()
    utility3_2 = models.IntegerField()
    utility4_2 = models.IntegerField()
    utility5_2 = models.IntegerField()
    utility6_2 = models.IntegerField()
    utility7_2 = models.IntegerField()
    utility8_2 = models.IntegerField()
    utility9_2 = models.IntegerField()
    utility10_2 = models.IntegerField()
    utility11_2 = models.IntegerField()
    utility12_2 = models.IntegerField()
    score_2 = models.IntegerField()
