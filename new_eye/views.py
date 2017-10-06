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
        image = "new_eye/eye%s.png" % (self.session.vars['final_list'][self.round_number - 1] + 1)
        return {
            'choice1': choice1,
            'choice2': choice2,
            'choice3': choice3,
            'choice4': choice4,
            'image': image
        }


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Introduction,
    MyPage,
    Results
]
