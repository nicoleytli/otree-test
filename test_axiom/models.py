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

    x_0 = models.CharField(
        widget=widgets.RadioSelect()
    )

    message0 = models.TextField()
    message0_other = models.TextField(
        blank=True
    )
    check = models.BooleanField()

    exp1_answer = models.CurrencyField(
        min=0, max=20
    )
    exp1_choice = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Option A', 'Option B']
    )
    result_A = models.CharField()
    result_B = models.CharField()
    x_1 = models.CharField(
        widget=widgets.RadioSelect()
    )
    payoff_1 = models.CurrencyField()


    exp2_answer = models.CurrencyField(
        min=0, max=20
    )
    result_exp2 = models.CharField()
    x_2 = models.CharField(
        widget=widgets.RadioSelect()
    )
    payoff_2 = models.CurrencyField()
    exp3_answer = models.CurrencyField(
        min=0, max=20
    )

    result_exp3 = models.CharField()
    random_draw = models.BooleanField()
    x_3 = models.CharField(
        widget=widgets.RadioSelect()
    )

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
        min=10, max=100
    )
    gender = models.CharField(
        choices=['Female', 'Male', 'Other'],
        widget=widgets.RadioSelectHorizontal()
    )
    educ = models.IntegerField(
        choices=[[1, 'Less than 1st grade'],
                 [2, '1st, 2nd, 3rd or 4th grade'],
                 [3, '5th or 6th grade'],
                 [4, '7th or 8th grade'],
                 [5, '9th grade'],
                 [6, '10th grade'],
                 [7, '1th grade'],
                 [8, '12th grade no diploma'],
                 [9, 'High school graduate - high school diploma or equivalent (for example: GED)'],
                 [10, 'Some college but no degree'],
                 [11, 'Associate degree in college - Occupational/vocational program'],
                 [12, 'Associate degree in college -- Academic program'],
                 [13, 'Bachelor\'s degree (For example: BA, AB, BS)'],
                 [14, 'Master\'s degree (For example: MA, MS, MEng, MEd, MSW, MBA)'],
                 [15, 'Professional School Degree (For example: MD,DDS,DVM,LLB,JD)'],
                 [16, 'Doctorate degree (For example: PhD, EdD)'],
                 [95, 'Others']]
    )
    time = models.CharField(
        choices=['Never', 'Once', '2 times', '3 times', 'More than 3 times'],
        widget=widgets.RadioSelectHorizontal()
    )
    religion = models.CharField()
    income = models.CharField(
        choices=['Less than $20000', 'Between $20000 to $40000', 'Between $40001 to $60000', 'Between $60001 to $80000',
                 'More than $80000'],
        doc="""Please choose one of the choices""",
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







