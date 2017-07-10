from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Introduction(Page):
    def vars_for_template(self):
        return {'link': 'https://www.browserling.com/tools/aes-encrypt'}


class Exp0(Page):
    form_model = models.Player
    form_fields = ['x_0']

    def vars_for_template(self):
        return {'link': 'https://www.browserling.com/tools/aes-decrypt'}

    def x_0_choices(self):
        messages = ['U2FsdGVkX18s+BqpZ/dBN3067AiYkJnfd5NeJLCjhnaRLNm/a4i581cbeXW9c6M8', 'U2FsdGVkX1/ifPvw3igI2+EHnNZOnExpj0tnBFKRWPV+3vWEupWUULslSxrA5gOo',
                    'U2FsdGVkX1/jV1fBxlBW4lhaOhcH7O4/sfZRkcxC3onbEeEZC4PVhhAkQ9itQ80h', 'U2FsdGVkX194iOHdJPb9fbJCs/B+QVbKz8b6HWnvY8Flp/8/Gk4744/dz3Jl7Ey0',
                    'U2FsdGVkX19YusyPtXZ1z6Pcdn1oPc9dghE0DE32DWM33bP7PwO5GIbFELiSYLL8', 'U2FsdGVkX1/2RWoCSmWhqYLfIIds/wZ+Up9bDFUgVbnaDJ5ZrKoFOQzp74xUvSlU',
                    'U2FsdGVkX1+q48npkC85b58c4lkH4qim6OZWGKRHZZLn6k4zWwpqkaSb3MBcirWc', 'U2FsdGVkX1+1eJqJH+neh5LFePLkHtTeli4u1jViGOD9XakqmhwasKiK/Lrtpbhk',
                    'U2FsdGVkX1/G3ZDK1ZvN7sJN/VH5C2mPaH5hcNrB2gaSVnTI706KbCxBj5OjXSJQ', 'U2FsdGVkX1846XuQxRFzypd61ShLLPx5bnQy9L+iTjNYVdQqjvDgnc3Wd3NHENN7',
                    'U2FsdGVkX1+7uixDo0aszwR2Tx4eHv0q64YcNbFmw9wIxvTS9eD4ISGwI8owWw+Z', 'U2FsdGVkX191bRYXUZvg6ddNbTUu2H1G5zFcgQAKCTJOTmQhpfE2ja1w2Zm3YcKU',
                    'U2FsdGVkX18SVum7pJsMTtPZD4MolAertmSExW7IRs+GX2iXHV3PdLqKMxCl7LXR', 'U2FsdGVkX1/l3p7MzkqegH3y3CXqX1V5M4M02/KzcYGGy+RIdLW4Wafe2lQ+gvb5',
                    'U2FsdGVkX18zrj0BLx/HLUgWumolB7u6svpMTGDEyA7Z0qz82POb4W56qRU8nuH7', 'U2FsdGVkX19JYC5N3m5bvsB083b7pgYaYi4+AvAUjerO9nn650YvVZ4XloZDnUWS',
                    'U2FsdGVkX1+A57qRRZGOPOOjdmYNwi71OVw2jnRStDBRbrs6GkMj/UfJsKnLeDUD', 'U2FsdGVkX1+IEXlFY6AOFkbwKh3IAu76byvEcBUUbKga8tBd1xFh0BVJgxERUy9S',
                    'U2FsdGVkX1/wx5U+9H+4+c5KfOOid2HbyhzkHw166iFv9c1HzzHHa5MfO0T4WCnv', 'U2FsdGVkX1/HTK7bHEXQB/wVxe8p4vHDOzJbrJzXexv7zVsMt2cUMPXNC4fbkMga',
                    'U2FsdGVkX19fdTyCrrUP1DMuybBcdQAHZlbJK4z21eH7y4Fs3xrfeuut8qlnnrP2']
        random.shuffle(messages)
        return messages


class Exp1(Page):
    form_model = models.Player
    form_fields = ['x_1', 'exp1_answer', 'exp1_choice']

    def vars_for_template(self):
        return {'link': 'https://www.browserling.com/tools/aes-decrypt'}

    def x_1_choices(self):
        messages = ['U2FsdGVkX1+xwJliNttDa3Vv6DZUnCmiCdXQ3zTz4u0=', 'U2FsdGVkX18ZbJBzRG1RO2EQhEu9musCKLYr89KFQfg=',
                    'U2FsdGVkX18ECE3+tKlB9DeV8w01+gnjxEOQZ9pe6P0=', 'U2FsdGVkX18VnJKa6kJBEbcdO0OjcJxhJ1Sb4OP1BvQ=',
                    'U2FsdGVkX18nc6ZjbX5MlCIJ2K7em2Q6eSyc6aBPO+8=', 'U2FsdGVkX1+8E5AvGy9bEiY4JyS3NIKsRJ0eX3Q1K4s=',
                    'U2FsdGVkX1/50iNaisZgUddyD8UeRaJzC2W7rFvsZm4=', 'U2FsdGVkX1+Im6guCEHVWsot4ISpydV2Lt/fiVMSy8k=',
                    'U2FsdGVkX18O5PBd7uSqxg35JoNANsU64u/s1qvU2AM=', 'U2FsdGVkX1+aBLiaWJ+7dsTQWhCd0qT83c6xtipwW1w=',
                    'U2FsdGVkX1/TOM4o7tF52K4iZkX4VF6sl/d0DcEElXc=', 'U2FsdGVkX1++OUbQa4VMtpMM8P9glhCkczKReX/r+rc=',
                    'U2FsdGVkX192XsBVPuyVkjDFMmyzjPwtXUjxa6U58/o=', 'U2FsdGVkX18ukBqFhTr4GfS/K1OUxLAL1Wj49Vy4XWg=',
                    'U2FsdGVkX190D7C1sPwCURzZvFl/eIlJm2DBtrS5I0s=', 'U2FsdGVkX1+596tdv12BL33Gkh/qRKmbkawcTu05odA=',
                    'U2FsdGVkX18uKONkVE29Xzot3oXMPPPZNRt5UyS7iwk=', 'U2FsdGVkX18vHTW3Bo+pjdZQ6mz4XimLhKuIzncvBOU=',
                    'U2FsdGVkX1/p8h5ges17VZ2MI4x//7V30+n3hxSqz9U=', 'U2FsdGVkX1+M+A60ZP7TqASYdffvGz/KEWq2eS+P0SM=',
                    'U2FsdGVkX18Gi83XtaixOqqggKx7KvVbZC7Bn8XB6AA=']
        random.shuffle(messages)
        return messages


class Exp2(Page):
    form_model = models.Player
    form_fields = ['x_2', 'exp2_answer']

    def vars_for_template(self):

        return {'link': 'https://www.browserling.com/tools/aes-decrypt'}

    def x_2_choices(self):
        messages = ['U2FsdGVkX1+BM69M26Mn618sc3Kp+foEnmwqK8i6eM8=', 'U2FsdGVkX1/ieVJYk8NQPeKshuOnXZUznVkoAJ1m4Cg=',
                    'U2FsdGVkX1/bxh/J9Jn00tU9T6szv/deMBbT1l6OEwY=', 'U2FsdGVkX1/YH9S7rlaOMgADhZJJ2y3Bh9Iuch1sPRs=',
                    'U2FsdGVkX1/LHkZMff0e/JQhOKogEmMqyJVZxcU5f/0=', 'U2FsdGVkX1/rl0MsQRjAwrVgSS58HaKBjiYTMJZ9VSU=',
                    'U2FsdGVkX19AS1L3jbK93lFq0GY63DUc5oF2AmzADuU=', 'U2FsdGVkX19GTRBHG26deWb3MViYxaRGd2Kn7QnGcKU=',
                    'U2FsdGVkX19niN9DPqDQNvuaOEvDOntSF3ieJ6d9rKc=', 'U2FsdGVkX19hpg4aEJCequXm/HyqPQzLwNZm9EUBp1A=',
                    'U2FsdGVkX1/X7lwmH+2JFtuXWEemDwsKgo6t91fJty8=', 'U2FsdGVkX1/PAV8MPoNO0Yf7cNiAXCQpZsUFgka0pJk=',
                    'U2FsdGVkX19NXGkXpQaep+7dNnrCG2pCVECl52JEz2w=', 'U2FsdGVkX19rRak6LmVoor7goaIuqiRSLMlEczdGYNQ=',
                    'U2FsdGVkX18n8gYiNq2Kina1Of5qIvsRkcp0PIdG37o=', 'U2FsdGVkX1/E32PydmSbgs3LzhRCjoM+e+09DrEiLaM=',
                    'U2FsdGVkX19rJW5v8xujBW6CoLp28jn8EvEzlITb+Fw=', 'U2FsdGVkX18bOknI2ef1EU0Knc9mLhjo6jKe0XWwXAs=',
                    'U2FsdGVkX18JWdgKpbenhMfzUX0QfGYzkbwRQjsUsYw=', 'U2FsdGVkX18xtpmOskZZEGzG+OQZgqPXkld85K4VXb4=',
                    'U2FsdGVkX18NTjZMudELP6Wbi4P/wlCh5JNanOgEz+Y=']
        random.shuffle(messages)
        return messages


class Exp3(Page):
    form_model = models.Player
    form_fields = ['x_3', 'dollar_0', 'dollar_1', 'dollar_2', 'dollar_3', 'dollar_4', 'dollar_5', 'dollar_6',
                   'dollar_7', 'dollar_8', 'dollar_9', 'dollar_10', 'dollar_11', 'dollar_12', 'dollar_13', 'dollar_14',
                   'dollar_15', 'dollar_16', 'dollar_17', 'dollar_18', 'dollar_19', 'dollar_20']

    def vars_for_template(self):
        values = [1, 2, 3]
        dollar = ['$0.00', '$0.10', '$0.20', '$0.30', '$0.40', '$0.50', '$0.60', '$0.70', '$0.80', '$0.90', '$1.00', '$1.10', '$1.20', '$1.30', '$1.40',
                  '$1.50', '$1.60', '$1.70', '$1.80', '$1.90', '$2.00']
        name = ['dollar_0', 'dollar_1', 'dollar_2', 'dollar_3', 'dollar_4', 'dollar_5', 'dollar_6', 'dollar_7', 'dollar_8',
                'dollar_9', 'dollar_10', 'dollar_11', 'dollar_12', 'dollar_13', 'dollar_14', 'dollar_15', 'dollar_16',
                'dollar_17', 'dollar_18', 'dollar_19', 'dollar_20']
        mylist = zip(dollar, name)

        return {'link': 'https://www.browserling.com/tools/aes-decrypt',
                'list': mylist,
                'values': values}

    def x_3_choices(self):
        messages = ['U2FsdGVkX1+lSdsw9mFWKOqy3pjhkpVojqI2amXsPq0=', 'U2FsdGVkX19IzQehaZQjvsQMB01ti5Ia3dmjyRQ1TLM=',
                    'U2FsdGVkX1+DdAsNqkEiXlYTHr/ripsNEatz7FORvbA=', 'U2FsdGVkX1+HBUnCxkTisQ7Q+Be/DLDuWpXFGdch5O8=',
                    'U2FsdGVkX18HxIbGUY8YjDDME0+uIuckLNsCXnZAfys=', 'U2FsdGVkX18Yi5vDpYrsgCRcQhcM/AiiLB2zxaVSuJI=',
                    'U2FsdGVkX18rK1y8Z7fhDwFXBjqsAtqJPZKH/EU2FbM=', 'U2FsdGVkX18DDpqBHZWa9ntsJP+mFyN4AtX8pbv3yRA=',
                    'U2FsdGVkX1+7crahYXtTvpWaGr+GDHOXIs3dzk1FKbY=', 'U2FsdGVkX1+uYJwjH+QUEc0BV2XHaE0TdfapuEVv53I=',
                    'U2FsdGVkX1/3cpvyWU83KDH/1x7JnTTEn+NUM9llL+o=', 'U2FsdGVkX18dstAgD8k8giVfXOad2Vt4nrscXvGg8hM=',
                    'U2FsdGVkX1/ikkGE2zC9v8Gu96AHpw+j5Xkj3aeX3og=', 'U2FsdGVkX19IgaNiNIXPwdhtgQiUGpLgy20M1OcDMxk=',
                    'U2FsdGVkX19GmR2nyn6piLZ/8k+t/RgWo4kiCn0jgto=', 'U2FsdGVkX1+shMxp7w8wW46UL6K9L6VpYoS8AqaZ/WE=',
                    'U2FsdGVkX1/EkgOEQYbV5dGh52bEtPNZcaBE6zzwOzg=', 'U2FsdGVkX1+MNsgj3s3Cdb4KtFmBLyQ4mq3bfR1en7I=',
                    'U2FsdGVkX19kPof/dhoJbJ07JMJovQ3L/hr+4lYXXV8=', 'U2FsdGVkX1+/9kDQDlQrSsJealnu1eM4HfA0WPKF9XE=',
                    'U2FsdGVkX199TpOuJJ71j1brfR6zHos/8rs38bzMdzQ=']

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


class Exp0_result(Page):
    form_model = models.Player
    form_fields = ['message0']

    def vars_for_template(self):
        return {'message': self.player.x_0,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class Exp1_result(Page):
    form_model = models.Player
    form_fields = ['message1']

    def vars_for_template(self):
        self.player.result_A = random.choice(['Red', 'Red', 'Red', 'Red', 'White', 'White', 'White', 'Black', 'Black', 'Black'])
        self.player.result_B = random.choice(['Red', 'Red', 'White', 'White', 'White', 'Black', 'Black', 'Black', 'Black', 'Black'])

        return {'result_A': self.player.result_A,
                'result_B': self.player.result_B,
                'message': self.player.x_1,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class Exp2_result(Page):
    form_model = models.Player
    form_fields = ['message2']

    def vars_for_template(self):
        self.player.result_exp2 = random.choice(['Black', 'White'])

        return {
                'result': self.player.result_exp2,
                'message': self.player.x_2,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class Exp3_result(Page):
    form_model = models.Player
    form_fields = ['message3']

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

        return {'black_ball': black_ball,
                'white_ball': white_ball,
                'result': self.player.result_exp3,
                'link': 'https://www.browserling.com/tools/aes-decrypt',
                'message': self.player.x_3}


class WaitExp0(Page):
    timeout_seconds = 5

    def before_next_page(self):
        messages = ['U2FsdGVkX18s+BqpZ/dBN3067AiYkJnfd5NeJLCjhnaRLNm/a4i581cbeXW9c6M8', 'U2FsdGVkX1/ifPvw3igI2+EHnNZOnExpj0tnBFKRWPV+3vWEupWUULslSxrA5gOo',
                    'U2FsdGVkX1/jV1fBxlBW4lhaOhcH7O4/sfZRkcxC3onbEeEZC4PVhhAkQ9itQ80h', 'U2FsdGVkX194iOHdJPb9fbJCs/B+QVbKz8b6HWnvY8Flp/8/Gk4744/dz3Jl7Ey0',
                    'U2FsdGVkX19YusyPtXZ1z6Pcdn1oPc9dghE0DE32DWM33bP7PwO5GIbFELiSYLL8', 'U2FsdGVkX1/2RWoCSmWhqYLfIIds/wZ+Up9bDFUgVbnaDJ5ZrKoFOQzp74xUvSlU',
                    'U2FsdGVkX1+q48npkC85b58c4lkH4qim6OZWGKRHZZLn6k4zWwpqkaSb3MBcirWc', 'U2FsdGVkX1+1eJqJH+neh5LFePLkHtTeli4u1jViGOD9XakqmhwasKiK/Lrtpbhk',
                    'U2FsdGVkX1/G3ZDK1ZvN7sJN/VH5C2mPaH5hcNrB2gaSVnTI706KbCxBj5OjXSJQ', 'U2FsdGVkX1846XuQxRFzypd61ShLLPx5bnQy9L+iTjNYVdQqjvDgnc3Wd3NHENN7',
                    'U2FsdGVkX1+7uixDo0aszwR2Tx4eHv0q64YcNbFmw9wIxvTS9eD4ISGwI8owWw+Z', 'U2FsdGVkX191bRYXUZvg6ddNbTUu2H1G5zFcgQAKCTJOTmQhpfE2ja1w2Zm3YcKU',
                    'U2FsdGVkX18SVum7pJsMTtPZD4MolAertmSExW7IRs+GX2iXHV3PdLqKMxCl7LXR', 'U2FsdGVkX1/l3p7MzkqegH3y3CXqX1V5M4M02/KzcYGGy+RIdLW4Wafe2lQ+gvb5',
                    'U2FsdGVkX18zrj0BLx/HLUgWumolB7u6svpMTGDEyA7Z0qz82POb4W56qRU8nuH7', 'U2FsdGVkX19JYC5N3m5bvsB083b7pgYaYi4+AvAUjerO9nn650YvVZ4XloZDnUWS',
                    'U2FsdGVkX1+A57qRRZGOPOOjdmYNwi71OVw2jnRStDBRbrs6GkMj/UfJsKnLeDUD', 'U2FsdGVkX1+IEXlFY6AOFkbwKh3IAu76byvEcBUUbKga8tBd1xFh0BVJgxERUy9S',
                    'U2FsdGVkX1/wx5U+9H+4+c5KfOOid2HbyhzkHw166iFv9c1HzzHHa5MfO0T4WCnv', 'U2FsdGVkX1/HTK7bHEXQB/wVxe8p4vHDOzJbrJzXexv7zVsMt2cUMPXNC4fbkMga',
                    'U2FsdGVkX19fdTyCrrUP1DMuybBcdQAHZlbJK4z21eH7y4Fs3xrfeuut8qlnnrP2']
        num = messages.index(self.player.x_0)
        text = ['Hello from Paris', 'Hello from London', 'Hello from Beijing', 'Hello from Berlin', 'Hello from New Heaven',
                'Hello from Tokyo', 'Hello from Seoul', 'Hello from Barcelona', 'Hello from Moscow', 'Hello from Shanghai',
                'Hello from Hong Kong', 'Hello from Boston', 'Hello from Los Angeles', 'Hello from Melbourne', 'Hello from Zurich',
                'Hello from Taipei', 'Hello from New York', 'Hello from Amsterdam',  'Hello from Toulouse', 'Hello from Toronto',
                'Hello from Philadelphia']
        real_text = text[num]
        a = real_text
        b = self.player.message0

        n, m = len(a), len(b)
        if n > m:
            # Make sure n <= m, to use O(min(n,m)) space
            a, b = b, a
            n, m = m, n

        current = range(n + 1)
        for i in range(1, m + 1):
            previous, current = current, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete = previous[j] + 1, current[j - 1] + 1
                change = previous[j - 1]
                if a[j - 1] != b[i - 1]:
                    change = change + 1
                current[j] = min(add, delete, change)

        distance = current[n]
        ok = distance <= 0

        if ok:
            self.player.check_0 = 1
        else:
            self.player.check_0 = 0

    def vars_for_template(self):
        return {'message': self.player.x_0,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class WaitExp1(Page):
    timeout_seconds = 5

    def vars_for_template(self):
        return {'message': self.player.x_1,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class WaitExp2(Page):
    timeout_seconds = 6

    def vars_for_template(self):
        return {'message': self.player.x_2,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class WaitExp3(Page):
    timeout_seconds = 5

    def vars_for_template(self):
        return {'message': self.player.x_3,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class ResultExp0(Page):
    form_model = models.Player
    form_fields = ['message0_other']

    def vars_for_template(self):
        return {'message': self.player.x_0,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class ResultExp1(Page):

    def vars_for_template(self):
        messages = ['U2FsdGVkX1+xwJliNttDa3Vv6DZUnCmiCdXQ3zTz4u0=', 'U2FsdGVkX18ZbJBzRG1RO2EQhEu9musCKLYr89KFQfg=',
                    'U2FsdGVkX18ECE3+tKlB9DeV8w01+gnjxEOQZ9pe6P0=', 'U2FsdGVkX18VnJKa6kJBEbcdO0OjcJxhJ1Sb4OP1BvQ=',
                    'U2FsdGVkX18nc6ZjbX5MlCIJ2K7em2Q6eSyc6aBPO+8=', 'U2FsdGVkX1+8E5AvGy9bEiY4JyS3NIKsRJ0eX3Q1K4s=',
                    'U2FsdGVkX1/50iNaisZgUddyD8UeRaJzC2W7rFvsZm4=', 'U2FsdGVkX1+Im6guCEHVWsot4ISpydV2Lt/fiVMSy8k=',
                    'U2FsdGVkX18O5PBd7uSqxg35JoNANsU64u/s1qvU2AM=', 'U2FsdGVkX1+aBLiaWJ+7dsTQWhCd0qT83c6xtipwW1w=',
                    'U2FsdGVkX1/TOM4o7tF52K4iZkX4VF6sl/d0DcEElXc=', 'U2FsdGVkX1++OUbQa4VMtpMM8P9glhCkczKReX/r+rc=',
                    'U2FsdGVkX192XsBVPuyVkjDFMmyzjPwtXUjxa6U58/o=', 'U2FsdGVkX18ukBqFhTr4GfS/K1OUxLAL1Wj49Vy4XWg=',
                    'U2FsdGVkX190D7C1sPwCURzZvFl/eIlJm2DBtrS5I0s=', 'U2FsdGVkX1+596tdv12BL33Gkh/qRKmbkawcTu05odA=',
                    'U2FsdGVkX18uKONkVE29Xzot3oXMPPPZNRt5UyS7iwk=', 'U2FsdGVkX18vHTW3Bo+pjdZQ6mz4XimLhKuIzncvBOU=',
                    'U2FsdGVkX1/p8h5ges17VZ2MI4x//7V30+n3hxSqz9U=', 'U2FsdGVkX1+M+A60ZP7TqASYdffvGz/KEWq2eS+P0SM=',
                    'U2FsdGVkX18Gi83XtaixOqqggKx7KvVbZC7Bn8XB6AA=']
        num = messages.index(self.player.x_1) / 10

        if self.player.exp1_answer > num:
            larger_smaller = 'smaller than'
            if self.player.exp1_choice == 'Option A':
                option = 'Option A'
                if self.player.result_A == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_A == 'White':
                    self.player.payoff_1 = 0.9
                else:
                    self.player.payoff_1 = 0.7
            else:
                option = 'Option B'
                if self.player.result_B == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_B == 'White':
                    self.player.payoff_1 = 0.9
                else:
                    self.player.payoff_1 = 0.7
        elif self.player.exp1_answer == num:
            larger_smaller = 'equal to'
            if self.player.exp1_choice == 'Option A':
                option = 'Option A'
                if self.player.result_A == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_A == 'White':
                    self.player.payoff_1 = 0.9
                else:
                    self.player.payoff_1 = 0.7
            else:
                option = 'Option B'
                if self.player.result_B == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_B == 'White':
                    self.player.payoff_1 = 0.9
                else:
                    self.player.payoff_1 = 0.7
        else:
            larger_smaller = 'larger than'
            if self.player.exp1_choice == 'Option B':
                option = 'Option A'
                if self.player.result_A == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_A == 'White':
                    self.player.payoff_1 = 0.9
                else:
                    self.player.payoff_1 = 0.7
            else:
                option = 'Option B'
                if self.player.result_B == 'Red':
                    self.player.payoff_1 = num
                elif self.player.result_B == 'White':
                    self.player.payoff_1 = 0.9
                else:
                    self.player.payoff_1 = 0.7

        if option == 'Option A':
            result = self.player.result_A
        else:
            result = self.player.result_B

        return {'option': option,
                'result': result,
                'payoff': self.player.payoff_1,
                'larger_smaller': larger_smaller,
                'threshold': self.player.exp1_answer}


class ResultExp2(Page):
    def vars_for_template(self):
        messages = ['U2FsdGVkX1+BM69M26Mn618sc3Kp+foEnmwqK8i6eM8=', 'U2FsdGVkX1/ieVJYk8NQPeKshuOnXZUznVkoAJ1m4Cg=',
                    'U2FsdGVkX1/bxh/J9Jn00tU9T6szv/deMBbT1l6OEwY=', 'U2FsdGVkX1/YH9S7rlaOMgADhZJJ2y3Bh9Iuch1sPRs=',
                    'U2FsdGVkX1/LHkZMff0e/JQhOKogEmMqyJVZxcU5f/0=', 'U2FsdGVkX1/rl0MsQRjAwrVgSS58HaKBjiYTMJZ9VSU=',
                    'U2FsdGVkX19AS1L3jbK93lFq0GY63DUc5oF2AmzADuU=', 'U2FsdGVkX19GTRBHG26deWb3MViYxaRGd2Kn7QnGcKU=',
                    'U2FsdGVkX19niN9DPqDQNvuaOEvDOntSF3ieJ6d9rKc=', 'U2FsdGVkX19hpg4aEJCequXm/HyqPQzLwNZm9EUBp1A=',
                    'U2FsdGVkX1/X7lwmH+2JFtuXWEemDwsKgo6t91fJty8=', 'U2FsdGVkX1/PAV8MPoNO0Yf7cNiAXCQpZsUFgka0pJk=',
                    'U2FsdGVkX19NXGkXpQaep+7dNnrCG2pCVECl52JEz2w=', 'U2FsdGVkX19rRak6LmVoor7goaIuqiRSLMlEczdGYNQ=',
                    'U2FsdGVkX18n8gYiNq2Kina1Of5qIvsRkcp0PIdG37o=', 'U2FsdGVkX1/E32PydmSbgs3LzhRCjoM+e+09DrEiLaM=',
                    'U2FsdGVkX19rJW5v8xujBW6CoLp28jn8EvEzlITb+Fw=', 'U2FsdGVkX18bOknI2ef1EU0Knc9mLhjo6jKe0XWwXAs=',
                    'U2FsdGVkX18JWdgKpbenhMfzUX0QfGYzkbwRQjsUsYw=', 'U2FsdGVkX18xtpmOskZZEGzG+OQZgqPXkld85K4VXb4=',
                    'U2FsdGVkX18NTjZMudELP6Wbi4P/wlCh5JNanOgEz+Y=']
        num = messages.index(self.player.x_2) / 10

        if self.player.exp2_answer > num:
            option = 'Option A'
            larger_smaller = 'smaller than'
            if self.player.result_exp2 == 'Black':
                self.player.payoff_2 = 2
            else:
                self.player.payoff_2 = 0
        elif self.player.exp2_answer == num:
            option = 'Option A'
            larger_smaller = 'equal to'
            if self.player.result_exp2 == 'Black':
                self.player.payoff_2 = 2
            else:
                self.player.payoff_2 = 0
        else:
            option = 'Option B'
            larger_smaller = 'larger than'
            self.player.payoff_2 = num

        result = self.player.result_exp2

        return {'option': option,
                'result': result,
                'larger_smaller': larger_smaller,
                'payoff': self.player.payoff_2,
                'threshold': self.player.exp2_answer}


class ResultExp3(Page):
    def vars_for_template(self):
        messages = ['U2FsdGVkX1+lSdsw9mFWKOqy3pjhkpVojqI2amXsPq0=', 'U2FsdGVkX19IzQehaZQjvsQMB01ti5Ia3dmjyRQ1TLM=',
                    'U2FsdGVkX1+DdAsNqkEiXlYTHr/ripsNEatz7FORvbA=', 'U2FsdGVkX1+HBUnCxkTisQ7Q+Be/DLDuWpXFGdch5O8=',
                    'U2FsdGVkX18HxIbGUY8YjDDME0+uIuckLNsCXnZAfys=', 'U2FsdGVkX18Yi5vDpYrsgCRcQhcM/AiiLB2zxaVSuJI=',
                    'U2FsdGVkX18rK1y8Z7fhDwFXBjqsAtqJPZKH/EU2FbM=', 'U2FsdGVkX18DDpqBHZWa9ntsJP+mFyN4AtX8pbv3yRA=',
                    'U2FsdGVkX1+7crahYXtTvpWaGr+GDHOXIs3dzk1FKbY=', 'U2FsdGVkX1+uYJwjH+QUEc0BV2XHaE0TdfapuEVv53I=',
                    'U2FsdGVkX1/3cpvyWU83KDH/1x7JnTTEn+NUM9llL+o=', 'U2FsdGVkX18dstAgD8k8giVfXOad2Vt4nrscXvGg8hM=',
                    'U2FsdGVkX1/ikkGE2zC9v8Gu96AHpw+j5Xkj3aeX3og=', 'U2FsdGVkX19IgaNiNIXPwdhtgQiUGpLgy20M1OcDMxk=',
                    'U2FsdGVkX19GmR2nyn6piLZ/8k+t/RgWo4kiCn0jgto=', 'U2FsdGVkX1+shMxp7w8wW46UL6K9L6VpYoS8AqaZ/WE=',
                    'U2FsdGVkX1/EkgOEQYbV5dGh52bEtPNZcaBE6zzwOzg=', 'U2FsdGVkX1+MNsgj3s3Cdb4KtFmBLyQ4mq3bfR1en7I=',
                    'U2FsdGVkX19kPof/dhoJbJ07JMJovQ3L/hr+4lYXXV8=', 'U2FsdGVkX1+/9kDQDlQrSsJealnu1eM4HfA0WPKF9XE=',
                    'U2FsdGVkX199TpOuJJ71j1brfR6zHos/8rs38bzMdzQ=']
        num = messages.index(self.player.x_3) / 10
        num2 = messages.index(self.player.x_3)

        option_num = self.participant.vars['dollar_%s' % num2]

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
                self.player.payoff_3 = 2
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
                self.player.payoff_3 = 2

        result = self.player.result_exp3

        return {'option': option,
                'result': result,
                'payoff': self.player.payoff_3}


class Page1(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3']

    def vars_for_template(self):
        order = random.randint(1, 6)
        return {'order': order}


class Page2(Page):
    form_model = models.Player
    form_fields = ['q4', 'q5']

    def vars_for_template(self):
        order = random.randint(0, 1)
        return {'order': order}


class Page3(Page):
    form_model = models.Player
    form_fields = ['citizenship', 'language', 'age', 'gender', 'educ', 'religion', 'income', 'time', 'exp1',
                   'other1', 'exp2', 'other2', 'exp3', 'other3', 'envelope', 'other4']


class Result(Page):
    def vars_for_template(self):
        total = self.player.payoff_1 + self.player.payoff_2 + self.player.payoff_3
        self.player.payoff = total
        return {'total': total}


class Before_exp(Page):
    pass

page_sequence = [
    Introduction,
    Exp0,
    Exp0_result,
    WaitExp0,
    ResultExp0,
    Before_exp,
    Exp1,
    Exp1_result,
    WaitExp1,
    ResultExp1,
    Exp2,
    Exp2_result,
    WaitExp2,
    ResultExp2,
    Exp3,
    Exp3_result,
    WaitExp3,
    ResultExp3,
    Page2,
    Page1,
    Page3,
    Result
]
