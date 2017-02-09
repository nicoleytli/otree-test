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
    name_in_url = 'majority_determine1'
    players_per_group = 4
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    coin = models.CharField()

    def set_payoffs(self):

        self.coin = random.choice(['head', 'tail'])

        for player in self.get_players():
            result1 = []
            result2 = []
            option_temp = [player.option1, player.option2, player.option3, player.option4]
            player.option = option_temp.index(max(option_temp)) + 1

            if player.option == 3 or player.option == 4:
                for i in self.get_players():
                    if i.id_in_group != player.id_in_group:
                        if i.decision == '♡':
                            result1.extend([i.decision])
                        else:
                            result2.extend([i.decision])
                    else:
                        pass
                if len(result1) > len(result2):
                    player.yourresult = bool(player.option == 4)
                else:
                    player.yourresult = bool(player.option == 3)

            else:
                if self.coin == 'head':
                    player.yourresult = bool(player.option == 2)
                else:
                    player.yourresult = bool(player.option == 1)


            player.payoff = player.yourresult * 4


class Player(BasePlayer):
    decision = models.CharField(
        choices=['♡', '☺︎'],
        doc="""Either ♡ or ☺︎""",
        widget=widgets.RadioSelect()
    )
    option1 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )
    option2 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )
    option3 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )
    option4 = models.CurrencyField(
        choices=currency_range(0, 4, c(0.01))
    )

    option = models.IntegerField()




