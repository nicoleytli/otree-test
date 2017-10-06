from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random

author = 'Yutong Li'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'new_eye'
    players_per_group = None

    with open('new_eye/answers.csv') as f:
        all_answers = list(csv.DictReader(f))

    num_rounds = len(all_answers)


class Subsession(BaseSubsession):

    ans_loc = models.CharField()
    ran_loc = models.CharField()

    def creating_session(self):
        if self.round_number == 1:
            number_of_random = 30
            # a list of random answers' location
            random_loc = random.sample(list(range(36)), number_of_random)
            # a list of drawn random answers
            answers_loc = []
            for i in range(len(random_loc)):
                loc = list(range(36))
                loc.remove(i)
                answers_loc.append(random.choice(loc))

            final_list = list(range(36))

            for i, j in zip(random_loc, answers_loc):
                final_list[i] = answers_loc.index(j)

            self.session.vars['final_list'] = final_list

            if self.round_number == 1:
                self.session.vars['all_answers'] = Constants.all_answers

            # for p in self.get_players():
            #     answers_data = p.current_answers()
            #     p.correct_answer = answers_data['correction']

            self.ans_loc = answers_loc
            self.ran_loc = random_loc



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.CharField(
        widget=widgets.RadioSelect()
    )
    # correct_answer = models.CharField()
    # score = models.IntegerField()

    def current_answers(self):
        num = self.session.vars['final_list'][self.round_number - 1]
        return self.session.vars['all_answers'][num]

    # def get_scores(self):
    #     answer = []
    #     for i in range(1, 37):
    #         answer.append(self.participant.vars['ans_%s' % i])
    #
    #     correction = ['Playful', 'Upset', 'Desire', 'Insisting', 'Worried', 'Fantasizing', 'Uneasy', 'Despondent',
    #                   'Preoccupied', 'Cautious', 'Regretful', 'Skeptical', 'Anticipating', 'Accusing',
    #                   'Contemplative', 'Thoughtful', 'Doubtful', 'Decisive', 'Tentative', 'Friendly', 'Fantasizing',
    #                   'Preoccupied', 'Defiant', 'Pensive', 'Interested', 'Hostile', 'Cautious', 'Interested',
    #                   'Reflective', 'Flirtatious', 'Confident', 'Serious', 'Concerned', 'Distrustful', 'Nervous',
    #                   'Suspicious']
    #
    #     filtered = filter(lambda x: x[0] == x[1], zip(answer, correction))
    #     self.score = len(list(filtered))
