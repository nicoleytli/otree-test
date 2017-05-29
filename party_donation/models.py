from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'party_donation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    party_donation = models.IntegerField(
        widget=widgets.RadioSelect(),
        choices=[[1, 'Guess his/her party identification'],
                 [2, 'Guess his/her donation decision']]
    )

    party_choice = models.IntegerField(
        widget=widgets.RadioSelect(),
        choices=[[1, 'Strong Democrat'],
                 [2, 'Weak Democrat'],
                 [3, 'Lean Democrat'],
                 [4, 'Independent'],
                 [5, 'Lean Republican'],
                 [6, 'Weak Republican'],
                 [7, 'Strong Republican']]
    )

    donation_choice = models.IntegerField(
        widget=widgets.RadioSelect(),
        choices=[[1, 'organization 1'],
                 [2, 'organization 2'],
                 [3, 'organization 3'],
                 [4, 'organization 4'],
                 [5, 'organization 5'],
                 [6, 'organization 6'],
                 [7, 'organization 7'],
                 [8, 'organization 8'],
                 [9, 'organization 9'],
                 [10, 'organization 10']]
    )
