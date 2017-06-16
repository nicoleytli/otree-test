from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Exp1(Page):
    form_model = models.Player
    form_fields = ['x_1', 'exp1_answer', 'exp1_choice']

    def vars_for_template(self):
        return {'link': 'https://codebeautify.org/encrypt-decrypt'}

    def x_1_choices(self):
        messages = ['/KAxSKFMcYkpFjDSDqNcew==', 'Ig+PGrdlMX6WURRmREvLmg==', 'C4OFFgzvPVZut0FdrX18eg==',
                    'pm0BGu5kyrEdxWcoWyGHNQ==',
                    'eT4E7rVOzy/7O2EzI4IMbg==', '7q9vL0cinUIL6rD9cIBnQ==', 'Yi0DsAryIO6QoTWpLNJ7sQ==',
                    'ZclnNbfYgpbzGOHcTVlpow==',
                    '3gEwVeKgnJxsOZsdh0P6DQ==', 'dGOCHiIx0j8dNdZ83Ri4YQ==', 'w5C/k+hSkc3W3H7IIMNelg==',
                    'WPm34oB53pC4uRlAbClh8Q==',
                    'xDvR1AAWF0NvV1eaI4B6EA==', 'AQb8MqPPL/Ly4fbI63o6gQ==', 'cOIE2daAU8BWR8HZWMi1DA==',
                    'wSLzJLwpvIbaxZXgsmA3Cw==',
                    'Og+4eZlV9nun9Vxksgv2jg==', 'qed6GSTpWI9bKE3TtdsHUw==', 'HFn1lOcSjw2jKUyL/bG8BQ==',
                    'CJr6dtfYgrJviADxkUlVpQ==',
                    'XZUlGjwrYVlw1a3zBlpKFA==']
        random.shuffle(messages)
        return messages


class Exp2(Page):
    form_model = models.Player
    form_fields = ['x_2', 'exp2_answer']

    def vars_for_template(self):

        return {'link': 'https://codebeautify.org/encrypt-decrypt'}

    def x_2_choices(self):
        messages = ['cteZfhNerD1Lc+OAxVdVvQ==', 'ZOS06LLuQL5chzeaPOr7bw==', 'AmIO9Cf+O6xbJB/F5dEsNA==',
                    'H1BEazTqdZ5WW3Zw/vshZg==',
                    '5EaSJj73KsbmuQn5fboVXA==', 'CJ96ryYNtPjVpwHZKyxYw==', 'Nv0dpfwWqMk6J0rIMmAmlg==',
                    'zrEjMK6/Ibkiv01+Jn91ag==',
                    'pyRU4AQDnJhJcmxoVozRIQ==', 'vjpDZI9a6HYW/JauZgww7A==', 'yR2Ri7/6ZaQJeh2so+E/jg==',
                    'g4strqXmHH5gF3TsEp8rGw==',
                    'XOhjok9BJGQlaSdeKhPCMA==', 'ZYS8y7ULqIXnf6uJ37t4dQ==', '4DC1F7zcfD7j8OnfW9HIrw==',
                    'XOOO3DtqiFk724mUJYpVKg==',
                    'Xd2O+FoDyqrdw6F8zdaVEQ==', 'CrOWg1atILOeqjt6aPdNsQ==', '2TzcYwXdRl4FJGPyS0X9Ww==',
                    '1nJFfA2/v0CUI6NxeflnDA==',
                    'Fwn2a6sS3M6Y51ou0pyUuQ==']
        random.shuffle(messages)
        return messages


class Exp3(Page):
    form_model = models.Player
    form_fields = ['x_3', 'dollar_0', 'dollar_1', 'dollar_2', 'dollar_3', 'dollar_4', 'dollar_5', 'dollar_6',
                   'dollar_7', 'dollar_8', 'dollar_9', 'dollar_10', 'dollar_11', 'dollar_12', 'dollar_13', 'dollar_14',
                   'dollar_15', 'dollar_16', 'dollar_17', 'dollar_18', 'dollar_19', 'dollar_20']

    def vars_for_template(self):
        values = [1, 2, 3]
        dollar = ['$0', '$1', '$2', '$3', '$4', '$5', '$6', '$7', '$8', '$9', '$10', '$11', '$12', '$13', '$14',
                  '$15', '$16', '$17', '$18', '$19', '$20']
        name = ['dollar_0', 'dollar_1', 'dollar_2', 'dollar_3', 'dollar_4', 'dollar_5', 'dollar_6', 'dollar_7', 'dollar_8',
                'dollar_9', 'dollar_10', 'dollar_11', 'dollar_12', 'dollar_13', 'dollar_14', 'dollar_15', 'dollar_16',
                'dollar_17', 'dollar_18', 'dollar_19', 'dollar_20']
        mylist = zip(dollar, name)

        return {'link': 'https://codebeautify.org/encrypt-decrypt',
                'list': mylist,
                'values': values}

    def x_3_choices(self):
        messages = ['gOil2ipql8W0n0mDPcxARg==', 'tWJedphA5AwHZ1CvRxRyGw==', 'UBlRnLtyDcF7XziItOXwNA==',
                    'VNOj9fFzP9poGBm6Z+vpHw==',
                    'n/5cXvSnx3EalBwsXfwuKA==', 'VSmVj05ZsukbrrqYErsO0Q==', 'SIlqOwmAlC1wuup4cyERJw==',
                    '03AfBZisvxwZhBJdFfwR1A==',
                    'PYCKemmAg/zaznFW2rMOEg==', 'tYYTRDX48pjbS17DUkN1KA==', 'ptmrijqrLtr1Cpsxo7CCyg==',
                    'BX1EKcbgyk8vx3ATBZScEg==',
                    'f8/LlHr38IRVJrxVLUpYSA==', 'pEexpnJAh2zzAhQNHBUmJA==', '7WT3vw7OKX6MPQ6ryDdq+w==',
                    '6+6OU7AOyDYbMZuCgjAKCA==',
                    'oBKBUMn25Y0WmLWaLKDmyg==', 'vHvlOHVo80xcs75BtETOvQ==', 'vuwIP2w4c9bcJjVktapS8Q==',
                    '132o+8Yi6ILuTFX9sABGGA==',
                    'Qwrs1mISKtfCsRRnY5NaNg==']

        random.shuffle(messages)

        return messages

    def before_next_page(self):
        self.participant.vars['dollar_0'] = self.player.dollar_0
        self.participant.vars['dollar_1'] = self.player.dollar_1
        self.participant.vars['dollar_2'] = self.player.dollar_2
        self.participant.vars['dollar_3'] = self.player.dollar_3
        self.participant.vars['dollar_4'] = self.player.dollar_4
        self.participant.vars['dollar_5'] = self.player.dollar_5
        self.participant.vars['dollar_6'] = self.player.dollar_6
        self.participant.vars['dollar_7'] = self.player.dollar_7
        self.participant.vars['dollar_8'] = self.player.dollar_8
        self.participant.vars['dollar_9'] = self.player.dollar_9
        self.participant.vars['dollar_10'] = self.player.dollar_10
        self.participant.vars['dollar_11'] = self.player.dollar_11
        self.participant.vars['dollar_12'] = self.player.dollar_12
        self.participant.vars['dollar_13'] = self.player.dollar_13
        self.participant.vars['dollar_14'] = self.player.dollar_14
        self.participant.vars['dollar_15'] = self.player.dollar_15
        self.participant.vars['dollar_16'] = self.player.dollar_16
        self.participant.vars['dollar_17'] = self.player.dollar_17
        self.participant.vars['dollar_18'] = self.player.dollar_18
        self.participant.vars['dollar_19'] = self.player.dollar_19
        self.participant.vars['dollar_20'] = self.player.dollar_20



class Exp1_result(Page):
    def vars_for_template(self):
        self.player.result_A = random.choice(['Red', 'Red', 'Red', 'Red', 'White', 'White', 'White', 'Black', 'Black', 'Black'])
        self.player.result_B = random.choice(['Red', 'Red', 'White', 'White', 'White', 'Black', 'Black', 'Black', 'Black', 'Black'])

        messages = ['/KAxSKFMcYkpFjDSDqNcew==', 'Ig+PGrdlMX6WURRmREvLmg==', 'C4OFFgzvPVZut0FdrX18eg==',
                    'pm0BGu5kyrEdxWcoWyGHNQ==',
                    'eT4E7rVOzy/7O2EzI4IMbg==', '7q9vL0cinUIL6rD9cIBnQ==', 'Yi0DsAryIO6QoTWpLNJ7sQ==',
                    'ZclnNbfYgpbzGOHcTVlpow==',
                    '3gEwVeKgnJxsOZsdh0P6DQ==', 'dGOCHiIx0j8dNdZ83Ri4YQ==', 'w5C/k+hSkc3W3H7IIMNelg==',
                    'WPm34oB53pC4uRlAbClh8Q==',
                    'xDvR1AAWF0NvV1eaI4B6EA==', 'AQb8MqPPL/Ly4fbI63o6gQ==', 'cOIE2daAU8BWR8HZWMi1DA==',
                    'wSLzJLwpvIbaxZXgsmA3Cw==',
                    'Og+4eZlV9nun9Vxksgv2jg==', 'qed6GSTpWI9bKE3TtdsHUw==', 'HFn1lOcSjw2jKUyL/bG8BQ==',
                    'CJr6dtfYgrJviADxkUlVpQ==',
                    'XZUlGjwrYVlw1a3zBlpKFA==']
        num = messages.index(self.player.x_1)

        if self.player.exp1_answer > num:
            larger_smaller = 'smaller than'
            if self.player.exp1_choice == 'Option A':
                option = 'Option A'
                if self.player.result_A == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_A == 'White':
                    self.player.payoff_1 = 9
                else:
                    self.player.payoff_1 = 7
            else:
                option = 'Option B'
                if self.player.result_B == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_B == 'White':
                    self.player.payoff_1 = 9
                else:
                    self.player.payoff_1 = 7
        elif self.player.exp1_answer == num:
            larger_smaller = 'equal to'
            if self.player.exp1_choice == 'Option A':
                option = 'Option A'
                if self.player.result_A == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_A == 'White':
                    self.player.payoff_1 = 9
                else:
                    self.player.payoff_1 = 7
            else:
                option = 'Option B'
                if self.player.result_B == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_B == 'White':
                    self.player.payoff_1 = 9
                else:
                    self.player.payoff_1 = 7
        else:
            larger_smaller = 'larger than'
            if self.player.exp1_choice == 'Option B':
                option = 'Option A'
                if self.player.result_A == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_A == 'White':
                    self.player.payoff_1 = 9
                else:
                    self.player.payoff_1 = 7
            else:
                option = 'Option B'
                if self.player.result_B == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_B == 'White':
                    self.player.payoff_1 = 9
                else:
                    self.player.payoff_1 = 7

        return {'result_A': self.player.result_A,
                'result_B': self.player.result_B,
                'payoff': self.player.payoff_1,
                'message': self.player.x_1,
                'link': 'https://codebeautify.org/encrypt-decrypt',
                'larger_smaller': larger_smaller,
                'threshold': self.player.exp1_answer,
                'option': option}


class Exp2_result(Page):
    def vars_for_template(self):
        self.player.result_exp2 = random.choice(['Black', 'White'])

        messages = ['cteZfhNerD1Lc+OAxVdVvQ==', 'ZOS06LLuQL5chzeaPOr7bw==', 'AmIO9Cf+O6xbJB/F5dEsNA==', 'H1BEazTqdZ5WW3Zw/vshZg==',
                    '5EaSJj73KsbmuQn5fboVXA==', 'CJ96ryYNtPjVpwHZKyxYw==', 'Nv0dpfwWqMk6J0rIMmAmlg==', 'zrEjMK6/Ibkiv01+Jn91ag==',
                    'pyRU4AQDnJhJcmxoVozRIQ==', 'vjpDZI9a6HYW/JauZgww7A==', 'yR2Ri7/6ZaQJeh2so+E/jg==', 'g4strqXmHH5gF3TsEp8rGw==',
                    'XOhjok9BJGQlaSdeKhPCMA==', 'ZYS8y7ULqIXnf6uJ37t4dQ==', '4DC1F7zcfD7j8OnfW9HIrw==', 'XOOO3DtqiFk724mUJYpVKg==',
                    'Xd2O+FoDyqrdw6F8zdaVEQ==', 'CrOWg1atILOeqjt6aPdNsQ==', '2TzcYwXdRl4FJGPyS0X9Ww==', '1nJFfA2/v0CUI6NxeflnDA==',
                    'Fwn2a6sS3M6Y51ou0pyUuQ==']
        num = messages.index(self.player.x_2)

        if self.player.exp2_answer > num:
            option = 'Option A'
            larger_smaller = 'smaller than'
            if self.player.result_exp2 == 'Black':
                self.player.payoff_2 = 20
            else:
                self.player.payoff_2 = 0
        elif self.player.exp2_answer == num:
            option = 'Option A'
            larger_smaller = 'equal to'
            if self.player.result_exp2 == 'Black':
                self.player.payoff_2 = 20
            else:
                self.player.payoff_2 = 0
        else:
            option = 'Option B'
            larger_smaller = 'larger than'
            self.player.payoff_2 = num

        return {'option': option,
                'result': self.player.result_exp2,
                'payoff': self.player.payoff_2,
                'message': self.player.x_2,
                'larger_smaller': larger_smaller,
                'link': 'https://codebeautify.org/encrypt-decrypt',
                'threshold': self.player.exp2_answer}


class Exp3_result(Page):
    def vars_for_template(self):
        black_ball = random.randint(0, 40)
        white_ball = 40 - black_ball
        draw = random.randint(0, 60)

        if draw <= 20:
            self.player.result_exp3 = 'Red'
        elif 20 < draw <= (black_ball + 20):
            self.player.result_exp3 = 'Black'
        else:
            self.player.result_exp3 = 'White'

        messages = ['gOil2ipql8W0n0mDPcxARg==', 'tWJedphA5AwHZ1CvRxRyGw==', 'UBlRnLtyDcF7XziItOXwNA==',
                    'VNOj9fFzP9poGBm6Z+vpHw==',
                    'n/5cXvSnx3EalBwsXfwuKA==', 'VSmVj05ZsukbrrqYErsO0Q==', 'SIlqOwmAlC1wuup4cyERJw==',
                    '03AfBZisvxwZhBJdFfwR1A==',
                    'PYCKemmAg/zaznFW2rMOEg==', 'tYYTRDX48pjbS17DUkN1KA==', 'ptmrijqrLtr1Cpsxo7CCyg==',
                    'BX1EKcbgyk8vx3ATBZScEg==',
                    'f8/LlHr38IRVJrxVLUpYSA==', 'pEexpnJAh2zzAhQNHBUmJA==', '7WT3vw7OKX6MPQ6ryDdq+w==',
                    '6+6OU7AOyDYbMZuCgjAKCA==',
                    'oBKBUMn25Y0WmLWaLKDmyg==', 'vHvlOHVo80xcs75BtETOvQ==', 'vuwIP2w4c9bcJjVktapS8Q==',
                    '132o+8Yi6ILuTFX9sABGGA==',
                    'Qwrs1mISKtfCsRRnY5NaNg==']
        num = messages.index(self.player.x_3)

        option_num = self.participant.vars['dollar_%s' % num]

        if option_num == 1:
            option = 'Option A'
            self.player.random_draw = 0
        elif option_num == 2:
            option = 'Option B'
            self.player.random_draw = 0
        else:
            option = random.choice(['Option A', 'Option B'])
            self.player.random_draw = 1

        if option == 'Option A':
            if self.player.result_exp3 == 'Red':
                self.player.payoff_3 = 20
            elif self.player.result_exp3 == 'Black':
                self.player.payoff_3 = 0
            else:
                self.player.payoff_3 = num
        else:
            if self.player.result_exp3 == 'Red':
                self.player.payoff_3 = 0
            elif self.player.result_exp3 == 'Black':
                self.player.payoff_3 = num
            else:
                self.player.payoff_3 = 20

        return {'black_ball': black_ball,
                'white_ball': white_ball,
                'option': option,
                'result': self.player.result_exp3,
                'payoff': self.player.payoff_3,
                'link': 'https://codebeautify.org/encrypt-decrypt',
                'message': self.player.x_3}


class Page1(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3']


class Page2(Page):
    form_model = models.Player
    form_fields = ['q4', 'q5']


class Page3(Page):
    form_model = models.Player
    form_fields = ['citizenship', 'language', 'age', 'gender', 'program', 'year', 'field', 'time', 'exp1',
                   'other1', 'exp2', 'other2', 'exp3', 'other3']


class Result(Page):
    def vars_for_template(self):
        total = self.player.payoff_1 + self.player.payoff_2 + self.player.payoff_3
        return {'total': total}

page_sequence = [
    Exp1,
    Exp1_result,
    Exp2,
    Exp2_result,
    Exp3,
    Exp3_result,
    Page1,
    Page2,
    Page3,
    Result
]
