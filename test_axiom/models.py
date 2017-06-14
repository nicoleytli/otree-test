from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'test_axiom'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    exp1_answer = models.CurrencyField(
        min=0, max=20
    )
    exp1_choice = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Option A', 'Option B']
    )
    result_A = models.CharField()
    result_B = models.CharField()
    x_1 = models.CharField()
    payoff_1 = models.CurrencyField()


    exp2_answer = models.CurrencyField(
        min=0, max=20
    )
    result_exp2 = models.CharField()
    x_2 = models.CharField()
    payoff_2 = models.CurrencyField()
    exp3_answer = models.CurrencyField(
        min=0, max=20
    )

    result_exp3 = models.CharField()
    random_draw = models.BooleanField()
    x_3 = models.CharField()

    dollar_0 = models.IntegerField()
    dollar_1 = models.IntegerField()
    dollar_2 = models.IntegerField()
    dollar_3 = models.IntegerField()
    dollar_4 = models.IntegerField()
    dollar_5 = models.IntegerField()
    dollar_6 = models.IntegerField()
    dollar_7 = models.IntegerField()
    dollar_8 = models.IntegerField()
    dollar_9 = models.IntegerField()
    dollar_10 = models.IntegerField()
    dollar_11 = models.IntegerField()
    dollar_12 = models.IntegerField()
    dollar_13 = models.IntegerField()
    dollar_14 = models.IntegerField()
    dollar_15 = models.IntegerField()
    dollar_16 = models.IntegerField()
    dollar_17 = models.IntegerField()
    dollar_18 = models.IntegerField()
    dollar_19 = models.IntegerField()
    dollar_20 = models.IntegerField()

    payoff_3 = models.CurrencyField()

    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.CharField(
        choices=['Lottery A: $1,000,000 for sure',
                 'Lottery B: 1% chance of nothing; 89% chance of $1,000,000; 10% chance of $5.000.000'],
        widget=widgets.RadioSelect()
    )
    q5 = models.CharField(
        choices=['Lottery A: 89% chance of nothing; 11% chance of $1,000,000',
                 'Lottery B: 90% chance of nothing; 10% chance of $5.000.000'],
        widget=widgets.RadioSelect()
    )

    citizenship = models.CharField()
    language = models.CharField()
    age = models.IntegerField(
        min=0, max=100
    )
    gender = models.CharField(
        choices=['Female', 'Male', 'Other'],
        widget=widgets.RadioSelectHorizontal()
    )
    program = models.CharField(
        choices=['Bachelor\'s program', 'Master\'s program', 'Not a student'],
        widget=widgets.RadioSelectHorizontal()
    )
    year = models.CharField(
        choices=['2017', '2018', 'Later', 'I am not a student'],
        widget=widgets.RadioSelectHorizontal()
    )
    field = models.CharField()
    time = models.CharField(
        choices=['Never', 'Once', '2 times', '3 times', 'More than 3 times'],
        widget=widgets.RadioSelectHorizontal()
    )
    exp1 = models.CharField(
        choices=['I didn\'t understand the instructions',
                 'I understood the instructions, but I didn\'t know what answer to give',
                 'Everything was clear',
                 'Other (provide extra details)'],
        widget=widgets.RadioSelect()
    )
    other1 = models.TextField(
        blank=True
    )
    exp2 = models.CharField(
        choices=['I didn\'t understand the instructions',
                 'I understood the instructions, but I didn\'t know what answer to give',
                 'Everything was clear',
                 'Other (provide extra details)'],
        widget=widgets.RadioSelect()
    )
    other2 = models.TextField(
        blank=True
    )
    exp3 = models.CharField(
        choices=['I didn\'t understand the instructions',
                 'I understood the instructions, but I didn\'t know what answer to give',
                 'Everything was clear',
                 'Other (provide extra details)'],
        widget=widgets.RadioSelect()
    )
    other3 = models.TextField(
        blank=True
    )







