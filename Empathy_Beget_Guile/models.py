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
    name_in_url = 'Empathy_Beget_Guile'
    players_per_group = 2
    num_rounds = 1
    # treatment_empathy = [1, 2, 3, 4]
    # treatment_control = [1, 2, 3, 4]
    # treatment_guile = [1, 2, 3, 4]
    # random.shuffle(treatment_empathy)
    # random.shuffle(treatment_control)
    # random.shuffle(treatment_guile)


class Subsession(BaseSubsession):
    def get_treatment(self):
        for g in self.get_groups():
            for p in g.get_players():
                p.treatment = p.participant['treatment']
                p.is_4 = bool(p.treatment == 4)
                g.treatment = p.treatment

        # treatment_empathy = [1, 2, 3, 4]
        # treatment_control = [1, 2, 3, 4]
        # treatment_guile = [1, 2, 3, 4]
        #
        # random.shuffle(treatment_empathy)
        # random.shuffle(treatment_control)
        # random.shuffle(treatment_guile)
        #
        # self.session.vars['treatment_empathy'] = treatment_empathy
        # self.session.vars['treatment_control'] = treatment_control
        # self.session.vars['treatment_guile'] = treatment_guile
        #
        # self.session.vars['Empathy'] = 0
        # self.session.vars['Control'] = 0
        # self.session.vars['Guile'] = 0

    # def before_session_starts(self):
    #     for p in self.get_players():
    #         temp = random.randint(1, 4)
    #         if temp == 1:
    #             p.is_4 = 1
    #         else:
    #             p.is_4 = 0
    # def get_treatment(self):
    #     # for i, g in enumerate(self.get_groups()):
    #     #     for p in g.get_players():
    #     #         p.treatment = treatment[i]
    #     #         if treatment[i] == 4:
    #     #             p.is_4 = 1
    #     #         else:
    #     #             p.is_4 = 0
    #     for g in self.get_groups():
    #         for p in g.get_players():
    #             if g.id_in_subsession % 4 == 2:
    #                 g.treatment = 1
    #                 p.treatment = 1
    #                 p.is_4 = 0
    #             elif g.id_in_subsession % 4 == 3:
    #                 g.treatment = 2
    #                 p.treatment = 2
    #                 p.is_4 = 0
    #             elif g.id_in_subsession % 4 == 0:
    #                 g.treatment = 3
    #                 p.treatment = 3
    #                 p.is_4 = 0
    #             else:
    #                 g.treatment = 4
    #                 p.treatment = 4
    #                 p.is_4 = 1
    # def get_treatment(self):
    #     for g in self.get_groups():
    #         for p in g.get_players():
    #             if p.participant.vars['priming'] == 'Empathy':
    #                 temp = 'Empathy'
    #                 p.treatment = self.session.vars['treatment_empathy'][self.session.vars['Empathy']]
    #                 p.is_4 = bool(self.session.vars['treatment_empathy'][self.session.vars['Empathy']] == 4)
    #
    #             elif p.participant.vars['priming'] == 'Control':
    #                 temp = 'Control'
    #                 p.treatment = self.session.vars['treatment_control'][self.session.vars['Control']]
    #                 p.is_4 = bool(self.session.vars['treatment_control'][self.session.vars['Control']] == 4)
    #
    #             else:
    #                 temp = 'Guile'
    #                 p.treatment = self.session.vars['treatment_guile'][self.session.vars['Guile']]
    #                 p.is_4 = bool(self.session.vars['treatment_guile'][self.session.vars['Guile']] == 4)
    #
    #             g.treatment = p.treatment
    #
    #         if temp == 'Empathy':
    #             self.session.vars['Empathy'] += 1
    #         elif temp == 'Control':
    #             self.session.vars['Control'] += 1
    #         else:
    #             self.session.vars['Guile'] += 1


class Group(BaseGroup):

    treatment = models.IntegerField()

    # def get_treatment(self):
    #     p1 = self.get_player_by_role('Player 1')
    #     p2 = self.get_player_by_role('Player 2')
    #
    #     self.treatment = random.randint(1, 3)
    #     p1.treatment = self.treatment
    #     p2.treatment = self.treatment

    # def get_treatment(self):
    #     for p in self.get_players():
    #         i = p.id_in_subsession - 1
    #         if p.participant.vars['priming'] == 'Empathy':
    #             p.treatment = Constants.treatment_empathy[i]
    #             p.is_4 = bool(Constants.treatment_empathy[i] == 4)
    #         elif p.participant.vars['priming'] == 'Control':
    #             p.treatment = Constants.treatment_control[i]
    #             p.is_4 = bool(Constants.treatment_control[i] == 4)
    #         else:
    #             p.treatment = Constants.treatment_guile[i]
    #             p.is_4 = bool(Constants.treatment_guile[i] == 4)
    #         self.treatment = p.treatment

    def set_payoffs(self):

        p1 = self.get_player_by_role('Player 1')
        p2 = self.get_player_by_role('Player 2')

        if self.treatment == 1:
            if p2.option_AB == 'Option A':
                p1.payoff = 0.25
                p2.payoff = 0.26
            else:
                p1.payoff = 0.26
                p2.payoff = 0.25
        elif self.treatment == 2:
            if p2.option_AB == 'Option A':
                p1.payoff = 0.25
                p2.payoff = 0.35
            else:
                p1.payoff = 0.26
                p2.payoff = 0.25
        elif self.treatment == 3:
            if p2.option_AB == 'Option A':
                p1.payoff = 0.25
                p2.payoff = 0.35
            else:
                p1.payoff = 0.35
                p2.payoff = 0.25
        else:
            p1.payoff = 0.30
            p2.payoff = 0.30


class Player(BasePlayer):

    # Decision for Treatment 1-3
    Message_12 = models.CharField(
        choices=['Message 1', 'Message 2'],
        doc="""Either 'Message 1' or 'Message 2'""",
        widget=widgets.RadioSelect()
    )
    option_AB = models.CharField(
        choices=['Option A', 'Option B'],
        doc="""Either 'Option A' or 'Option B'""",
        widget=widgets.RadioSelect()
    )

    # Decision for Treatment 4
    option4_1 = models.CharField(
        choices=['Completely Fair', 'Fair', 'Unfair', 'Very Unfair'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option4_2 = models.CharField(
        choices=['Completely Fair', 'Fair', 'Unfair', 'Very Unfair'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    def role(self):
        if self.id_in_group == 1:
            return 'Player 1'
        if self.id_in_group == 2:
            return 'Player 2'

    def other_player(self):
        """Returns other player in group"""
        return self.get_others_in_group()[0]

    gender = models.CharField(
        choices=['Male', 'Female', 'Other'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    age = models.PositiveIntegerField()

    religion = models.CharField(
        # doc="""Please fill in the blank with, e.x.: Christian, Hindu.""",
        # widget=widgets.RadioSelect()
    )

    service = models.CharField(
        choices=['Never', 'Once a year', 'Once a month', 'Once a week', 'More than once a week'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    # Is treatment 4
    is_4 = models.IntegerField()

    # treatment
    treatment = models.IntegerField()
