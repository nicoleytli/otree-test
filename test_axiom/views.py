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
        messages = ['U2FsdGVkX1/j4mb7KhgfqvDQJio/Nxo1y6XlOyGOtN3x6WWj3uOZdO+hmuOvLzF0', 'U2FsdGVkX1+3u/nF6C6K8zaIzDGVs82ZpDEk8cX9V0//6VSHXHB4mN4tUnYL/j3X',
                    'U2FsdGVkX19Ry7iN9ssjgPSz3QuofSPCmCN/kas9+dcbbLR9H8NDpjIeODu1A7r/', 'U2FsdGVkX1+5l6Za3/57g3ZUspz3eC2VyyIcPzpnttgYZlswQSfr4lst7IDYPDaL',
                    'U2FsdGVkX1+4Tr0pXNqpVnVhbMi6a8sX1JYbqQ2KiSa/eqUx1jsIGu0nkAR8Kl1X', 'U2FsdGVkX1/iEyJPqSp4z9gqZWLS6d7mglVGoYZEcGqcWTjtP50tFmJo9Gscyax2',
                    'U2FsdGVkX19H2KiGPASXYAHanyO7WGpIvnxniL5jPBX7AVInMULS8uAWYOvZNlz0', 'U2FsdGVkX184QtReEcFaoEM40EpRGov/ix+KHyvfT9OjOoTlZhg+U9iUoxuEahuY',
                    'U2FsdGVkX19ahhUWXsJ2NlU7q8B34X5mjcXj40GN3tmb95pYovaLFtgftKcKa8sY', 'U2FsdGVkX1/buqZe39rR55kfHqq+7aca5ZHJvKh413IqrHFk6PlnYJ5tMETYMWSI',
                    'U2FsdGVkX1936my7mOI7VV+1ss2zG310eaT5+w+PEYiSLh7VXFQ7mxMRH1qT72+S', 'U2FsdGVkX1+IATNNLHxPXnDG1qSsO/7FeJR/O4cHqq2uMePPVw91CVSQk8NjZ3On',
                    'U2FsdGVkX18Ii2GMgx1KqWvFiek7T0Ubdo1lBWF0JkNJkdMrNTGn3DU6UStsNPDJ', 'U2FsdGVkX1+LXJt1Wb9BCJXFIrvgjIm0S1qW6/FiBhIhlslCRwvKkAwVh1Jq54y7',
                    'U2FsdGVkX18uL8/JtUcbOytTnfA3LtqOqX4UtpeLNGOEXICA5ix6r1tqzhGq7q2D', 'U2FsdGVkX18uuLeFlI1+Ljqbrg6WpQWTlBifv4jXM94f2jgY97a1YOMcYWNY/W4e',
                    'U2FsdGVkX1+8YOpsdhbNXcJXa3XI846w7r9WVkVPgYRsTqE78xL/jQZzkLKFuyAE', 'U2FsdGVkX1+I6C17jJaVoSg2dxZrP6oNIS2V5G/qJj+NoQ/azIxNsOhfswqcRdmG',
                    'U2FsdGVkX1/WHR8hjA8HBCKkun0HE3FyB5L6RQmlx1vdtZsNBpFdsC7ndHRjhThC', 'U2FsdGVkX18tq47VX8RmoIrbiClOnkKf5yfLkUbSIrnPL9I9naCh+oWkxwBpkn/T',
                    'U2FsdGVkX18bGdo/Q9RkrSjdf+XbVUBjZDHQdH0RulfvySznhL/Ic2wt5SWuDgUE']
        random.shuffle(messages)
        return messages


class Exp1(Page):
    form_model = models.Player
    form_fields = ['x_1', 'exp1_answer', 'exp1_choice']

    def vars_for_template(self):
        return {'link': 'https://www.browserling.com/tools/aes-decrypt'}

    def x_1_choices(self):
        messages = ['U2FsdGVkX1+xwJliNttDa3Vv6DZUnCmiCdXQ3zTz4u0=', 'U2FsdGVkX18ZjiCQSG9SNsmI1vHg07fs6FQqiLqJoU8=',
                    'U2FsdGVkX19XyXRUNYHe/UMkcJv1HNDbS9ggAQ4F+qo=', 'U2FsdGVkX18mlYyk6jy+bACxGS8Ic9zhjHVb6fisQWk=',
                    'U2FsdGVkX1/X1eEF7lNheDklf59i1JxJglXCBFbMPew=', 'U2FsdGVkX1+A6e5VHmbGn0H1ZaxYS2pjlBLmROBYb5k=',
                    'U2FsdGVkX18VZ4cnz18H6I7rH/22GhKRO/S3lfZ9sHE=', 'U2FsdGVkX18FFzCQM7SOHYjLwX1D9hE4DdQ5qvCaS+A=',
                    'U2FsdGVkX18yS4/B/XI1U7FAV2DbzGB0EtJT1RfKpFA=', 'U2FsdGVkX18qDcqtk3ZDh5XPHo4bs+voVwb1FaDodcg=',
                    'U2FsdGVkX18ZbJBzRG1RO2EQhEu9musCKLYr89KFQfg=', 'U2FsdGVkX19AODAmy/pFnKMRKzR93kr+7sRjRwNzaqY=',
                    'U2FsdGVkX18FXz2CIpRpjYTKSU3Jt06r/9lsSPEF9Bc=', 'U2FsdGVkX19Us2QWxq6ZgftbIUwkCnJ1je018Jql4ns=',
                    'U2FsdGVkX1+DaxnXmyk4JqlszhFLcyzD6cZfaFmzIOQ=', 'U2FsdGVkX1+I7WIqKLFl66ej4ndspK+797O9oOMQmss=',
                    'U2FsdGVkX18YMi48W+JLyE6x1+EfW+ygW6cD6rbPF3M=', 'U2FsdGVkX19Rvd+pY4/2LNHs/VsTFBCSrpqpc1dzWFw=',
                    'U2FsdGVkX1/o81rolhFWm4/SboLsoVq+L1zX0hV70Ho=', 'U2FsdGVkX185OijSu07iZfBT1kn0+MQygb52sN7CdHE=',
                    'U2FsdGVkX18ECE3+tKlB9DeV8w01+gnjxEOQZ9pe6P0=']
        random.shuffle(messages)
        return messages


class Exp2(Page):
    form_model = models.Player
    form_fields = ['x_2', 'exp2_answer']

    def vars_for_template(self):

        return {'link': 'https://www.browserling.com/tools/aes-decrypt'}

    def x_2_choices(self):
        messages = ['U2FsdGVkX1+BM69M26Mn618sc3Kp+foEnmwqK8i6eM8=', 'U2FsdGVkX1+Vg3+vnOh8DUimjQgGMVhsa2nzoiY48oM=',
                    'U2FsdGVkX19rSflcGYeO6JmX2Gzwxe9HxTXmX1EEaOQ=', 'U2FsdGVkX1/er2SEOArwGn5IEth1vqnDU8hLM4HA2z4=',
                    'U2FsdGVkX185zFQPBMT5HBlOo+OL72fAy3DFrg1bEZo=', 'U2FsdGVkX19DF/JfoEHksGWVW49AdSvOjVuiyhGuaeo=',
                    'U2FsdGVkX1+M6knvcoN+ggc2NGWtLPdVHDryZEK1/Mg=', 'U2FsdGVkX1+L79zcly4M1CuRjXKPEL1Vj4FUCL9quL4=',
                    'U2FsdGVkX193rJ07imlaInqe9CDX3WLjfQIrHgoRScw=', 'U2FsdGVkX18MI8K8Sbtgu5pR/C6yNMD8vkr0LkL3/3M=',
                    'U2FsdGVkX1/ieVJYk8NQPeKshuOnXZUznVkoAJ1m4Cg=', 'U2FsdGVkX1+drW5Ynipd2zPUf4spULJPmWnL3wul/9w=',
                    'U2FsdGVkX1/dfHoCHi49ciLDYnxsFO4788CyxMl360Y=', 'U2FsdGVkX19rMbbUU6Ksw5Ar5WDnAL0xDSs1krR1SvM=',
                    'U2FsdGVkX19jVyRM4J7DDspK6MgXEfWojB2Xbwyjof4=', 'U2FsdGVkX19csUhGtsoANyHtq2Z6jGtPB0teZJzqGu0=',
                    'U2FsdGVkX1+/BhnEIiaW044necZH5JSu/+bI0MzJ1bA=', 'U2FsdGVkX182EfT9tLh68rhg41wZ+XLofv97eNZFk30=',
                    'U2FsdGVkX18VUKEqULydCRZprfOUyeByB2coDm+JaPw=', 'U2FsdGVkX19JVFCsrrpnmqMcNIwqc5rQ5PO+riuf7L4=',
                    'U2FsdGVkX1/bxh/J9Jn00tU9T6szv/deMBbT1l6OEwY=']
        random.shuffle(messages)
        return messages


class Exp3(Page):
    form_model = models.Player
    form_fields = ['x_3', 'dollar_0', 'dollar_1', 'dollar_2', 'dollar_3', 'dollar_4', 'dollar_5', 'dollar_6',
                   'dollar_7', 'dollar_8', 'dollar_9', 'dollar_10', 'dollar_11', 'dollar_12', 'dollar_13', 'dollar_14',
                   'dollar_15', 'dollar_16', 'dollar_17', 'dollar_18', 'dollar_19', 'dollar_20']

    def vars_for_template(self):
        values = [1, 2, 3]
        dollar = ['$0.00', '$0.01', '$0.02', '$0.03', '$0.04', '$0.05', '$0.06', '$0.07', '$0.08', '$0.09', '$0.10', '$0.11', '$0.12', '$0.13', '$0.14',
                  '$0.15', '$0.16', '$0.17', '$0.18', '$0.19', '$0.20']
        name = ['dollar_0', 'dollar_1', 'dollar_2', 'dollar_3', 'dollar_4', 'dollar_5', 'dollar_6', 'dollar_7', 'dollar_8',
                'dollar_9', 'dollar_10', 'dollar_11', 'dollar_12', 'dollar_13', 'dollar_14', 'dollar_15', 'dollar_16',
                'dollar_17', 'dollar_18', 'dollar_19', 'dollar_20']
        mylist = zip(dollar, name)

        return {'link': 'https://www.browserling.com/tools/aes-decrypt',
                'list': mylist,
                'values': values}

    def x_3_choices(self):
        messages = ['U2FsdGVkX1+lSdsw9mFWKOqy3pjhkpVojqI2amXsPq0=', 'U2FsdGVkX19UO4o/V+PM/gEh52Aghrl5WS9wvgZQaso=',
                    'U2FsdGVkX1+DpQa4/Ms3HvesJ8oQgge21szNboP/BCM=', 'U2FsdGVkX1+4p4WCZ9mjhTGyG7XeEMDNyLvUhv8TnOQ=',
                    'U2FsdGVkX1/QfPc1GWcXv2DdlHHhGsGs5e2BsKPeQGk=', 'U2FsdGVkX192QrisoIPmGB7dtrUiSkOI+llJ1KkbsAs=',
                    'U2FsdGVkX1++r5injNGxq7V3BeUKpkOe3rmvXQBrYoo=', 'U2FsdGVkX1850jABUaGuTfXl0YKxJb7+Ir5flVh1egc=',
                    'U2FsdGVkX18hZVCa9tHc0Be89FY7W9O3+W5PT6dNA/8=', 'U2FsdGVkX1/jmqPv4njnqQiqwY7JI4vQ4jJo6d/1wQI=',
                    'U2FsdGVkX19IzQehaZQjvsQMB01ti5Ia3dmjyRQ1TLM=', 'U2FsdGVkX1+oUG4rK5uH+IOkLGZ9/TZbaGpNC70F+40=',
                    'U2FsdGVkX1+X+fhPM9Wf1BnHLUTAp5xagkQNNKCE9pY=', 'U2FsdGVkX1/arDROSwqrO/SfUzoNNCeaTUv/AMm+gto=',
                    'U2FsdGVkX19uBdSP0+STB8Dg92D/p0/X2tH7zqtOqtk=', 'U2FsdGVkX19g9V7lhgg9ZfsMiC7ei+3xM5x8mTFeEuA=',
                    'U2FsdGVkX1+amFbu/gC7SH/y9jU4oZeu3OUyEBKOeLo=', 'U2FsdGVkX1+EeZuGqy1YtvO3XoWLKPfTVu884Dlbw4g=',
                    'U2FsdGVkX1/iKrpTELmuwcNPBWBe+9DJxpbmOMvzVj0=', 'U2FsdGVkX18pCbBQKEkw9lmcepBIoy+g4ZZvCjKovrs=',
                    'U2FsdGVkX1+DdAsNqkEiXlYTHr/ripsNEatz7FORvbA=']

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
    def vars_for_template(self):
        self.player.result_A = random.choice(['Red', 'Red', 'Red', 'Red', 'White', 'White', 'White', 'Black', 'Black', 'Black'])
        self.player.result_B = random.choice(['Red', 'Red', 'White', 'White', 'White', 'Black', 'Black', 'Black', 'Black', 'Black'])

        return {'result_A': self.player.result_A,
                'result_B': self.player.result_B,
                'message': self.player.x_1,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class Exp2_result(Page):
    def vars_for_template(self):
        self.player.result_exp2 = random.choice(['Black', 'White'])

        return {
                'result': self.player.result_exp2,
                'message': self.player.x_2,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


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

        return {'black_ball': black_ball,
                'white_ball': white_ball,
                'result': self.player.result_exp3,
                'link': 'https://www.browserling.com/tools/aes-decrypt',
                'message': self.player.x_3}


class FakeWaitExp0(Page):
    timeout_seconds = 10

    def before_next_page(self):
        messages = ['U2FsdGVkX1/j4mb7KhgfqvDQJio/Nxo1y6XlOyGOtN3x6WWj3uOZdO+hmuOvLzF0', 'U2FsdGVkX1+3u/nF6C6K8zaIzDGVs82ZpDEk8cX9V0//6VSHXHB4mN4tUnYL/j3X',
                    'U2FsdGVkX19Ry7iN9ssjgPSz3QuofSPCmCN/kas9+dcbbLR9H8NDpjIeODu1A7r/', 'U2FsdGVkX1+5l6Za3/57g3ZUspz3eC2VyyIcPzpnttgYZlswQSfr4lst7IDYPDaL',
                    'U2FsdGVkX1+4Tr0pXNqpVnVhbMi6a8sX1JYbqQ2KiSa/eqUx1jsIGu0nkAR8Kl1X', 'U2FsdGVkX1/iEyJPqSp4z9gqZWLS6d7mglVGoYZEcGqcWTjtP50tFmJo9Gscyax2',
                    'U2FsdGVkX19H2KiGPASXYAHanyO7WGpIvnxniL5jPBX7AVInMULS8uAWYOvZNlz0', 'U2FsdGVkX184QtReEcFaoEM40EpRGov/ix+KHyvfT9OjOoTlZhg+U9iUoxuEahuY',
                    'U2FsdGVkX19ahhUWXsJ2NlU7q8B34X5mjcXj40GN3tmb95pYovaLFtgftKcKa8sY', 'U2FsdGVkX1/buqZe39rR55kfHqq+7aca5ZHJvKh413IqrHFk6PlnYJ5tMETYMWSI',
                    'U2FsdGVkX1936my7mOI7VV+1ss2zG310eaT5+w+PEYiSLh7VXFQ7mxMRH1qT72+S', 'U2FsdGVkX1+IATNNLHxPXnDG1qSsO/7FeJR/O4cHqq2uMePPVw91CVSQk8NjZ3On',
                    'U2FsdGVkX18Ii2GMgx1KqWvFiek7T0Ubdo1lBWF0JkNJkdMrNTGn3DU6UStsNPDJ', 'U2FsdGVkX1+LXJt1Wb9BCJXFIrvgjIm0S1qW6/FiBhIhlslCRwvKkAwVh1Jq54y7',
                    'U2FsdGVkX18uL8/JtUcbOytTnfA3LtqOqX4UtpeLNGOEXICA5ix6r1tqzhGq7q2D', 'U2FsdGVkX18uuLeFlI1+Ljqbrg6WpQWTlBifv4jXM94f2jgY97a1YOMcYWNY/W4e',
                    'U2FsdGVkX1+8YOpsdhbNXcJXa3XI846w7r9WVkVPgYRsTqE78xL/jQZzkLKFuyAE', 'U2FsdGVkX1+I6C17jJaVoSg2dxZrP6oNIS2V5G/qJj+NoQ/azIxNsOhfswqcRdmG',
                    'U2FsdGVkX1/WHR8hjA8HBCKkun0HE3FyB5L6RQmlx1vdtZsNBpFdsC7ndHRjhThC', 'U2FsdGVkX18tq47VX8RmoIrbiClOnkKf5yfLkUbSIrnPL9I9naCh+oWkxwBpkn/T',
                    'U2FsdGVkX18bGdo/Q9RkrSjdf+XbVUBjZDHQdH0RulfvySznhL/Ic2wt5SWuDgUE']
        num = messages.index(self.player.x_0)
        text = ['Hello from Paris', 'Hello from London', 'Hello from Beijing', 'Hello from Berlin', 'Hello from New Heaven',
                'Hello from Tokyo', 'Hello from Seoul', 'Hello from Barcelona', 'Hello from Moscow', 'Hello from Shanghai',
                'Hello from Hong Kong', 'Hello from Boston', 'Hello from Los Angeles', 'Hello from Melbourne', 'Hello from Zurich',
                'Hello from Taipei', 'Hello from New York', 'Hello from Singapore', 'Hello from Toulouse', 'Hello from Toronto',
                'Hello from Amsterdam']
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
            self.player.check = 1
        else:
            self.player.check = 0

    def vars_for_template(self):
        return {'message': self.player.x_0,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class FakeWaitExp1(Page):
    timeout_seconds = 15

    def vars_for_template(self):
        return {'message': self.player.x_1,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class FakeWaitExp2(Page):
    timeout_seconds = 9

    def vars_for_template(self):
        return {'message': self.player.x_2,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class FakeWaitExp3(Page):
    timeout_seconds = 17

    def vars_for_template(self):
        return {'message': self.player.x_3,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class FakeResultExp0(Page):
    form_model = models.Player
    form_fields = ['message0_other']

    def vars_for_template(self):
        return {'message': self.player.x_0,
                'link': 'https://www.browserling.com/tools/aes-decrypt'}


class FakeResultExp1(Page):

    def vars_for_template(self):
        messages = ['U2FsdGVkX1+xwJliNttDa3Vv6DZUnCmiCdXQ3zTz4u0=', 'U2FsdGVkX18ZjiCQSG9SNsmI1vHg07fs6FQqiLqJoU8=',
                    'U2FsdGVkX19XyXRUNYHe/UMkcJv1HNDbS9ggAQ4F+qo=', 'U2FsdGVkX18mlYyk6jy+bACxGS8Ic9zhjHVb6fisQWk=',
                    'U2FsdGVkX1/X1eEF7lNheDklf59i1JxJglXCBFbMPew=', 'U2FsdGVkX1+A6e5VHmbGn0H1ZaxYS2pjlBLmROBYb5k=',
                    'U2FsdGVkX18VZ4cnz18H6I7rH/22GhKRO/S3lfZ9sHE=', 'U2FsdGVkX18FFzCQM7SOHYjLwX1D9hE4DdQ5qvCaS+A=',
                    'U2FsdGVkX18yS4/B/XI1U7FAV2DbzGB0EtJT1RfKpFA=', 'U2FsdGVkX18qDcqtk3ZDh5XPHo4bs+voVwb1FaDodcg=',
                    'U2FsdGVkX18ZbJBzRG1RO2EQhEu9musCKLYr89KFQfg=', 'U2FsdGVkX19AODAmy/pFnKMRKzR93kr+7sRjRwNzaqY=',
                    'U2FsdGVkX18FXz2CIpRpjYTKSU3Jt06r/9lsSPEF9Bc=', 'U2FsdGVkX19Us2QWxq6ZgftbIUwkCnJ1je018Jql4ns=',
                    'U2FsdGVkX1+DaxnXmyk4JqlszhFLcyzD6cZfaFmzIOQ=', 'U2FsdGVkX1+I7WIqKLFl66ej4ndspK+797O9oOMQmss=',
                    'U2FsdGVkX18YMi48W+JLyE6x1+EfW+ygW6cD6rbPF3M=', 'U2FsdGVkX19Rvd+pY4/2LNHs/VsTFBCSrpqpc1dzWFw=',
                    'U2FsdGVkX1/o81rolhFWm4/SboLsoVq+L1zX0hV70Ho=', 'U2FsdGVkX185OijSu07iZfBT1kn0+MQygb52sN7CdHE=',
                    'U2FsdGVkX18ECE3+tKlB9DeV8w01+gnjxEOQZ9pe6P0=']
        num = messages.index(self.player.x_1)

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


class FakeResultExp2(Page):
    def vars_for_template(self):
        messages = ['U2FsdGVkX1+BM69M26Mn618sc3Kp+foEnmwqK8i6eM8=', 'U2FsdGVkX1+Vg3+vnOh8DUimjQgGMVhsa2nzoiY48oM=',
                    'U2FsdGVkX19rSflcGYeO6JmX2Gzwxe9HxTXmX1EEaOQ=', 'U2FsdGVkX1/er2SEOArwGn5IEth1vqnDU8hLM4HA2z4=',
                    'U2FsdGVkX185zFQPBMT5HBlOo+OL72fAy3DFrg1bEZo=', 'U2FsdGVkX19DF/JfoEHksGWVW49AdSvOjVuiyhGuaeo=',
                    'U2FsdGVkX1+M6knvcoN+ggc2NGWtLPdVHDryZEK1/Mg=', 'U2FsdGVkX1+L79zcly4M1CuRjXKPEL1Vj4FUCL9quL4=',
                    'U2FsdGVkX193rJ07imlaInqe9CDX3WLjfQIrHgoRScw=', 'U2FsdGVkX18MI8K8Sbtgu5pR/C6yNMD8vkr0LkL3/3M=',
                    'U2FsdGVkX1/ieVJYk8NQPeKshuOnXZUznVkoAJ1m4Cg=', 'U2FsdGVkX1+drW5Ynipd2zPUf4spULJPmWnL3wul/9w=',
                    'U2FsdGVkX1/dfHoCHi49ciLDYnxsFO4788CyxMl360Y=', 'U2FsdGVkX19rMbbUU6Ksw5Ar5WDnAL0xDSs1krR1SvM=',
                    'U2FsdGVkX19jVyRM4J7DDspK6MgXEfWojB2Xbwyjof4=', 'U2FsdGVkX19csUhGtsoANyHtq2Z6jGtPB0teZJzqGu0=',
                    'U2FsdGVkX1+/BhnEIiaW044necZH5JSu/+bI0MzJ1bA=', 'U2FsdGVkX182EfT9tLh68rhg41wZ+XLofv97eNZFk30=',
                    'U2FsdGVkX18VUKEqULydCRZprfOUyeByB2coDm+JaPw=', 'U2FsdGVkX19JVFCsrrpnmqMcNIwqc5rQ5PO+riuf7L4=',
                    'U2FsdGVkX1/bxh/J9Jn00tU9T6szv/deMBbT1l6OEwY=']
        num = messages.index(self.player.x_2)

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


class FakeResultExp3(Page):
    def vars_for_template(self):
        messages = ['U2FsdGVkX1+lSdsw9mFWKOqy3pjhkpVojqI2amXsPq0=', 'U2FsdGVkX19UO4o/V+PM/gEh52Aghrl5WS9wvgZQaso=',
                    'U2FsdGVkX1+DpQa4/Ms3HvesJ8oQgge21szNboP/BCM=', 'U2FsdGVkX1+4p4WCZ9mjhTGyG7XeEMDNyLvUhv8TnOQ=',
                    'U2FsdGVkX1/QfPc1GWcXv2DdlHHhGsGs5e2BsKPeQGk=', 'U2FsdGVkX192QrisoIPmGB7dtrUiSkOI+llJ1KkbsAs=',
                    'U2FsdGVkX1++r5injNGxq7V3BeUKpkOe3rmvXQBrYoo=', 'U2FsdGVkX1850jABUaGuTfXl0YKxJb7+Ir5flVh1egc=',
                    'U2FsdGVkX18hZVCa9tHc0Be89FY7W9O3+W5PT6dNA/8=', 'U2FsdGVkX1/jmqPv4njnqQiqwY7JI4vQ4jJo6d/1wQI=',
                    'U2FsdGVkX19IzQehaZQjvsQMB01ti5Ia3dmjyRQ1TLM=', 'U2FsdGVkX1+oUG4rK5uH+IOkLGZ9/TZbaGpNC70F+40=',
                    'U2FsdGVkX1+X+fhPM9Wf1BnHLUTAp5xagkQNNKCE9pY=', 'U2FsdGVkX1/arDROSwqrO/SfUzoNNCeaTUv/AMm+gto=',
                    'U2FsdGVkX19uBdSP0+STB8Dg92D/p0/X2tH7zqtOqtk=', 'U2FsdGVkX19g9V7lhgg9ZfsMiC7ei+3xM5x8mTFeEuA=',
                    'U2FsdGVkX1+amFbu/gC7SH/y9jU4oZeu3OUyEBKOeLo=', 'U2FsdGVkX1+EeZuGqy1YtvO3XoWLKPfTVu884Dlbw4g=',
                    'U2FsdGVkX1/iKrpTELmuwcNPBWBe+9DJxpbmOMvzVj0=', 'U2FsdGVkX18pCbBQKEkw9lmcepBIoy+g4ZZvCjKovrs=',
                    'U2FsdGVkX1+DdAsNqkEiXlYTHr/ripsNEatz7FORvbA=']
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


class Page2(Page):
    form_model = models.Player
    form_fields = ['q4', 'q5']


class Page3(Page):
    form_model = models.Player
    form_fields = ['citizenship', 'language', 'age', 'gender', 'educ', 'religion', 'income', 'time', 'exp1',
                   'other1', 'exp2', 'other2', 'exp3', 'other3', 'envelope', 'other4']


class Result(Page):
    def vars_for_template(self):
        total = self.player.payoff_1 + self.player.payoff_2 + self.player.payoff_3
        return {'total': total}

page_sequence = [
    Introduction,
    Exp0,
    Exp0_result,
    FakeWaitExp0,
    FakeResultExp0,
    Exp1,
    Exp1_result,
    FakeWaitExp1,
    FakeResultExp1,
    Exp2,
    Exp2_result,
    FakeWaitExp2,
    FakeResultExp2,
    Exp3,
    Exp3_result,
    FakeWaitExp3,
    FakeResultExp3,
    Page1,
    Page2,
    Page3,
    Result
]
