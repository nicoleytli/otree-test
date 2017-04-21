from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'item'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Q1 = models.IntegerField(
        choices=[[1, 'Yes, voted'],
                 [2, 'No, did not vote']],
        widget=widgets.RadioSelect()
    )

    Q2 = models.IntegerField(
        choices=[[1, 'Hillary Clinton'],
                 [2, 'Donald Trump'],
                 [3, 'Other']],
        widget=widgets.RadioSelect()
    )

    Q3 = models.IntegerField(
        widget=widgets.RadioSelect()
    )
    Q4 = models.IntegerField(
        choices=[[1, 'Yes, I did'],
                [2, 'No, I did not']],
        widget=widgets.RadioSelect()
    )
    Q4_2 = models.IntegerField(
        choices=[[1, 'Support'],
                 [2, 'Oppose'],
                 [3, 'Neither']],
        widget = widgets.RadioSelect()
    )
    Q4_3 = models.TextField()
    Q5 = models.IntegerField()
    Q6 = models.IntegerField(
        choices=[[1, 'Liberal'],
                 [2, 'Conservative']],
        widget=widgets.RadioSelect()
    )
    Q7 = models.IntegerField()
    Q8 = models.IntegerField()
    Q9 = models.IntegerField()
    Q10 = models.IntegerField()
    Q11 = models.IntegerField()
    Q12 = models.IntegerField()
    Q13 = models.IntegerField()
