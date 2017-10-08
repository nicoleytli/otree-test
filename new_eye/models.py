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

    # pics = models.CharField()
    # pics_loc = models.CharField()

    def creating_session(self):
        if self.round_number == 1:
            number_of_random = 30
            # a list of random answers' location
            random_loc = random.sample(list(range(36)), number_of_random)
            # a list of drawn random answers
            # 哪些位置上的图片会换
            pics_loc = random_loc
            # self.pics_loc = pics_loc

            # 换来的图片是来自哪里
            random_loc = random.sample(random_loc, len(random_loc))

            # for i in range(len(random_loc)):
            #     loc = list(range(36))
            #     loc.remove(i)
            #     answers_loc.append(random.choice(loc))

            final_list = list(range(36))

            for i, j in zip(range(len(random_loc)), pics_loc):
                final_list[j] = random_loc[i]

            self.session.vars['final_list'] = final_list

            if self.round_number == 1:
                self.session.vars['all_answers'] = Constants.all_answers

            # for p in self.get_players():
            #     answers_data = p.current_answers()
            #     p.correct_answer = answers_data['correction']

            # self.pics = random_loc

            for p in self.get_players():
                order_list = list(range(36))
                order_list = random.sample(order_list, len(order_list))

                pic_final_list = list(range(36))
                for i in range(len(pic_final_list)):
                    pic_final_list[i] = final_list[order_list[i]]

                p.participant.vars['order_list'] = order_list
                p.participant.vars['pic_final_list'] = pic_final_list



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_num = models.IntegerField()
    answer_num = models.IntegerField()
    answer = models.CharField(
        widget=widgets.RadioSelect()
    )
    q1 = models.CharField(
        choices=['Yes', 'No']
    )
    q2 = models.IntegerField(
        max=100, min=10
    )
    q3 = models.CharField(
        choices=['male', 'female', 'It\'s complicated']
    )
    q4 = models.CharField(
        choices=['Once a week or less', 'A few times a week', 'A couple of hours most days', 'Many hours on most days']
    )
    q5 = models.CharField(
        choices=['Mouse', 'Touchpad', 'Finger on a touch screen', 'Some other device']
    )
    q6 = models.CharField(
        choices=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua & Barbuda', 'Argentina',
                 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
                 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia & Herzegovina',
                 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Myanmar/Burma', 'Burundi',
                 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad',
                 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
                 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominican Republic', 'Dominica', 'Ecuador',
                 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France',
                 'French Guiana', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Great Britain', 'Greece',
                 'Grenada', 'Guadeloupe', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
                 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel and the Occupied Territories', 'Italy',
                 'Ivory Coast (Cote d\'Ivoire)', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait',
                 'Kyrgyz Republic (Kyrgyzstan)', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
                 'Lithuania', 'Luxembourg', 'Republic of Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
                 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova, Republic of',
                 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nepal',
                 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Korea, Democratic Republic of (North Korea)',
                 'Norway', 'Oman', 'Pacific Islands', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
                 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russian Federation', 'Rwanda',
                 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent\'s & Grenadines', 'Samoa', 'Sao Tome and Principe',
                 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore','Slovak Republic (Slovakia)',
                 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Korea, Republic of (South Korea)', 'South Sudan',
                 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan',
                 'Tanzania', 'Thailand', 'Timor Leste', 'Togo', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                 'Turks & Caicos Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United States of America (USA)',
                 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Virgin Islands (UK)', 'Virgin Islands (US)', 'Yemen',
                 'Zambia', 'Zimbabwe']
    )
    q7 = models.CharField(
        choices=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua & Barbuda', 'Argentina',
                 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
                 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia & Herzegovina',
                 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Myanmar/Burma', 'Burundi',
                 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad',
                 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
                 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominican Republic', 'Dominica', 'Ecuador',
                 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France',
                 'French Guiana', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Great Britain', 'Greece',
                 'Grenada', 'Guadeloupe', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
                 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel and the Occupied Territories', 'Italy',
                 'Ivory Coast (Cote d\'Ivoire)', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait',
                 'Kyrgyz Republic (Kyrgyzstan)', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
                 'Lithuania', 'Luxembourg', 'Republic of Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
                 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova, Republic of',
                 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nepal',
                 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Korea, Democratic Republic of (North Korea)',
                 'Norway', 'Oman', 'Pacific Islands', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
                 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russian Federation', 'Rwanda',
                 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent\'s & Grenadines', 'Samoa', 'Sao Tome and Principe',
                 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore','Slovak Republic (Slovakia)',
                 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Korea, Republic of (South Korea)', 'South Sudan',
                 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan',
                 'Tanzania', 'Thailand', 'Timor Leste', 'Togo', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                 'Turks & Caicos Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United States of America (USA)',
                 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Virgin Islands (UK)', 'Virgin Islands (US)', 'Yemen',
                 'Zambia', 'Zimbabwe']
    )
    q8 = models.CharField(
        choices=['I am a native speaker of English',
                 'I am not a native speaker, but I recognized all the words used to describe emotions in the study',
                 'I recognized almost all the words used to describe emotions in the study',
                 'I recognized only some of the words used to describe emotions in the study']
    )
    q9 = models.TextField(
        blank=True
    )
    # correct_answer = models.CharField()
    # score = models.IntegerField()

    def current_answers(self):
        num = self.participant.vars['order_list'][self.round_number - 1]
        self.answer_num = num + 1
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
