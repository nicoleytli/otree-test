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
    name_in_url = 'Eye_Exam'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            if 1 <= p.id_in_group <= 8:
                p.priming = 'Empathy'
            elif 9 <= p.id_in_group <= 16:
                p.priming = 'Control'
            else:
                p.priming = 'Guile'


class Group(BaseGroup):
    def get_scores(self):

        def compute(player):
            answer = [player.option_1, player.option_2, player.option_3, player.option_4, player.option_5,
                      player.option_6, player.option_7, player.option_8, player.option_9, player.option_10,
                      player.option_11, player.option_12, player.option_13, player.option_14, player.option_15,
                      player.option_16, player.option_17, player.option_18, player.option_19, player.option_20,
                      player.option_21, player.option_22, player.option_23, player.option_24, player.option_25,
                      player.option_26, player.option_27, player.option_28, player.option_29, player.option_30,
                      player.option_31, player.option_32, player.option_33, player.option_34, player.option_35,
                      player.option_36]

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

    # Priming paragraph
    priming = models.CharField()

    # Computing eye scores
    score = models.IntegerField()
