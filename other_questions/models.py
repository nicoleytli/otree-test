from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'other_questions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # item
    Q1 = models.IntegerField(
        choices=[[1, 'Yes, voted'],
                 [2, 'No, did not vote']],
        widget=widgets.RadioSelect()
    )

    Q2 = models.IntegerField(
        choices=[[1, 'Hillary Clinton'],
                 [2, 'Donald Trump'],
                 [3, 'Other']],
        widget=widgets.RadioSelect()
    )

    Q3 = models.IntegerField(
        widget=widgets.RadioSelect()
    )
    Q4 = models.IntegerField(
        choices=[[1, 'Yes, I did'],
                 [2, 'No, I did not']],
        widget=widgets.RadioSelect()
    )
    Q4_2 = models.IntegerField(
        choices=[[1, 'Support'],
                 [2, 'Oppose'],
                 [3, 'Neither']],
        widget=widgets.RadioSelect()
    )
    Q4_3 = models.TextField()
    Q5 = models.IntegerField()
    Q6 = models.IntegerField(
        choices=[[1, 'Liberal'],
                 [2, 'Conservative']],
        widget=widgets.RadioSelect()
    )
    Q7 = models.IntegerField()
    Q8 = models.IntegerField()
    Q9 = models.IntegerField()
    Q10 = models.IntegerField()
    Q11 = models.IntegerField()
    Q12 = models.IntegerField()
    Q13 = models.IntegerField()

    # ses
    birth = models.IntegerField(
        max=2016,
        min=1900
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

    dip = models.IntegerField(
        choices=[[1, 'Graduation from High School'],
                 [2, 'GED or other equivalent']]
    )

    duty = models.IntegerField(
        choices=[[1, 'Now serving on active duty'],
                 [2, 'Previously served on active duty but not now on active duty'],
                 [3, 'Have never served on active duty']]
    )

    emptype = models.IntegerField(
        choices=[[1, 'Working now'],
                 [2, 'Temporarily laid off'],
                 [3, 'Unemployed'],
                 [4, 'Retired'],
                 [5, 'Permanently disabled'],
                 [6, 'Homemaker'],
                 [7, 'Student']]
    )

    work = models.IntegerField(
        choices=[[1, 'Yes'],
                 [2, 'No']]
    )

    myclass = models.IntegerField(
        choices=[[1, 'Yes'],
                 [2, 'No']]
    )

    whichclass = models.IntegerField(
        choices=[[1, 'Lower class or poor'],
                 [2, 'Middle class'],
                 [3, 'Working class'],
                 [4, 'Both middle and working class'],
                 [5, 'Upper class'],
                 [6, 'Other']]
    )

    chclass = models.IntegerField(
        choices=[[1, 'Middle class'],
                 [2, 'Working class']]
    )

    middle = models.IntegerField(
        choices=[
            [1, 'Average middle class'],
            [2, 'Upper middle class']]
    )

    working = models.IntegerField(
        choices=[
            [1, 'Average working class'],
            [2, 'Upper working class']]
    )

    race1 = models.CharField(
        blank=True
    )
    race2 = models.CharField(
        blank=True
    )
    race3 = models.CharField(
        blank=True
    )
    race4 = models.CharField(
        blank=True
    )
    race5 = models.CharField(
        blank=True
    )
    race6 = models.CharField(
        blank=True
    )

    hisp = models.IntegerField(
        choices=[[1, 'Yes'],
                 [2, 'No']]
    )

    gender = models.IntegerField(
        choices=[[1, 'Male'],
                 [2, 'Female'],
                 [3, 'Other']]
    )
