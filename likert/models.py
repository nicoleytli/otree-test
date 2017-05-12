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
    num_rounds = 1

    # with open('likert/quiz.csv') as f:
    #     questions = list(csv.DictReader(f))
    #
    # num_rounds = len(questions)

    amount_allocated = c(10)

    conditions = ['1LG', '1QG', '1QNG', '1LP', '1QP', '1QNP', '1LD', '1QD', '1QND', '1LI', '1QI',
                  '1QNI', '1LM', '1QM', '1QNM', '2LG', '2QG', '2QNG', '2LP', '2QP', '2QNP', '2LD',
                  '2QD', '2QND', '2LI', '2QI', '2QNI', '2LM', '2QM', '2QNM', '3LG', '3QG', '3QNG',
                  '3LP', '3QP', '3QNP', '3LD', '3QD', '3QND', '3LI', '3QI', '3QNI', '3LM', '3QM', '3QNM']

    organization = ['organization 1', 'organization 2', 'The American Chamber of Commerce', 'organization 4',
                    'organization 5', 'Center for Immigration Studies', 'organization 7', 'organization 8',
                    'organization 9', 'organization 10']

    description = ['description 1', 'description 2',
                   'The ACC is a non-partisan association that lobbies Congress to maintain low tariffs on imports because an increase would raise consumer prices and hurt American exports',
                   'description 4',
                   'description 5',
                   'The CIS is a conservative non-profit research organization "that favors far lower immigration numbers and produces research to further those views.” It also lobbies congress for policies in that direction',
                   'description 7',
                   'description 8',
                   'description 9',
                   'description 10']



class Subsession(BaseSubsession):
    # def before_session_starts(self):
    #     if self.round_number == 1:
    #         self.session.vars['questions'] = Constants.questions
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
    def before_session_starts(self):
        for p in self.get_players():
            p.preference_party = random.choice(['same', 'opposite'])
            p.mouse_option = 999
            p.condition = 'None'




class Group(BaseGroup):
    pass


class Player(BasePlayer):

    priming1 = models.CharField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )

    priming2_dem_1 = models.CharField()
    priming2_dem_2 = models.CharField()
    priming2_dem_3 = models.CharField()
    priming2_dem_4 = models.CharField()
    priming2_dem_5 = models.CharField()
    priming2_dem_6 = models.CharField()
    priming2_dem_7 = models.CharField()
    priming2_dem_8 = models.CharField()
    priming2_dem_9 = models.CharField()
    priming2_dem_10 = models.CharField()

    priming2_rep_1 = models.CharField()
    priming2_rep_2 = models.CharField()
    priming2_rep_3 = models.CharField()
    priming2_rep_4 = models.CharField()
    priming2_rep_5 = models.CharField()
    priming2_rep_6 = models.CharField()
    priming2_rep_7 = models.CharField()
    priming2_rep_8 = models.CharField()
    priming2_rep_9 = models.CharField()
    priming2_rep_10 = models.CharField()

    # condition
    condition = models.CharField()

    submitted_answer_1 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_2 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_3 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_4 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_5 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_6 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_7 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_8 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_9 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )
    submitted_answer_10 = models.CharField(
        widget=widgets.RadioSelect(),
        choices=['Favor', 'Oppose', 'Neither favor nor oppose']
    )


    likert_1 = models.IntegerField()
    likert_2 = models.IntegerField()
    likert_3 = models.IntegerField()
    likert_4 = models.IntegerField()
    likert_5 = models.IntegerField()
    likert_6 = models.IntegerField()
    likert_7 = models.IntegerField()
    likert_8 = models.IntegerField()
    likert_9 = models.IntegerField()
    likert_10 = models.IntegerField()


    important_1 = models.IntegerField()
    important_2 = models.IntegerField()
    important_3 = models.IntegerField()
    important_4 = models.IntegerField()
    important_5 = models.IntegerField()
    important_6 = models.IntegerField()
    important_7 = models.IntegerField()
    important_8 = models.IntegerField()
    important_9 = models.IntegerField()
    important_10 = models.IntegerField()


    #
    # def current_question(self):
    #     return self.session.vars['questions'][self.round_number - 1]

    #
    # def care(self):
    #     self.participant.vars['care_%s' % self.round_number] = 999


    # likertquest
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

    # donation
    donation = models.CurrencyField(
        blank=True,
        min=0, max=Constants.amount_allocated,
        doc='Please choose from $0 to $10'
    )

    org = models.IntegerField(
        blank=True,
        doc='Please enter the number of organization you want',
        min=0, max=3
    )

    org_option1 = models.CharField()
    org_option2 = models.CharField()
    org_option3 = models.CharField()

    email = models.CharField(
        blank=True,
        doc='For example: XXXX@gmail.com'
    )

    annotation = models.CharField()

    # infoseeking
    info1 = models.CharField(
        blank=True
    )
    info2 = models.CharField(
        blank=True
    )
    info3 = models.CharField(
        blank=True
    )
    info4 = models.CharField(
        blank=True
    )
    info5 = models.CharField(
        blank=True
    )
    info6 = models.CharField(
        blank=True
    )
    info7 = models.CharField(
        blank=True
    )
    info8 = models.CharField(
        blank=True
    )
    info9 = models.CharField(
        blank=True
    )
    info10 = models.CharField(
        blank=True
    )

    email_info = models.CharField()

    # petition
    petition_1 = models.CharField(
        blank=True
    )

    petition_2 = models.CharField(
        blank=True
    )

    petition_3 = models.CharField(
        blank=True
    )

    petition_4 = models.CharField(
        blank=True
    )

    petition_5 = models.CharField(
        blank=True
    )

    petition_6 = models.CharField(
        blank=True
    )

    petition_7 = models.CharField(
        blank=True
    )

    petition_8 = models.CharField(
        blank=True
    )

    petition_9 = models.CharField(
        blank=True
    )

    petition_10 = models.CharField(
        blank=True
    )

    email_petition = models.CharField(
        blank=True
    )


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
        widget = widgets.RadioSelect()
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

    partisanship1 = models.IntegerField(
        choices=[[1, 'Democrat'],
                 [2, 'Republican'],
                 [3, 'Independent'],
                 [5, 'Other party'],
                 [8, 'Do not know']],
        widget=widgets.RadioSelect()
    )

    partisanship2 = models.IntegerField(
        choices=[[1, 'Strong'],
                 [2, 'Not very strong'],
                 [5, 'Inapplicable'],
                 [8, 'Do not know']],
        widget=widgets.RadioSelect()
    )

    partisanship3 = models.IntegerField(
        choices=[[1, 'Closer to Republican'],
                 [2, 'Closer to Democratic'],
                 [3, 'Neither']],
        widget=widgets.RadioSelect()
    )


    # mytrust
    partner = models.IntegerField(
        widget=widgets.RadioSelect()
    )
    preference_party = models.CharField()
    donation_party = models.IntegerField(
        choices=[[1, 'I choose to guess his/her party identification'],
                 [2, 'I choose to guess his/her donation decision']],
        widget=widgets.RadioSelect()
    )
    if_random = models.IntegerField()

    donation1 = models.CharField()
    donation2 = models.CharField()
    donation3 = models.CharField()
    donation_correct = models.CharField()
    donation_choice = models.IntegerField(
        choices=[1, 2, 3],
        widget=widgets.RadioSelect()
    )

    description1 = models.CharField()
    description2 = models.CharField()
    description3 = models.CharField()

    other_opinion = models.CharField()
    other_preference = models.CharField()
    other_party = models.CharField()
    other_party_level = models.CharField()
    party_identification = models.CharField()
    party_choice = models.CharField(
        widget=widgets.RadioSelect()
    )

    mouse_x = models.TextField(
        blank=True
    )
    mouse_y = models.TextField(
        blank=True
    )
    percentage = models.FloatField(
        blank=True
    )
    mouse_option = models.IntegerField(
        choices=[[1, 'Reduce the difference in income'],
                 [2, 'Limit imports'],
                 [3, 'Send troops to fight ISIS'],
                 [4, 'Protect gays and lesbians against job discrimination'],
                 [5, 'The death penalty for murder'],
                 [6, 'Change access to citizenship for children of illegal immigrants'],
                 [7, 'Build a wall on the US-Mexico border'],
                 [8, 'Paid leave for parents of new children'],
                 [9, 'Increase number of black students at universities'],
                 [10, 'Pay women and men the same amount for the same work']],
        blank=True,
        widget=widgets.RadioSelect()
    )

    #被抽中的issue的号码
    issue_num = models.IntegerField()

    #自己的opinion
    self_opinion = models.CharField()





