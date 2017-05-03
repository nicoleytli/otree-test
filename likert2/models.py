from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'likert2'
    players_per_group = None

    with open('likert2/quiz.csv') as f:
        questions = list(csv.DictReader(f))

    num_rounds = len(questions)



class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.PositiveIntegerField()
    question = models.CharField()
    submitted_answer = models.CharField(
        widget=widgets.RadioSelect()
    )

    likert = models.IntegerField()
    important = models.IntegerField()


    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

    #
    # def care(self):
    #     self.participant.vars['care_%s' % self.round_number] = 999

    care1f = models.IntegerField(
        widget=widgets.RadioSelect()
    )

    care1o = models.IntegerField(
        widget=widgets.RadioSelect()
    )

    care2f = models.IntegerField(
        widget=widgets.RadioSelect(),
    )

    care2o = models.IntegerField(
        widget=widgets.RadioSelect(),
    )

    care3f = models.IntegerField(
        widget=widgets.RadioSelect(),
    )

    care3o = models.IntegerField(
        widget=widgets.RadioSelect(),
    )



