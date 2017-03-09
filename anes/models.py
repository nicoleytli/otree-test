from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'anes'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_1 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_2 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_3 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_4 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_5 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_6 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_7 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_8 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_9 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_10 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_11 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_12 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_13 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )
    question_14 = models.CharField(
        choices=['Favor', 'Oppose', 'Neither favor nor oppose'],
        widget=widgets.RadioSelect()
    )

    likert_1 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_2 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_3 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_4 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_5 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_6 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_7 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_8 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_9 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_10 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_11 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_12 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_13 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )
    likert_14 = models.CharField(
        choices=['A great deal', 'Moderately', 'A little'],
        widget=widgets.RadioSelectHorizontal()
    )

    gender = models.CharField(
        choices=['Female', 'Male', 'Other'],
        widget=widgets.RadioSelect()
    )
    age = models.PositiveIntegerField(
        max=100, min=18
    )
    religion = models.CharField()


