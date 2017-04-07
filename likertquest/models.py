from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'likertquest'
    players_per_group = None
    num_rounds = 1

    # with open('likertquest/issue.csv') as f:
    #     issue = list(csv.DictReader(f))



class Subsession(BaseSubsession):
    # def before_session_starts(self):
    #     if self.round_number == 1:
    #         self.session.vars['issue'] = Constants.issue
    #         randomized_list = random.sample(Constants.list_question, len(Constants.list_question))
    #         self.session.vars['list'] = randomized_list
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    care1f = models.CharField(
        widget=widgets.RadioSelect()
    )

    care1o = models.CharField(
        widget=widgets.RadioSelect()
    )

    care2f = models.CharField(
        widget=widgets.RadioSelect(),
    )

    care2o = models.CharField(
        widget=widgets.RadioSelect(),
    )

    care3f = models.CharField(
        widget=widgets.RadioSelect(),
    )

    care3o = models.CharField(
        widget=widgets.RadioSelect(),
    )

    # def current_question(self):
    #     return self.session.vars['issue'][0]
