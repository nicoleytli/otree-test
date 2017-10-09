from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'risk_infection_2'
    players_per_group = 9
    num_rounds = 2

    with open('risk_infection/info.csv') as f:
        info = list(csv.DictReader(f))


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            # for p in self.get_players():
            #     for i in range(len(Constants.info)):
            #         if Constants.info[i]['Number'] == str(p.participant.vars.get('number')):
            #             p.participant.vars['grouprole'] = Constants.info[i]['GroupRole']
            #             if p.participant.vars['grouprole'] == '1A' or p.participant.vars['grouprole'] == '2A' or \
            #                             p.participant.vars['grouprole'] == '3A' or p.participant.vars[
            #                 'grouprole'] == '4A' or \
            #                             p.participant.vars['grouprole'] == '5A' or p.participant.vars[
            #                 'grouprole'] == '6A':
            #                 p.role = 'A'
            #                 p.participant.vars['role'] = 'A'
            #             else:
            #                 p.role = 'B'
            #                 p.participant.vars['role'] = 'B'
            #
            # players = self.get_players()
            # players_1A = [p for p in players if p.participant.vars.get('grouprole') == '1A']
            # players_1B = [p for p in players if p.participant.vars.get('grouprole') == '1B']
            # players_2A = [p for p in players if p.participant.vars.get('grouprole') == '2A']
            # players_2B = [p for p in players if p.participant.vars.get('grouprole') == '2B']
            # players_3A = [p for p in players if p.participant.vars.get('grouprole') == '3A']
            # players_3B = [p for p in players if p.participant.vars.get('grouprole') == '3B']
            # players_4A = [p for p in players if p.participant.vars.get('grouprole') == '4A']
            # players_4B = [p for p in players if p.participant.vars.get('grouprole') == '4B']
            # players_5A = [p for p in players if p.participant.vars.get('grouprole') == '5A']
            # players_5B = [p for p in players if p.participant.vars.get('grouprole') == '5B']
            # players_6A = [p for p in players if p.participant.vars.get('grouprole') == '6A']
            # players_6B = [p for p in players if p.participant.vars.get('grouprole') == '6B']
            # group_matrix = []
            # names = locals()
            #
            # for i in range(1, 7):
            #     while names['players_%sA' % i]:
            #         new_group = [
            #             names['players_%sA' % i].pop(),
            #             names['players_%sA' % i].pop(),
            #             names['players_%sA' % i].pop(),
            #             names['players_%sA' % i].pop(),
            #             names['players_%sA' % i].pop(),
            #             names['players_%sA' % i].pop(),
            #             names['players_%sB' % i].pop(),
            #             names['players_%sB' % i].pop(),
            #             names['players_%sB' % i].pop(),
            #         ]
            #         group_matrix.append(new_group)
            #
            # self.set_group_matrix(group_matrix)

            self.session.vars['fluiditya_1'] = random.choice(['H', 'L', 'L'])
            self.session.vars['fluidityb_1'] = random.choice(['H', 'L', 'L'])
        else:
            # self.group_like_round(1)
            # 其中一个
            r1 = random.choice(list(range(3)))
            if self.session.vars['fluiditya_%s' % (self.round_number - 1)] == 'H':
                if r1 <= 1: # 2/3
                    self.session.vars['fluiditya_%s' % self.round_number] = 'L'
                else:
                    self.session.vars['fluiditya_%s' % self.round_number] = 'H'
            else: # 上一轮是低
                if r1 <= 1:
                    self.session.vars['fluiditya_%s' % self.round_number] = 'H'
                else:
                    self.session.vars['fluiditya_%s' % self.round_number] = 'L'

            # 第二个
            r2 = random.choice(list(range(3)))
            if self.session.vars['fluidityb_%s' % (self.round_number - 1)] == 'H':
                if r2 <= 1: # 2/3
                    self.session.vars['fluidityb_%s' % self.round_number] = 'L'
                else:
                    self.session.vars['fluidityb_%s' % self.round_number] = 'H'
            else: # 上一轮是低
                if r2 <= 1:
                    self.session.vars['fluidityb_%s' % self.round_number] = 'H'
                else:
                    self.session.vars['fluidityb_%s' % self.round_number] = 'L'

        for p in self.get_players():
            if p.id_in_subsession <= 27:
                if p.id_in_subsession % 9 == 0 or p.id_in_subsession % 9 == 8 or p.id_in_subsession % 9 == 7:
                    p.role = 'B_dep'
                else:
                    p.role = 'A_dep'
            else:
                if p.id_in_subsession % 9 == 0 or p.id_in_subsession % 9 == 8 or p.id_in_subsession % 9 == 7:
                    p.role = 'B_ind'
                else:
                    p.role = 'A_ind'


class Group(BaseGroup):
    def set_payoffs(self):
        withdraw_A = []
        withdraw_B = []
        for p in self.get_players():
            if p.role == 'A_dep' or p.role == 'A_ind':
                if p.choice == 1:
                    withdraw_A.append(p.choice)
            else:
                if p.choice == 1:
                    withdraw_B.append(p.choice)

        self.session.vars['withdraw_A'] = len(withdraw_A)
        self.session.vars['withdraw_B'] = len(withdraw_B)

        for p in self.get_players():
            if self.round_number <= 30:
                if p.role == 'A_ind' or p.role == 'A_dep':
                    if self.session.vars['fluiditya_%s' % self.round_number] == 'L':
                        p.fluidity = 'L'
                        if len(withdraw_A) == 0:
                            if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_A) == 1:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 25
                        elif len(withdraw_A) == 2:
                            if p.choice == 1:
                                p.utility = 60
                            else:
                                p.utility = 0
                        elif len(withdraw_A) == 3:
                            if p.choice == 1:
                                p.utility = 40
                            else:
                                p.utility = 0
                        elif len(withdraw_A) == 4:
                            if p.choice == 1:
                                p.utility = 30
                            else:
                                p.utility = 0
                        elif len(withdraw_A) == 5:
                            if p.choice == 1:
                                p.utility = 24
                            else:
                                p.utility = 0
                        else:
                            if p.choice == 1:
                                p.utility = 20
                    else:
                        p.fluidity = 'H'
                        if len(withdraw_A) == 0:
                            if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_A) == 1:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 119
                        elif len(withdraw_A) == 2:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 109
                        elif len(withdraw_A) == 3:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 94
                        elif len(withdraw_A) == 4:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 63
                        elif len(withdraw_A) == 5:
                            if p.choice == 1:
                                p.utility = 96
                            else:
                                p.utility = 0
                        else:
                            if p.choice == 1:
                                p.utility = 80
                else:
                    if p.role == 'B_ind':
                        prob = self.session.vars['fluidityb_%s' % self.round_number]
                    else:
                        prob = self.session.vars['fluiditya_%s' % self.round_number]
                    if prob == 'L':
                        p.fluidity = 'L'
                        if len(withdraw_B) == 0:
                            if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_B) == 1:
                            if p.choice == 1:
                                p.utility = 60
                            else:
                                p.utility = 0
                        elif len(withdraw_B) == 2:
                            if p.choice == 1:
                                p.utility = 30
                            else:
                                p.utility = 0
                        else:
                            if p.choice == 1:
                                p.utility = 20
                    else:
                        p.fluidity = 'H'
                        if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_B) == 1:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 109
                        elif len(withdraw_B) == 2:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 63
                        else:
                            if p.choice == 1:
                                p.utility = 80
            else:
                if p.role == 'B_ind' or p.role == 'B_dep':
                    if self.session.vars['fluiditya_%s' % self.round_number] == 'L':
                        p.fluidity = 'L'
                        if len(withdraw_B) == 0:
                            if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_B) == 1:
                            if p.choice == 1:
                                p.utility = 60
                            else:
                                p.utility = 0
                        elif len(withdraw_B) == 2:
                            if p.choice == 1:
                                p.utility = 30
                            else:
                                p.utility = 0
                        else:
                            if p.choice == 1:
                                p.utility = 20
                    else:
                        p.fluidity = 'H'
                        if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_B) == 1:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 109
                        elif len(withdraw_B) == 2:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 63
                        else:
                            if p.choice == 1:
                                p.utility = 80
                else:
                    if p.role == 'A_ind':
                        prob = self.session.vars['fluidityb_%s' % self.round_number]
                    else:
                        prob = self.session.vars['fluiditya_%s' % self.round_number]
                    if prob == 'L':
                        p.fluidity = 'L'
                        if len(withdraw_A) == 0:
                            if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_A) == 1:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 25
                        elif len(withdraw_A) == 2:
                            if p.choice == 1:
                                p.utility = 60
                            else:
                                p.utility = 0
                        elif len(withdraw_A) == 3:
                            if p.choice == 1:
                                p.utility = 40
                            else:
                                p.utility = 0
                        elif len(withdraw_A) == 4:
                            if p.choice == 1:
                                p.utility = 30
                            else:
                                p.utility = 0
                        elif len(withdraw_A) == 5:
                            if p.choice == 1:
                                p.utility = 24
                            else:
                                p.utility = 0
                        else:
                            if p.choice == 1:
                                p.utility = 20
                    else:
                        p.fluidity = 'H'
                        if len(withdraw_A) == 0:
                            if p.choice == 2:
                                p.utility = 125
                        elif len(withdraw_A) == 1:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 119
                        elif len(withdraw_A) == 2:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 109
                        elif len(withdraw_A) == 3:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 94
                        elif len(withdraw_A) == 4:
                            if p.choice == 1:
                                p.utility = 100
                            else:
                                p.utility = 63
                        elif len(withdraw_A) == 5:
                            if p.choice == 1:
                                p.utility = 96
                            else:
                                p.utility = 0
                        else:
                            if p.choice == 1:
                                p.utility = 80


class Player(BasePlayer):
    role = models.CharField()
    choice = models.IntegerField(
        choices=[[1, '当期取款'], [2, '等待期满']]
    )
    utility = models.IntegerField()
    payoff = models.FloatField()
    fluidity = models.CharField()
