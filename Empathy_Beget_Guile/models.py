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


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.priming = random.choice(['Empathy', 'Control', 'Guile'])


class Group(BaseGroup):

    treatment = models.IntegerField()

    def get_treatment(self):
        p1 = self.get_player_by_role('Player 1')
        p2 = self.get_player_by_role('Player 2')

        self.treatment = random.randint(1, 4)
        p1.treatment = self.treatment
        p2.treatment = self.treatment

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
    # Used to transcribe a paragraph
    text = models.TextField()

    # 36 eye expressions
    option_1 = models.CharField(
        choices=['Playful', 'Comforting', 'Irritated', 'Bored'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_2 = models.CharField(
        choices=['Terrified', 'Upset', 'Arrogant', 'Annoyed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_3 = models.CharField(
        choices=['Joking', 'Flustered', 'Desire', 'Convinced'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_4 = models.CharField(
        choices=['Joking', 'Insisting', 'Amused', 'Relaxed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_5 = models.CharField(
        choices=['Irritated', 'Sarcastic', 'Worried', 'Friendly'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_6 = models.CharField(
        choices=['Aghast', 'Fantasizing', 'Impatient', 'Alarmed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_7 = models.CharField(
        choices=['Apologetic', 'Friendly', 'Uneasy', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_8 = models.CharField(
        choices=['Despondent', 'Relieved', 'Shy', 'Excited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_9 = models.CharField(
        choices=['Annoyed', 'Hostile', 'Horrified', 'Preoccupied'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_10 = models.CharField(
        choices=['Cautious', 'Insisting', 'Bored', 'Aghast'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_11 = models.CharField(
        choices=['Terrified', 'Amused', 'Regretful', 'Flirtatious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_12 = models.CharField(
        choices=['Indifferent', 'Embarrassed', 'Skeptical', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_13 = models.CharField(
        choices=['Decisive', 'Anticipating', 'Threatening', 'Shy'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_14 = models.CharField(
        choices=['Irritated', 'Disappointed', 'Depressed', 'Accusing'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_15 = models.CharField(
        choices=['Contemplative', 'Flustered', 'Encouraging', 'Amused'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_16 = models.CharField(
        choices=['Irritated', 'Thoughtful', 'Encouraging', 'Sympathetic'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_17 = models.CharField(
        choices=['Doubtful', 'Affectionate', 'Playful', 'Aghast'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_18 = models.CharField(
        choices=['Decisive', 'Amused', 'Aghast', 'Bored'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_19 = models.CharField(
        choices=['Arrogant', 'Grateful', 'Sarcastic', 'Tentative'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_20 = models.CharField(
        choices=['Dominant', 'Friendly', 'Guilty', 'Horrified'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_21 = models.CharField(
        choices=['Embarrassed', 'Fantasizing', 'Confused', 'Panicked'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_22 = models.CharField(
        choices=['Preoccupied', 'Grateful', 'Insisting', 'Imploring'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_23 = models.CharField(
        choices=['Contented', 'Apologetic', 'Defiant', 'Curious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_24 = models.CharField(
        choices=['Pensive', 'Irritated', 'Excited', 'Hostile'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_25 = models.CharField(
        choices=['Panicked', 'Incredulous', 'Despondent', 'Interested'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_26 = models.CharField(
        choices=['Alarmed', 'Shy', 'Hostile', 'Anxious'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_27 = models.CharField(
        choices=['Joking', 'Cautious', 'Arrogant', 'Reassuring'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_28 = models.CharField(
        choices=['Interested', 'Joking', 'Affectionate', 'Contented'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_29 = models.CharField(
        choices=['Impatient', 'Aghast', 'Irritated', 'Reflective'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_30 = models.CharField(
        choices=['Grateful', 'Flirtatious', 'Hostile', 'Disappointed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_31 = models.CharField(
        choices=['Ashamed', 'Confident', 'Joking', 'Dispirited'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_32 = models.CharField(
        choices=['Serious', 'Ashamed', 'Bewildered', 'Alarmed'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_33 = models.CharField(
        choices=['Embarrassed', 'Guilty', 'Fantasizing', 'Concerned'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_34 = models.CharField(
        choices=['Aghast', 'Baffled', 'Distrustful', 'Terrified'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_35 = models.CharField(
        choices=['Puzzled', 'Nervous', 'Insisting', 'Contemplative'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )
    option_36 = models.CharField(
        choices=['Ashamed', 'Nervous', 'Suspicious', 'Indecisive'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

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

    # Priming paragraph
    priming = models.CharField()

    # Treatment
    treatment = models.IntegerField()

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
        choices=['Christian', 'Hindu', 'Muslim', 'Atheist'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    service = models.CharField(
        choices=['Never', 'Once a year', 'Once a month', 'Once a week', 'More than once a week'],
        doc="""Please choose one of the options""",
        widget=widgets.RadioSelect()
    )

    get_code1 = models.CharField()
    get_code2 = models.CharField()