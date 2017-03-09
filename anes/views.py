from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class Demographic(Page):
    form_model = models.Player
    form_fields = ['gender', 'age', 'religion']


class Results(Page):
    pass


class Q1(Page):
    form_model = models.Player
    form_fields = ['question_1']


class L1(Page):
    form_model = models.Player
    form_fields = ['likert_1']

    def vars_for_template(self):
        if self.player.question_1 == 'Favor':
            altitude = 'favor'
        elif self.player.question_1 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_1 != 'Neither favor nor oppose'


class Q2(Page):
    form_model = models.Player
    form_fields = ['question_2']


class L2(Page):
    form_model = models.Player
    form_fields = ['likert_2']

    def vars_for_template(self):
        if self.player.question_2 == 'Favor':
            altitude = 'favor'
        elif self.player.question_2 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_2 != 'Neither favor nor oppose'


class Q3(Page):
    form_model = models.Player
    form_fields = ['question_3']


class L3(Page):
    form_model = models.Player
    form_fields = ['likert_3']

    def vars_for_template(self):
        if self.player.question_3 == 'Favor':
            altitude = 'favor'
        elif self.player.question_3 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_3 != 'Neither favor nor oppose'


class Q4(Page):
    form_model = models.Player
    form_fields = ['question_4']

class L4(Page):
    form_model = models.Player
    form_fields = ['likert_4']

    def vars_for_template(self):
        if self.player.question_4 == 'Favor':
            altitude = 'favor'
        elif self.player.question_4 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_4 != 'Neither favor nor oppose'


class Q5(Page):
    form_model = models.Player
    form_fields = ['question_5']


class L5(Page):
    form_model = models.Player
    form_fields = ['likert_5']

    def vars_for_template(self):
        if self.player.question_5 == 'Favor':
            altitude = 'favor'
        elif self.player.question_5 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_5 != 'Neither favor nor oppose'


class Q6(Page):
    form_model = models.Player
    form_fields = ['question_6']


class L6(Page):
    form_model = models.Player
    form_fields = ['likert_6']

    def vars_for_template(self):
        if self.player.question_6 == 'Favor':
            altitude = 'favor'
        elif self.player.question_6 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_6 != 'Neither favor nor oppose'


class Q7(Page):
    form_model = models.Player
    form_fields = ['question_7']


class L7(Page):
    form_model = models.Player
    form_fields = ['likert_7']

    def vars_for_template(self):
        if self.player.question_7 == 'Favor':
            altitude = 'favor'
        elif self.player.question_7 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_7 != 'Neither favor nor oppose'


class Q8(Page):
    form_model = models.Player
    form_fields = ['question_8']


class L8(Page):
    form_model = models.Player
    form_fields = ['likert_8']

    def vars_for_template(self):
        if self.player.question_8 == 'Favor':
            altitude = 'favor'
        elif self.player.question_8 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_8 != 'Neither favor nor oppose'


class Q9(Page):
    form_model = models.Player
    form_fields = ['question_9']


class L9(Page):
    form_model = models.Player
    form_fields = ['likert_9']

    def vars_for_template(self):
        if self.player.question_9 == 'Favor':
            altitude = 'favor'
        elif self.player.question_9 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_9 != 'Neither favor nor oppose'


class Q10(Page):
    form_model = models.Player
    form_fields = ['question_10']


class L10(Page):
    form_model = models.Player
    form_fields = ['likert_10']

    def vars_for_template(self):
        if self.player.question_10 == 'Favor':
            altitude = 'favor'
        elif self.player.question_10 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_10 != 'Neither favor nor oppose'


class Q11(Page):
    form_model = models.Player
    form_fields = ['question_11']


class L11(Page):
    form_model = models.Player
    form_fields = ['likert_11']

    def vars_for_template(self):
        if self.player.question_11 == 'Favor':
            altitude = 'favor'
        elif self.player.question_11 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_11 != 'Neither favor nor oppose'


class Q12(Page):
    form_model = models.Player
    form_fields = ['question_12']


class L12(Page):
    form_model = models.Player
    form_fields = ['likert_12']

    def vars_for_template(self):
        if self.player.question_12 == 'Favor':
            altitude = 'favor'
        elif self.player.question_12 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_12 != 'Neither favor nor oppose'


class Q13(Page):
    form_model = models.Player
    form_fields = ['question_13']


class L13(Page):
    form_model = models.Player
    form_fields = ['likert_13']

    def vars_for_template(self):
        if self.player.question_13 == 'Favor':
            altitude = 'favor'
        elif self.player.question_13 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_13 != 'Neither favor nor oppose'


class Q14(Page):
    form_model = models.Player
    form_fields = ['question_14']


class L14(Page):
    form_model = models.Player
    form_fields = ['likert_14']

    def vars_for_template(self):
        if self.player.question_14 == 'Favor':
            altitude = 'favor'
        elif self.player.question_14 == 'Oppose':
            altitude = 'oppose'
        return {'altitude': altitude}

    def is_displayed(self):
        return self.player.question_14 != 'Neither favor nor oppose'


page_sequence = [
    MyPage,
    # ResultsWaitPage,
    # Results
    Q1,
    L1,
    Q2,
    L2,
    Q3,
    L3,
    Q4,
    L4,
    Q5,
    L5,
    Q6,
    L6,
    Q7,
    L7,
    Q8,
    L8,
    Q9,
    L9,
    Q10,
    L10,
    Q11,
    L11,
    Q12,
    L12,
    Q13,
    L13,
    Q14,
    L14,
    Demographic,
    Results
]
