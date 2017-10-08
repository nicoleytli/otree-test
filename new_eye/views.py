from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    form_model = models.Player
    form_fields = ['answer']

    def answer_choices(self):
        ans = self.player.current_answers()
        return [
            ans['choice1'],
            ans['choice2'],
            ans['choice3'],
            ans['choice4']
        ]

    # def before_next_page(self):
    #     self.participant.vars['ans_%s' % self.round_number] = self.player.answer
    #     if self.round_number == Constants.num_rounds:
    #         self.player.get_scores()

    def vars_for_template(self):
        ans = self.player.current_answers()
        choice1 = ans['choice1']
        choice2 = ans['choice2']
        choice3 = ans['choice3']
        choice4 = ans['choice4']
        title1 = ans['title1']
        title2 = ans['title2']
        title3 = ans['title3']
        title4 = ans['title4']
        self.player.question_num = self.participant.vars['pic_final_list'][self.round_number - 1] + 1
        image = "new_eye/eye%s.png" % self.player.question_num
        return {
            'choice1': choice1,
            'choice2': choice2,
            'choice3': choice3,
            'choice4': choice4,
            'image': image,
            'title1': title1,
            'title2': title2,
            'title3': title3,
            'title4': title4
        }


class Completion(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Introduction,
    MyPage,
    Completion,
    Results
]
