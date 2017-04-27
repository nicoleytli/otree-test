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
    name_in_url = 'Empathy'
    players_per_group = 2
    num_rounds = 1
    conditions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.group_num = 999


class Group(BaseGroup):
    def get_scores(self):

        def compute(player):
            answer = [player.feeling1_response, player.feeling2_response, player.feeling3_response, player.feeling4_response, player.feeling5_response,
                      player.feeling6_response, player.feeling7_response, player.feeling8_response, player.feeling9_response, player.feeling10_response,
                      player.feeling11_response, player.feeling12_response, player.feeling13_response, player.feeling14_response, player.feeling15_response,
                      player.feeling16_response, player.feeling17_response, player.feeling18_response, player.feeling19_response, player.feeling20_response,
                      player.feeling21_response, player.feeling22_response, player.feeling23_response, player.feeling24_response, player.feeling25_response,
                      player.feeling26_response, player.feeling27_response, player.feeling28_response, player.feeling29_response, player.feeling30_response,
                      player.feeling31_response, player.feeling32_response, player.feeling33_response, player.feeling34_response, player.feeling35_response,
                      player.feeling36_response]

            correction = ['Playful', 'Upset', 'Desire', 'Insisting', 'Worried', 'Fantasizing', 'Uneasy', 'Despondent',
                          'Preoccupied', 'Cautious', 'Regretful', 'Skeptical', 'Anticipating', 'Accusing',
                          'Contemplative', 'Thoughtful', 'Doubtful', 'Decisive', 'Tentative', 'Friendly', 'Fantasizing',
                          'Preoccupied', 'Defiant', 'Pensive', 'Interested', 'Hostile', 'Cautious', 'Interested',
                          'Reflective', 'Flirtatious', 'Confident', 'Serious', 'Concerned', 'Distrustful', 'Nervous',
                          'Suspicious']
            filtered = filter(lambda x: x[0] == x[1], zip(answer, correction))

            player.score = len(list(filtered))

            return player.score

        for p in self.get_players():
            p.score = compute(p)

    # def get_priming(self):
    #     for p in self.get_players():
    #         i = self.id_in_subsession - 1
    #         p.priming = Constants.priming_list[i]
    #         p.participant.vars['priming'] = Constants.priming_list[i]

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

    def get_treatment(self):
        for p in self.get_players():
            if p.group_num == 10 or p.group_num == 11 or p.group_num == 12:
                p.is_4 = 1
                self.treatment = 4
            else:
                p.is_4 = 0
                if p.group_num == 1 or p.group_num == 2 or p.group_num == 3:
                    self.treatment = 1
                elif p.group_num == 4 or p.group_num == 5 or p.group_num == 6:
                    self.treatment = 2
                else:
                    self.treatment = 3

    treatment = models.IntegerField()

class Player(BasePlayer):
    # Used to transcribe a paragraph
    text = models.TextField()

    # 36 eye expressions
    feeling1_response = models.CharField(
        choices=['Playful', 'Comforting', 'Irritated', 'Bored'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling2_response = models.CharField(
        choices=['Terrified', 'Upset', 'Arrogant', 'Annoyed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling3_response = models.CharField(
        choices=['Joking', 'Flustered', 'Desire', 'Convinced'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling4_response = models.CharField(
        choices=['Joking', 'Insisting', 'Amused', 'Relaxed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling5_response = models.CharField(
        choices=['Irritated', 'Sarcastic', 'Worried', 'Friendly'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling6_response = models.CharField(
        choices=['Aghast', 'Fantasizing', 'Impatient', 'Alarmed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling7_response = models.CharField(
        choices=['Apologetic', 'Friendly', 'Uneasy', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling8_response = models.CharField(
        choices=['Despondent', 'Relieved', 'Shy', 'Excited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling9_response = models.CharField(
        choices=['Annoyed', 'Hostile', 'Horrified', 'Preoccupied'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling10_response = models.CharField(
        choices=['Cautious', 'Insisting', 'Bored', 'Aghast'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling11_response = models.CharField(
        choices=['Terrified', 'Amused', 'Regretful', 'Flirtatious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling12_response = models.CharField(
        choices=['Indifferent', 'Embarrassed', 'Skeptical', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling13_response = models.CharField(
        choices=['Decisive', 'Anticipating', 'Threatening', 'Shy'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling14_response = models.CharField(
        choices=['Irritated', 'Disappointed', 'Depressed', 'Accusing'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling15_response = models.CharField(
        choices=['Contemplative', 'Flustered', 'Encouraging', 'Amused'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling16_response = models.CharField(
        choices=['Irritated', 'Thoughtful', 'Encouraging', 'Sympathetic'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling17_response = models.CharField(
        choices=['Doubtful', 'Affectionate', 'Playful', 'Aghast'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling18_response = models.CharField(
        choices=['Decisive', 'Amused', 'Aghast', 'Bored'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling19_response = models.CharField(
        choices=['Arrogant', 'Grateful', 'Sarcastic', 'Tentative'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling20_response = models.CharField(
        choices=['Dominant', 'Friendly', 'Guilty', 'Horrified'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling21_response = models.CharField(
        choices=['Embarrassed', 'Fantasizing', 'Confused', 'Panicked'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling22_response = models.CharField(
        choices=['Preoccupied', 'Grateful', 'Insisting', 'Imploring'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling23_response = models.CharField(
        choices=['Contented', 'Apologetic', 'Defiant', 'Curious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling24_response = models.CharField(
        choices=['Pensive', 'Irritated', 'Excited', 'Hostile'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling25_response = models.CharField(
        choices=['Panicked', 'Incredulous', 'Despondent', 'Interested'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling26_response = models.CharField(
        choices=['Alarmed', 'Shy', 'Hostile', 'Anxious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling27_response = models.CharField(
        choices=['Joking', 'Cautious', 'Arrogant', 'Reassuring'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling28_response = models.CharField(
        choices=['Interested', 'Joking', 'Affectionate', 'Contented'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling29_response = models.CharField(
        choices=['Impatient', 'Aghast', 'Irritated', 'Reflective'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling30_response = models.CharField(
        choices=['Grateful', 'Flirtatious', 'Hostile', 'Disappointed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling31_response = models.CharField(
        choices=['Ashamed', 'Confident', 'Joking', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling32_response = models.CharField(
        choices=['Serious', 'Ashamed', 'Bewildered', 'Alarmed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling33_response = models.CharField(
        choices=['Embarrassed', 'Guilty', 'Fantasizing', 'Concerned'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling34_response = models.CharField(
        choices=['Aghast', 'Baffled', 'Distrustful', 'Terrified'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling35_response = models.CharField(
        choices=['Puzzled', 'Nervous', 'Insisting', 'Contemplative'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    feeling36_response = models.CharField(
        choices=['Ashamed', 'Nervous', 'Suspicious', 'Indecisive'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    # Computing eye scores
    score = models.IntegerField()

    # Decision for Treatment 1-3
    message = models.CharField(
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
    D_Q39_1 = models.CharField(
        choices=['Completely Fair', 'Fair', 'Unfair', 'Very Unfair'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    D_Q39_2 = models.CharField(
        choices=['Completely Fair', 'Fair', 'Unfair', 'Very Unfair'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    def role_p(self):
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

    services = models.CharField(
        choices=['Never', 'Once a year', 'Once a month', 'Once a week', 'More than once a week'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    # Is treatment 4
    is_4 = models.IntegerField()


    # group
    group_num = models.IntegerField()
