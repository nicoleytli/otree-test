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
    name_in_url = 'likert'
    players_per_group = None

    with open('likert/quiz.csv') as f:
        questions = list(csv.DictReader(f))

    num_rounds = len(questions)



class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions
            # randomized_list = random.sample(Constants.list_question, len(Constants.list_question))
            # self.session.vars['list'] = randomized_list
            ## ALTERNATIVE DESIGN:
            ## to randomize the order of the questions, you could instead do:

            # import random
            # randomized_questions = random.sample(Constants.questions, len(Constants.questions))
            # self.session.vars['questions'] = randomized_questions

            ## and to randomize differently for each participant, you could use
            ## the random.sample technique, but assign into participant.vars
            ## instead of session.vars.

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

    likert = models.IntegerField(
        widget=widgets.RadioSelectHorizontal()
    )


    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]
