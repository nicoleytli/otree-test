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
    players_per_group = None
    num_rounds = 1

    with open('risk_infection/info.csv') as f:
        questions = list(csv.DictReader(f))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number = models.IntegerField()
    name = models.CharField()
    grade = models.IntegerField()
    major = models.CharField()

