from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import csv

class Donation_party(Page):
    form_model = models.Player
    form_fields = ['donation_party']

    def before_next_page(self):
        if self.player.donation_party == 2:   #如果选择猜donation
            if self.player.partner == 1:  #选择和意见相反的人玩游戏
                if self.participant.vars['issue'] != 999:   #如果不是极端情况
                    num = self.participant.vars['issue']    #需要匹配的issue号码
                    # self_preference = self.participant.vars['preference_%s' % num]  #匹配自己的issue，得到代表偏好的号码
                    self_opinion = self.participant.vars['opinion_%s' % num] #得到自己的意见 agree or disagree
                    if self_opinion == 'Agree':  #找对方的意见
                        other_opinion = 'Oppose'
                    else:
                        other_opinion = 'Favor'

                    # other_preference = self_preference  #由于是和意见相反的人做游戏，所以preference要一致

                    with open('likert/data.csv') as f:
                        all_objects = list(csv.DictReader(f))

                    dona_1 = []
                    dona_2 = []
                    dona_3 = []
                    dona_correct = []
                    for i in range(len(all_objects)):
                        if all_objects[i]['opinion_%s' % num] == other_opinion:
                            # if all_objects[i]['level_%s' % num] == str(other_preference):
                            if all_objects[i]['donation_1'] != '':   #如果是有donation的
                                dona_1.append(all_objects[i]['donation_1'])
                                dona_2.append(all_objects[i]['donation_2'])
                                dona_3.append(all_objects[i]['donation_3'])
                                dona_correct.append(all_objects[i]['donation_correct'])
                                # else:
                                #     pass
                            else:
                                pass
                        else:
                            pass

                    if len(dona_1) == 0:  #如果没有找到合适的人
                        self.player.if_random = 1  #标记：接下来的工作都是随机进行
                        self.player.donation1 = random.choice(Constants.organization)
                        list_temp_1 = [self.player.donation1]
                        list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                        self.player.donation2 = random.choice(list_new_1)
                        list_temp_2 = [self.player.donation1, self.player.donation2]
                        list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                        self.player.donation3 = random.choice(list_new_2)
                        self.player.donation_correct = 'None'  #随机选的，没有正确答案
                        for i in range(10):  #找donation org的号码
                            if Constants.organization[i] == self.player.donation1:
                                numb1 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb2 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb3 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb1]
                        self.player.description2 = Constants.description[numb2]
                        self.player.description3 = Constants.description[numb3]
                    else:
                        self.player.if_random = 0
                        self.player.donation1 = random.choice(dona_1)  #随机选择一个人
                        for i in range(len(dona_1)):
                            if dona_1[i] == self.player.donation1:
                                numb4 = i
                        self.player.donation2 = dona_2[numb4]
                        self.player.donation3 = dona_3[numb4]
                        self.player.donation_correct = dona_correct[numb4]
                        for i in range(10):
                            if Constants.organization[i] == self.player.donation1:
                                numb5 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb6 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb7 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb5]
                        self.player.description2 = Constants.description[numb6]
                        self.player.description3 = Constants.description[numb7]

                    self.player.other_opinion = other_opinion
                    # if other_preference == 1:
                    #     self.player.other_preference = 'a great deal'
                    # elif other_preference == 2:
                    #     self.player.other_preference = 'a moderate amount'
                    # else:
                    #     self.player.other_preference = 'a little'
                # 如果是极端情况, 那么选取任何一个意见相左的人的donation
                else:
                    num = self.participant.vars['issue']    #需要匹配的issue号码

                    with open('likert/data.csv') as f:
                        all_objects = list(csv.DictReader(f))

                    dona_1 = []
                    dona_2 = []
                    dona_3 = []
                    dona_correct = []
                    opinion_list = []
                    preference_list = []
                    for i in range(len(all_objects)):
                        if all_objects[i]['opinion_%s' % num] != 'Neither favor nor oppose':
                            if all_objects[i]['donation_1'] != '':   #如果是有donation的
                                dona_1.append(all_objects[i]['donation_1'])
                                dona_2.append(all_objects[i]['donation_2'])
                                dona_3.append(all_objects[i]['donation_3'])
                                dona_correct.append(all_objects[i]['donation_correct'])
                                opinion_list.append(all_objects[i]['opinion_%s' % num])
                                # preference_list.append(all_objects[i]['level_%s' % num])
                            else:
                                pass

                    if len(dona_1) == 0:
                        self.player.if_random = 1  #标记：接下来的工作都是随机进行
                        self.player.donation1 = random.choice(Constants.organization)
                        list_temp_1 = [self.player.donation1]
                        list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                        self.player.donation2 = random.choice(list_new_1)
                        list_temp_2 = [self.player.donation1, self.player.donation2]
                        list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                        self.player.donation3 = random.choice(list_new_2)
                        self.player.donation_correct = 'None'  #随机选的，没有正确答案
                        for i in range(10):  #找donation org的号码
                            if Constants.organization[i] == self.player.donation1:
                                numb10 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb11 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb12 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb10]
                        self.player.description2 = Constants.description[numb11]
                        self.player.description3 = Constants.description[numb12]

                        other_opinion = random.choice(['Favor', 'Oppose'])
                        # other_preference = str(random.choice([1, 2, 3]))
                    else:
                        self.player.if_random = 0
                        self.player.donation1 = random.choice(dona_1)  # 随机选择一个人
                        for i in range(len(dona_1)):
                            if dona_1[i] == self.player.donation1:
                                numb8 = i
                        self.player.donation2 = dona_2[numb8]
                        self.player.donation3 = dona_3[numb8]
                        self.player.donation_correct = dona_correct[numb8]
                        # other_preference = preference_list[numb8]  #记录下选择的人的preference 和 opinion
                        other_opinion = opinion_list[numb8]
                        for i in range(10):
                            if Constants.organization[i] == self.player.donation1:
                                numb5 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb6 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb7 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb5]
                        self.player.description2 = Constants.description[numb6]
                        self.player.description3 = Constants.description[numb7]

                    self.player.other_opinion = other_opinion
                    # if other_preference == '1':
                    #     self.player.other_preference = 'a great deal'
                    # elif other_preference == '2':
                    #     self.player.other_preference = 'a moderate amount'
                    # else:
                    #     self.player.other_preference = 'a little'


            elif self.player.partner == 3: # 玩家选择和自己意见相同的人玩游戏

                if self.participant.vars['issue'] != 999:   #如果不是极端情况
                    num = self.participant.vars['issue']    #需要匹配的issue号码
                    # self_preference = self.participant.vars['preference_%s' % num]  #匹配自己的issue，得到代表偏好的号码
                    self_opinion = self.participant.vars['opinion_%s' % num] #得到自己的意见 agree or disagree
                    if self_opinion == 'Agree':
                        other_opinion = 'Favor'
                    else:
                        other_opinion = 'Oppose'

                    with open('likert/data.csv') as f:
                        all_objects = list(csv.DictReader(f))

                    # other_preference = self_preference

                    dona_1 = []
                    dona_2 = []
                    dona_3 = []
                    dona_correct = []
                    for i in range(len(all_objects)):
                        if all_objects[i]['opinion_%s' % num] == other_opinion:
                            # if all_objects[i]['level_%s' % num] == str(other_preference):
                            if all_objects[i]['donation_1'] != '':  # 如果是有donation的
                                dona_1.append(all_objects[i]['donation_1'])
                                dona_2.append(all_objects[i]['donation_2'])
                                dona_3.append(all_objects[i]['donation_3'])
                                dona_correct.append(all_objects[i]['donation_correct'])
                                # else:
                                #     pass
                            else:
                                pass
                        else:
                            pass

                    if len(dona_1) == 0:  # 如果没有找到合适的人
                        self.player.if_random = 1  # 标记：接下来的工作都是随机进行
                        self.player.donation1 = random.choice(Constants.organization)
                        list_temp_1 = [self.player.donation1]
                        list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                        self.player.donation2 = random.choice(list_new_1)
                        list_temp_2 = [self.player.donation1, self.player.donation2]
                        list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                        self.player.donation3 = random.choice(list_new_2)
                        self.player.donation_correct = 'None'  # 随机选的，没有正确答案
                        for i in range(10):  # 找donation org的号码
                            if Constants.organization[i] == self.player.donation1:
                                numb1 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb2 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb3 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb1]
                        self.player.description2 = Constants.description[numb2]
                        self.player.description3 = Constants.description[numb3]
                    else:
                        self.player.if_random = 0
                        self.player.donation1 = random.choice(dona_1)  # 随机选择一个人
                        for i in range(len(dona_1)):
                            if dona_1[i] == self.player.donation1:
                                numb4 = i
                        self.player.donation2 = dona_2[numb4]
                        self.player.donation3 = dona_3[numb4]
                        self.player.donation_correct = dona_correct[numb4]
                        for i in range(10):
                            if Constants.organization[i] == self.player.donation1:
                                numb5 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb6 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb7 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb5]
                        self.player.description2 = Constants.description[numb6]
                        self.player.description3 = Constants.description[numb7]


                else: #极端的case
                    num = self.participant.vars['issue']  # 需要匹配的issue号码

                    other_opinion = 'Neither favor nor oppose'

                    with open('likert/data.csv') as f:
                        all_objects = list(csv.DictReader(f))

                    dona_1 = []
                    dona_2 = []
                    dona_3 = []
                    dona_correct = []
                    opinion_list = []
                    preference_list = []
                    for i in range(len(all_objects)):
                        if all_objects[i]['opinion_%s' % num] == 'Neither favor nor oppose':
                            if all_objects[i]['donation_1'] != '':  # 如果是有donation的
                                dona_1.append(all_objects[i]['donation_1'])
                                dona_2.append(all_objects[i]['donation_2'])
                                dona_3.append(all_objects[i]['donation_3'])
                                dona_correct.append(all_objects[i]['donation_correct'])
                                opinion_list.append(all_objects[i]['opinion_%s' % num])
                                # preference_list.append(all_objects[i]['level_%s' % num])
                            else:
                                pass

                    if len(dona_1) == 0:
                        self.player.if_random = 1  # 标记：接下来的工作都是随机进行
                        self.player.donation1 = random.choice(Constants.organization)
                        list_temp_1 = [self.player.donation1]
                        list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                        self.player.donation2 = random.choice(list_new_1)
                        list_temp_2 = [self.player.donation1, self.player.donation2]
                        list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                        self.player.donation3 = random.choice(list_new_2)
                        self.player.donation_correct = 'None'  # 随机选的，没有正确答案
                        for i in range(10):  # 找donation org的号码
                            if Constants.organization[i] == self.player.donation1:
                                numb10 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb11 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb12 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb10]
                        self.player.description2 = Constants.description[numb11]
                        self.player.description3 = Constants.description[numb12]

                    else:
                        self.player.if_random = 0
                        self.player.donation1 = random.choice(dona_1)  # 随机选择一个人
                        for i in range(len(dona_1)):
                            if dona_1[i] == self.player.donation1:
                                numb8 = i
                        self.player.donation2 = dona_2[numb8]
                        self.player.donation3 = dona_3[numb8]
                        self.player.donation_correct = dona_correct[numb8]
                        for i in range(10):
                            if Constants.organization[i] == self.player.donation1:
                                numb5 = i
                            elif Constants.organization[i] == self.player.donation2:
                                numb6 = i
                            elif Constants.organization[i] == self.player.donation3:
                                numb7 = i
                            else:
                                pass
                        self.player.description1 = Constants.description[numb5]
                        self.player.description2 = Constants.description[numb6]
                        self.player.description3 = Constants.description[numb7]

                self.player.other_opinion = other_opinion
                # if other_opinion != 'Neither favor nor oppose':
                #     self.player.other_preference = other_preference
                # else:
                #     pass

            elif self.player.partner == 2: #和相反党派的人玩游戏
                self_party = self.player.partisanship1
                if self_party == 1: #自己是demo
                    other_party = 2
                elif self_party == 2:
                    other_party = 1
                else:
                    # other_party = random.choice([1, 2]) #中立的话，随机为他选择对方的党派
                    pass

                with open('likert/data.csv') as f:
                    all_objects = list(csv.DictReader(f))

                party_list = []
                dona_1 = []
                dona_2 = []
                dona_3 = []
                dona_correct = []
                for i in range(len(all_objects)):
                    if all_objects[i]['partisanship_1'] == str(other_party):
                        if all_objects[i]['donation_1'] != '':  # 如果是有donation的
                            dona_1.append(all_objects[i]['donation_1'])
                            dona_2.append(all_objects[i]['donation_2'])
                            dona_3.append(all_objects[i]['donation_3'])
                            dona_correct.append(all_objects[i]['donation_correct'])
                            # party_list.append(all_objects[i]['partisanship_1'])
                        else:
                            pass

                if len(dona_1) == 0:  # 如果没有找到合适的人
                    self.player.if_random = 1  # 标记：接下来的工作都是随机进行
                    self.player.donation1 = random.choice(Constants.organization)
                    list_temp_1 = [self.player.donation1]
                    list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                    self.player.donation2 = random.choice(list_new_1)
                    list_temp_2 = [self.player.donation1, self.player.donation2]
                    list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                    self.player.donation3 = random.choice(list_new_2)
                    self.player.donation_correct = 'None'  # 随机选的，没有正确答案
                    for i in range(10):  # 找donation org的号码
                        if Constants.organization[i] == self.player.donation1:
                            numb10 = i
                        elif Constants.organization[i] == self.player.donation2:
                            numb11 = i
                        elif Constants.organization[i] == self.player.donation3:
                            numb12 = i
                        else:
                            pass
                    self.player.description1 = Constants.description[numb10]
                    self.player.description2 = Constants.description[numb11]
                    self.player.description3 = Constants.description[numb12]
                else:
                    self.player.if_random = 0
                    self.player.donation1 = random.choice(dona_1)  # 随机选择一个人
                    for i in range(len(dona_1)):
                        if dona_1[i] == self.player.donation1:
                            numb8 = i
                    self.player.donation2 = dona_2[numb8]
                    self.player.donation3 = dona_3[numb8]
                    self.player.donation_correct = dona_correct[numb8]
                    for i in range(10):
                        if Constants.organization[i] == self.player.donation1:
                            numb5 = i
                        elif Constants.organization[i] == self.player.donation2:
                            numb6 = i
                        elif Constants.organization[i] == self.player.donation3:
                            numb7 = i
                        else:
                            pass
                    self.player.description1 = Constants.description[numb5]
                    self.player.description2 = Constants.description[numb6]
                    self.player.description3 = Constants.description[numb7]

                if other_party == 1:
                    self.player.other_party = 'Democrat'
                else:
                    self.player.other_party = 'Republican'


            else: #和相同党派的人玩
                self_party = self.player.partisanship1
                if self_party == 1:
                    other_party = 1
                elif self_party == 2:
                    other_party = 2
                else:
                    # other_party = 999
                    pass

                with open('likert/data.csv') as f:
                    all_objects = list(csv.DictReader(f))

                party_list = []
                dona_1 = []
                dona_2 = []
                dona_3 = []
                dona_correct = []
                for i in range(len(all_objects)):
                    if other_party == 999:
                        if all_objects[i]['partisanship_1'] == '3' or all_objects[i]['partisanship_1'] == '5' or all_objects[i]['partisanship_1'] == '8':
                            if all_objects[i]['donation_1'] != '':  # 如果是有donation的
                                dona_1.append(all_objects[i]['donation_1'])
                                dona_2.append(all_objects[i]['donation_2'])
                                dona_3.append(all_objects[i]['donation_3'])
                                dona_correct.append(all_objects[i]['donation_correct'])
                                party_list.append(all_objects[i]['partisanship_1'])
                            else:
                                pass
                        else:
                            pass
                    else:
                        if all_objects[i]['partisanship_1'] == str(other_party):
                            if all_objects[i]['donation_1'] != '':  # 如果是有donation的
                                dona_1.append(all_objects[i]['donation_1'])
                                dona_2.append(all_objects[i]['donation_2'])
                                dona_3.append(all_objects[i]['donation_3'])
                                dona_correct.append(all_objects[i]['donation_correct'])
                                party_list.append(all_objects[i]['partisanship_1'])
                            else:
                                pass

                if len(dona_1) == 0:  # 如果没有找到合适的人
                    self.player.if_random = 1  # 标记：接下来的工作都是随机进行
                    self.player.donation1 = random.choice(Constants.organization)
                    list_temp_1 = [self.player.donation1]
                    list_new_1 = [i for i in Constants.organization if i not in list_temp_1]
                    self.player.donation2 = random.choice(list_new_1)
                    list_temp_2 = [self.player.donation1, self.player.donation2]
                    list_new_2 = [i for i in Constants.organization if i not in list_temp_2]
                    self.player.donation3 = random.choice(list_new_2)
                    self.player.donation_correct = 'None'  # 随机选的，没有正确答案
                    for i in range(10):  # 找donation org的号码
                        if Constants.organization[i] == self.player.donation1:
                            numb10 = i
                        elif Constants.organization[i] == self.player.donation2:
                            numb11 = i
                        elif Constants.organization[i] == self.player.donation3:
                            numb12 = i
                        else:
                            pass
                    self.player.description1 = Constants.description[numb10]
                    self.player.description2 = Constants.description[numb11]
                    self.player.description3 = Constants.description[numb12]
                else:
                    self.player.if_random = 0
                    self.player.donation1 = random.choice(dona_1)  # 随机选择一个人
                    for i in range(len(dona_1)):
                        if dona_1[i] == self.player.donation1:
                            numb8 = i
                    self.player.donation2 = dona_2[numb8]
                    self.player.donation3 = dona_3[numb8]
                    self.player.donation_correct = dona_correct[numb8]
                    # self.player.other_party = party_list[numb8]
                    for i in range(10):
                        if Constants.organization[i] == self.player.donation1:
                            numb5 = i
                        elif Constants.organization[i] == self.player.donation2:
                            numb6 = i
                        elif Constants.organization[i] == self.player.donation3:
                            numb7 = i
                        else:
                            pass
                    self.player.description1 = Constants.description[numb5]
                    self.player.description2 = Constants.description[numb6]
                    self.player.description3 = Constants.description[numb7]

                if self_party == 1:  # 党派只有两个
                    self.player.other_party = 'Democrat'
                else:
                    self.player.other_party = 'Republican'
                # elif self_party == 3:
                #     self.player.other_party = 'Independent'
                # elif self_party == 5:
                #     self.player.other_party = 'Other party'
                # else:
                #     self.player.other_party = 'Do not know'

        # 猜党派: 选项是固定的
        else:
            if self.player.partner == 1: #和意见相反的人玩
                num = self.participant.vars['issue']  # 需要匹配的issue号码
                # self_preference = self.participant.vars['preference_%s' % num]  # 匹配自己的issue，得到代表偏好的号码
                self_opinion = self.participant.vars['opinion_%s' % num]  # 得到自己的意见 agree or disagree
                if self_opinion == 'Agree':  # 找对方的意见
                    other_opinion = 'Oppose'
                else:
                    other_opinion = 'Favor'

                # other_preference = self_preference  # 由于是和意见相反的人做游戏，所以preference要一致

                with open('likert/data.csv') as f:
                    all_objects = list(csv.DictReader(f))

                party_list_1 = []
                party_list_2 = []
                party_list_3 = []
                for i in range(len(all_objects)):
                    if all_objects[i]['opinion_%s' % num] == other_opinion:
                        # if all_objects[i]['level_%s' % num] == str(other_preference):
                        party_list_1.append(all_objects[i]['partisanship_1'])
                        party_list_2.append(all_objects[i]['partisanship_2'])
                        party_list_3.append(all_objects[i]['partisanship_3'])
                        # else:
                        #     pass
                    else:
                        pass

                if len(party_list_1) == 0:  # 如果没有找到合适的人
                    self.player.party_identification = random.choice(['Strong Democrat', 'Not very strong Democrat', 'Do not know', 'Inapplicable', 'Not very strong Republican', 'Strong Republican', 'Closer to Republican', 'Closer to Democratic', 'Neither closer to Republican nor Democratic'])
                else:
                    party1 = random.choice(party_list_1)
                    for i in range(len(party_list_1)):
                        if party_list_1[i] == party1:
                            numbx = i
                        else:
                            pass
                    party2 = party_list_2[numbx]
                    party3 = party_list_3[numbx]
                    if party1 == '1':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Democrat'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Democrat'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    elif party1 == '2':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Republican'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Republican'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    else:
                        if party3 == '1':
                            self.player.party_identification = 'Closer to Republican'
                        elif party3 == '2':
                            self.player.party_identification = 'Closer to Democratic'
                        else:
                            self.player.party_identification = 'Neither closer to Republican nor Democratic'

            elif self.player.partner == 3: #和意见相同的人玩
                num = self.participant.vars['issue']  # 需要匹配的issue号码
                # self_preference = self.participant.vars['preference_%s' % num]  # 匹配自己的issue，得到代表偏好的号码
                self_opinion = self.participant.vars['opinion_%s' % num]  # 得到自己的意见 agree or disagree
                if self_opinion == 'Agree':  # 找对方的意见
                    other_opinion = 'Favor'
                else:
                    other_opinion = 'Oppose'

                with open('likert/data.csv') as f:
                    all_objects = list(csv.DictReader(f))

                party_list_1 = []
                party_list_2 = []
                party_list_3 = []
                for i in range(len(all_objects)):
                    if all_objects[i]['opinion_%s' % num] == other_opinion:
                        # if all_objects[i]['level_%s' % num] == str(other_preference):
                        party_list_1.append(all_objects[i]['partisanship_1'])
                        party_list_2.append(all_objects[i]['partisanship_2'])
                        party_list_3.append(all_objects[i]['partisanship_3'])
                        # else:
                        #     pass
                    else:
                        pass

                if len(party_list_1) == 0:  # 如果没有找到合适的人
                    self.player.party_identification = random.choice(['Strong Democrat', 'Not very strong Democrat', 'Do not know', 'Inapplicable', 'Not very strong Republican', 'Strong Republican', 'Closer to Republican', 'Closer to Democratic', 'Neither closer to Republican nor Democratic'])
                else:
                    party1 = random.choice(party_list_1)
                    for i in range(len(party_list_1)):
                        if party_list_1[i] == party1:
                            numbx = i
                        else:
                            pass
                    party2 = party_list_2[numbx]
                    party3 = party_list_3[numbx]
                    if party1 == '1':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Democrat'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Democrat'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    elif party1 == '2':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Republican'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Republican'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    else:
                        if party3 == '1':
                            self.player.party_identification = 'Closer to Republican'
                        elif party3 == '2':
                            self.player.party_identification = 'Closer to Democratic'
                        else:
                            self.player.party_identification = 'Neither closer to Republican nor Democratic'

            elif self.player.partner == 2: #和不同党派的人玩
                party0 = self.player.partisanship1
                if party0 == 1:
                    other_party = 2
                elif party0 == 2:
                    other_party = 1
                else:
                    other_party = random.choice([1, 2])

                with open('likert/data.csv') as f:
                    all_objects = list(csv.DictReader(f))

                party_list_1 = []
                party_list_2 = []
                party_list_3 = []
                for i in range(len(all_objects)):
                    if all_objects[i]['partisanship_1'] == str(other_party):
                        # if all_objects[i]['level_%s' % num] == str(other_preference):
                        party_list_1.append(all_objects[i]['partisanship_1'])
                        party_list_2.append(all_objects[i]['partisanship_2'])
                        party_list_3.append(all_objects[i]['partisanship_3'])
                        # else:
                        #     pass
                    else:
                        pass

                if len(party_list_1) == 0:  # 如果没有找到合适的人
                    self.player.party_identification = random.choice(['Strong Democrat', 'Not very strong Democrat', 'Do not know', 'Inapplicable', 'Not very strong Republican', 'Strong Republican', 'Closer to Republican', 'Closer to Democratic', 'Neither closer to Republican nor Democratic'])
                else:
                    party1 = random.choice(party_list_1)
                    for i in range(len(party_list_1)):
                        if party_list_1[i] == party1:
                            numbx = i
                        else:
                            pass
                    party2 = party_list_2[numbx]
                    party3 = party_list_3[numbx]
                    if party1 == '1':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Democrat'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Democrat'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    elif party1 == '2':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Republican'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Republican'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    else:
                        if party3 == '1':
                            self.player.party_identification = 'Closer to Republican'
                        elif party3 == '2':
                            self.player.party_identification = 'Closer to Democratic'
                        else:
                            self.player.party_identification = 'Neither closer to Republican nor Democratic'

            else: #和相同党派的人玩
                party0 = self.player.partisanship1
                if party0 == 1:
                    other_party = 1
                elif party0 == 2:
                    other_party = 2
                else:
                    other_party = party0

                with open('likert/data.csv') as f:
                    all_objects = list(csv.DictReader(f))

                party_list_1 = []
                party_list_2 = []
                party_list_3 = []
                for i in range(len(all_objects)):
                    if all_objects[i]['partisanship_1'] == str(other_party):
                        # if all_objects[i]['level_%s' % num] == str(other_preference):
                        party_list_1.append(all_objects[i]['partisanship_1'])
                        party_list_2.append(all_objects[i]['partisanship_2'])
                        party_list_3.append(all_objects[i]['partisanship_3'])
                        # else:
                        #     pass
                    else:
                        pass

                if len(party_list_1) == 0:  # 如果没有找到合适的人
                    self.player.party_identification = random.choice(
                        ['Strong Democrat', 'Not very strong Democrat', 'Do not know', 'Inapplicable',
                         'Not very strong Republican', 'Strong Republican', 'Closer to Republican',
                         'Closer to Democratic', 'Neither closer to Republican nor Democratic'])
                else:
                    party1 = random.choice(party_list_1)
                    for i in range(len(party_list_1)):
                        if party_list_1[i] == party1:
                            numbx = i
                        else:
                            pass
                    party2 = party_list_2[numbx]
                    party3 = party_list_3[numbx]
                    if party1 == '1':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Democrat'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Democrat'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    elif party1 == '2':
                        if party2 == '1':
                            self.player.party_identification = 'Strong Republican'
                        elif party2 == '2':
                            self.player.party_identification = 'Not very strong Republican'
                        elif party2 == '5':
                            self.player.party_identification = 'Inapplicable'
                        else:
                            self.player.party_identification = 'Do not know'
                    else:
                        if party3 == '1':
                            self.player.party_identification = 'Closer to Republican'
                        elif party3 == '2':
                            self.player.party_identification = 'Closer to Democratic'
                        else:
                            self.player.party_identification = 'Neither closer to Republican nor Democratic'

    def is_displayed(self):
        return self.participant.vars['group'] == '1LG' or self.participant.vars['group'] == '1QG' or \
                self.participant.vars['group'] == '1QNG' or self.participant.vars['group'] == '2LG' or \
                self.participant.vars['group'] == '2QG' or self.participant.vars['group'] == '2QNG' or \
                self.participant.vars['group'] == '3LG' or self.participant.vars['group'] == '3QG' or \
                self.participant.vars['group'] == '3QNG'

# 现在有一些疑问，第一，partisanship放在哪里合适，第二，如果这个player是中立的，那么选择和同一党派的人玩猜党派的游戏该怎么办。
