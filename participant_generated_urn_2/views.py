from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Decide(Page):
    form_model = models.Player
    form_fields = ['decision']

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'htmla': htmla,
                'htmlb': htmlb}

    def decision_choices(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return [['A', htmla],
                ['B', htmlb]]


class Decide2(Page):

    form_model = models.Player
    form_fields = ['option1', 'option2', 'option3', 'option4']

    def is_displayed(self):
        return self.player.treatment == 'Participant'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'htmla': htmla,
                'htmlb': htmlb}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        id_num = []
        other_result = []
        for p in self.player.get_others_in_group():
            id_num.append(p.id_in_group)
            if self.group.symbol_pair == 'uparrow':
                if p.decision == 'A':
                    decision = '↗'
                else:
                    decision = '↖'
            elif self.group.symbol_pair == 'downarrow':
                if p.decision == 'A':
                    decision = '↙'
                else:
                    decision = '↘︎'
            elif self.group.symbol_pair == 'heart':
                if p.decision == 'A':
                    decision = '♡'
                else:
                    decision = '☺︎'
            elif self.group.symbol_pair == 'circle':
                if p.decision == 'A':
                    decision = '◯'
                else:
                    decision = '•'
            elif self.group.symbol_pair == 'downzhe':
                if p.decision == 'A':
                    decision = '┓'
                else:
                    decision = '┏︎'
            elif self.group.symbol_pair == 'upzhe':
                if p.decision == 'A':
                    decision = '┗'
                else:
                    decision = '┛'
            elif self.group.symbol_pair == 'square':
                if p.decision == 'A':
                    decision = '■'
                else:
                    decision = '□'
            elif self.group.symbol_pair == 'arrow':
                if p.decision == 'A':
                    decision = '↔'
                else:
                    decision = '↕'
            elif self.group.symbol_pair == 'line':
                if p.decision == 'A':
                    decision = '—'
                else:
                    decision = '|︎'
            elif self.group.symbol_pair == 'circle2':
                if p.decision == 'A':
                    decision = '◌'
                else:
                    decision = '●'
            elif self.group.symbol_pair == 'theta':
                if p.decision == 'A':
                    decision = 'φ'
                else:
                    decision = 'θ︎'
            elif self.group.symbol_pair == 'question':
                if p.decision == 'A':
                    decision = 'ʔ'
                else:
                    decision = 'ʕ'
            else:
                if p.decision == 'A':
                    decision = '⑪'
                else:
                    decision = '⓫'

            other_result.append(decision)

        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
            if self.player.result == 'A':
                result = '↗'
            else:
                result = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
            if self.player.result == 'A':
                result = '↙'
            else:
                result = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
            if self.player.result == 'A':
                result = '♡'
            else:
                result = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
            if self.player.result == 'A':
                result = '◯'
            else:
                result = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏'
            if self.player.result == 'A':
                result = '┓'
            else:
                result = '┏'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛︎'
            if self.player.result == 'A':
                result = '┗'
            else:
                result = '┛︎'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
            if self.player.result == 'A':
                result = '■'
            else:
                result = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
            if self.player.result == 'A':
                result = '—'
            else:
                result = '|︎'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
            if self.player.result == 'A':
                result = '↔'
            else:
                result = '↕︎'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
            if self.player.result == 'A':
                result = '◌'
            else:
                result = '●'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ︎'
            if self.player.result == 'A':
                result = 'ʔ'
            else:
                result = 'ʕ︎'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
            if self.player.result == 'A':
                result = 'φ'
            else:
                result = 'θ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
            if self.player.result == 'A':
                result = '⑪'
            else:
                result = '⓫'

        mylist = zip(id_num, other_result)

        return {'list': mylist,
                'result': result,
                'htmla': htmla,
                'htmlb': htmlb}

    def is_displayed(self):
        return self.player.treatment == 'Participant'


class FirstWait(WaitPage):
    group_by_arrival_time = True
    players_per_group = 4

    def after_all_players_arrive(self):
        # Retrieve the condition assignments from each participant so far
        conditions_so_far = []
        symbols_so_far = []
        for g in self.subsession.get_groups():
            conditions_so_far.append(g.treatment)
            symbols_so_far.append(g.symbol_pair)

        # Count how often each condition has been run
        conditions_n = {}
        symbols_n = {}
        for c in Constants.conditions:
            conditions_n[c] = conditions_so_far.count(c)
        for s in Constants.symbols:
            symbols_n[s] = symbols_so_far.count(s)

        # Create a new array containing the conditions that have been run the least amount of times
        conditions = []
        symbols = []
        for c, n in conditions_n.items():
            if n == min(conditions_n.values()):
                conditions.append(c)
        for s, n in symbols_n.items():
            if n == min(symbols_n.values()):
                symbols.append(s)

        # Randomly assign the participant to one of these conditions
        self.group.treatment = random.choice(conditions)
        self.group.symbol_pair = random.choice(symbols)

        for p in self.group.get_players():
            p.treatment = self.group.treatment


class Introduction(Page):
    form_model = models.Player
    form_fields = ['decision']

    def decision_choices(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return [['A', htmla],
                ['B', htmlb]]

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'total': 3,
                'htmla': htmla,
                'htmlb': htmlb}

    def is_displayed(self):
        return self.player.treatment == 'Participant'


class Decide_exp(Page):

    form_model = models.Player
    form_fields = ['option1', 'option2', 'option3', 'option4']

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'htmla': htmla,
                'htmlb': htmlb}


class Results_2(Page):

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'

        if self.group.symbol_pair == 'uparrow':
            if self.player.result == 'A':
                result = '↗'
            else:
                result = '↖'
        elif self.group.symbol_pair == 'downarrow':
            if self.player.result == 'A':
                result = '↙'
            else:
                result = '↘︎'
        elif self.group.symbol_pair == 'heart':
            if self.player.result == 'A':
                result = '♡'
            else:
                result = '☺︎'
        elif self.group.symbol_pair == 'circle':
            if self.player.result == 'A':
                result = '◯'
            else:
                result = '•'
        elif self.group.symbol_pair == 'downzhe':
            if self.player.result == 'A':
                result = '┓'
            else:
                result = '┏'
        elif self.group.symbol_pair == 'upzhe':
            if self.player.result == 'A':
                result = '┗'
            else:
                result = '┛'
        elif self.group.symbol_pair == 'square':
            if self.player.result == 'A':
                result = '■'
            else:
                result = '□'
        elif self.group.symbol_pair == 'line':
            if self.player.result == 'A':
                result = '—'
            else:
                result = '|︎'
        elif self.group.symbol_pair == 'arrow':
            if self.player.result == 'A':
                result = '↔'
            else:
                result = '↕'
        elif self.group.symbol_pair == 'circle2':
            if self.player.result == 'A':
                result = '◌'
            else:
                result = '●'
        elif self.group.symbol_pair == 'theta':
            if self.player.result == 'A':
                result = 'φ'
            else:
                result = 'θ'
        elif self.group.symbol_pair == 'question':
            if self.player.result == 'A':
                result = 'ʔ'
            else:
                result = 'ʕ︎'
        else:
            if self.player.result == 'A':
                result = '⑪'
            else:
                result = '⓫'

        return {'htmla': htmla,
                'htmlb': htmlb,
                'result': result}


class Introduction_2(Page):

    def is_displayed(self):
        return self.player.treatment == 'Experimenter'

    def vars_for_template(self):
        if self.group.symbol_pair == 'uparrow':
            htmla = '↗'
            htmlb = '↖'
        elif self.group.symbol_pair == 'downarrow':
            htmla = '↙'
            htmlb = '↘︎'
        elif self.group.symbol_pair == 'heart':
            htmla = '♡'
            htmlb = '☺︎'
        elif self.group.symbol_pair == 'circle':
            htmla = '◯'
            htmlb = '•'
        elif self.group.symbol_pair == 'downzhe':
            htmla = '┓'
            htmlb = '┏︎'
        elif self.group.symbol_pair == 'upzhe':
            htmla = '┗'
            htmlb = '┛'
        elif self.group.symbol_pair == 'square':
            htmla = '■'
            htmlb = '□'
        elif self.group.symbol_pair == 'line':
            htmla = '—'
            htmlb = '|'
        elif self.group.symbol_pair == 'arrow':
            htmla = '↔'
            htmlb = '↕'
        elif self.group.symbol_pair == 'circle2':
            htmla = '◌'
            htmlb = '●'
        elif self.group.symbol_pair == 'theta':
            htmla = 'φ'
            htmlb = 'θ'
        elif self.group.symbol_pair == 'question':
            htmla = 'ʔ'
            htmlb = 'ʕ'
        else:
            htmla = '⑪'
            htmlb = '⓫'
        return {'total': 3,
                'htmla': htmla,
                'htmlb': htmlb}


class Belief(Page):
    form_model = models.Player
    form_fields = ['belief']

    def vars_for_template(self):
        return {'sum': 3}

    def belief_choices(self):
        if self.group.symbol_pair == 'uparrow':
            one = '0 chose ↗ and 3 chose ↖'
            two = '1 chose ↗ and 2 chose ↖'
            three = '2 chose ↗ and 1 chose ↖'
            four = '3 chose ↗ and 0 chose ↖'
        elif self.group.symbol_pair == 'downarrow':
            one = '0 chose ↙ and 3 chose ↘'
            two = '1 chose ↙ and 2 chose ↘'
            three = '2 chose ↙ and 1 chose ↘'
            four = '3 chose ↙ and 0 chose ↘'
        elif self.group.symbol_pair == 'heart':
            one = '0 chose ♡ and 3 chose ☺︎'
            two = '1 chose ♡ and 2 chose ☺︎'
            three = '2 chose ♡ and 1 chose ☺︎'
            four = '3 chose ♡ and 0 chose ☺︎'
        elif self.group.symbol_pair == 'circle':
            one = '0 chose ◯ and 3 chose •'
            two = '1 chose ◯ and 2 chose •'
            three = '2 chose ◯ and 1 chose •'
            four = '3 chose ◯ and 0 chose •'
        elif self.group.symbol_pair == 'downzhe':
            one = '0 chose ┓ and 3 chose ┏'
            two = '1 chose ┓ and 2 chose ┏'
            three = '2 chose ┓ and 1 chose ┏'
            four = '3 chose ┓ and 0 chose ┏'
        elif self.group.symbol_pair == 'upzhe':
            one = '0 chose ┗ and 3 chose ┛︎'
            two = '1 chose ┗ and 2 chose ┛︎'
            three = '2 chose ┗ and 1 chose ┛︎'
            four = '3 chose ┗ and 0 chose ┛'
        elif self.group.symbol_pair == 'square':
            one = '0 chose ■ and 3 chose □'
            two = '1 chose ■ and 2 chose □'
            three = '2 chose ■ and 1 chose □'
            four = '3 chose ■ and 0 chose □'
        elif self.group.symbol_pair == 'line':
            one = '0 chose — and 3 chose |'
            two = '1 chose — and 2 chose |'
            three = '2 chose — and 1 chose |'
            four = '3 chose — and 0 chose |'
        elif self.group.symbol_pair == 'arrow':
            one = '0 chose ↔ and 3 chose ↕'
            two = '1 chose ↔ and 2 chose ↕'
            three = '2 chose ↔ and 1 chose ↕'
            four = '3 chose ↔ and 0 chose ↕︎'
        elif self.group.symbol_pair == 'circle2':
            one = '0 chose ◌ and 3 chose ●'
            two = '1 chose ◌ and 2 chose ●'
            three = '2 chose ◌ and 1 chose ●'
            four = '3 chose ◌ and 0 chose ●'
        elif self.group.symbol_pair == 'theta':
            one = '0 chose φ and 3 chose θ'
            two = '1 chose φ and 2 chose θ'
            three = '2 chose φ and 1 chose θ'
            four = '3 chose φ and 0 chose θ'
        elif self.group.symbol_pair == 'question':
            one = '0 chose ʔ and 3 chose ʕ︎'
            two = '1 chose ʔ and 2 chose ʕ︎'
            three = '2 chose ʔ and 1 chose ʕ'
            four = '3 chose ʔ and 0 chose ʕ'
        else:
            one = '0 chose ⑪ and 3 chose ⓫'
            two = '1 chose ⑪ and 2 chose ⓫'
            three = '2 chose ⑪ and 1 chose ⓫'
            four = '3 chose ⑪ and 0 chose ⓫'

        return [[1, one],
                [2, two],
                [3, three],
                [4, four]]

    def is_displayed(self):
        return self.player.treatment == 'Participant'


class Demographic(Page):
    form_model = models.Player
    form_fields = ['citizenship', 'language', 'age', 'gender', 'educ', 'time', 'religion', 'income']



page_sequence = [
    FirstWait,
    Introduction,
    Introduction_2,
    Decide2,
    Decide_exp,
    Belief,
    Demographic,
    ResultsWaitPage,
    Results,
    Results_2
]
