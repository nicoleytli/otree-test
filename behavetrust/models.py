from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'behavetrust'
    players_per_group = 2
    num_rounds = 1


    # Initial amount allocated to each player
    amount_allocated = 1
    multiplication_factor = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        doc="""Amount sent by P1""",
        choices=currency_range(0, Constants.amount_allocated, 0.1),
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
        min=0,
    )


    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.amount_allocated - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


class Player(BasePlayer):

    choice = models.CharField()

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]

    def fchoice(self):
        self.choice = self.participant.vars['partisanship']
