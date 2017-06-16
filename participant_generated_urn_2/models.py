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
    name_in_url = 'participant_generate_urn'
    players_per_group = 4
    num_rounds = 1
    conditions = ['Participant', 'Experimenter']
    symbols = ['uparrow', 'downarrow', 'heart', 'circle', 'downzhe', 'upzhe', 'square', 'line', 'arrow', 'circle2',
               'theta', 'question', '11']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    symbol_exp = models.IntegerField()
    treatment = models.CharField()
    symbol_pair = models.CharField()
    a = models.IntegerField()
    b = models.IntegerField()
    coin = models.CharField()

    def set_payoffs(self):
        # result of first coin
        self.coin = random.choice(['Head', 'Tail'])

        self.symbol_exp = random.randint(1, 3)
        if self.treatment == 'Experimenter':
            self.a = random.randint(0, 3)
            self.b = 3 - self.a
        else:
            pass

        for player in self.get_players():

            result_a = []
            option_temp = [player.option1, player.option2, player.option3, player.option4]
            player.option = option_temp.index(max(option_temp)) + 1

            # for those choose second coin
            if self.treatment == 'Participant':
                for p in self.get_players():
                    if p.id_in_group != player.id_in_group:
                        if p.decision == 'A':
                            result_a.extend([p.decision])
                        else:
                            pass
                    else:
                        pass
                player.a = len(result_a)
                player.b = 3 - player.a
            else:
                pass

            player.symbol_par = random.randint(1, 3)

            if self.treatment == 'Participant':
                if player.option == 4:
                    if player.symbol_par <= player.a:
                        player.result = 'A'
                        player.payoff = 4
                    else:
                        player.result = 'B'
                        player.payoff = 0
                elif player.option == 3:
                    if player.symbol_par <= player.a:
                        player.result = 'A'
                        player.payoff = 0
                    else:
                        player.result = 'B'
                        player.payoff = 4
                elif player.option == 1:
                    if self.coin == 'Head':
                        player.payoff = 0
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 4
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                else:
                    if self.coin == 'Head':
                        player.payoff = 4
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 0
                        if player.symbol_par <= player.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
            else:
                if player.option == 4:
                    if self.symbol_exp <= self.a:
                        player.result = 'A'
                        player.payoff = 4
                    else:
                        player.result = 'B'
                        player.payoff = 0
                elif player.option == 3:
                    if self.symbol_exp <= self.a:
                        player.result = 'A'
                        player.payoff = 0
                    else:
                        player.result = 'B'
                        player.payoff = 4
                elif player.option == 1:
                    if self.coin == 'Head':
                        player.payoff = 0
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 4
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                else:
                    if self.coin == 'Head':
                        player.payoff = 4
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'
                    else:
                        player.payoff = 0
                        if self.symbol_exp <= self.a:
                            player.result = 'A'
                        else:
                            player.result = 'B'


class Player(BasePlayer):
    decision = models.CharField(
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

    treatment = models.CharField()

    option = models.IntegerField()

    # 抽出来的结果
    result = models.CharField()

    belief = models.IntegerField(
        doc="""Please choose one of the options"""
    )

    a = models.IntegerField()
    b = models.IntegerField()
    symbol_par = models.IntegerField()

