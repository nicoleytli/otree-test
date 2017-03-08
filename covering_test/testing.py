import os
import random
import types

# class player:
#
#     def __init__(self):
#         self.audio_for_player_1 = []
#         self.audio_for_player_2 = []
#         self.audio_for_player_3 = []
#         self.audio_for_player_4 = []
#         self.audio_for_player_5 = []
#
#     def get_audios(self, pep):
#         path = "/Users/Nicole/Documents/oTree/covering_test/static/covering_test"  # insert the path to your directory
#         collection = os.listdir(path)
#         selected = set()  # the set don't allow repetition
#
#         while len(selected) <= 66:
#             selected.add(random.choice(collection))
#
#         temp = list(selected)
#         could = pep
#
#         self.audio_for_player_1 = temp[0]
#         self.audio_for_player_2 = temp[1]
#         self.audio_for_player_3 = temp[2]
#         self.audio_for_player_4 = temp[3]
#         self.audio_for_player_5 = temp[4]
#         # self.audio_for_player_6 = temp[5]
#         # self.audio_for_player_7 = temp[6]
#         # self.audio_for_player_8 = temp[7]
#         # self.audio_for_player_9 = temp[8]
#         # self.audio_for_player_10 = temp[9]
#         # self.audio_for_player_11 = temp[10]
#         # self.audio_for_player_12 = temp[11]
#         # self.audio_for_player_13 = temp[12]
#         # self.audio_for_player_14 = temp[13]
#         # self.audio_for_player_15 = temp[14]
#         # self.audio_for_player_16 = temp[15]
#         # self.audio_for_player_17 = temp[16]
#         # self.audio_for_player_18 = temp[17]
#         # self.audio_for_player_19 = temp[18]
#         # self.audio_for_player_20 = temp[19]
#         # self.audio_for_player_21 = temp[20]
#         # self.audio_for_player_22 = temp[21]
#         # self.audio_for_player_23 = temp[22]
#         # self.audio_for_player_24 = temp[23]
#         # self.audio_for_player_25 = temp[24]
#         # self.audio_for_player_26 = temp[25]
#         # self.audio_for_player_27 = temp[26]
#         # self.audio_for_player_28 = temp[27]
#         # self.audio_for_player_29 = temp[28]
#         # self.audio_for_player_30 = temp[29]
#         # self.audio_for_player_31 = temp[30]
#         # self.audio_for_player_32 = temp[31]
#         # self.audio_for_player_33 = temp[32]
#         # self.audio_for_player_34 = temp[33]
#         # self.audio_for_player_35 = temp[34]
#         # self.audio_for_player_36 = temp[35]
#         # self.audio_for_player_37 = temp[36]
#         # self.audio_for_player_38 = temp[37]
#         # self.audio_for_player_39 = temp[38]
#         # self.audio_for_player_40 = temp[39]
#         # self.audio_for_player_41 = temp[40]
#         # self.audio_for_player_42 = temp[41]
#         # self.audio_for_player_43 = temp[42]
#         # self.audio_for_player_44 = temp[43]
#         # self.audio_for_player_45 = temp[44]
#         # self.audio_for_player_46 = temp[45]
#         # self.audio_for_player_47 = temp[46]
#         # self.audio_for_player_48 = temp[47]
#         # self.audio_for_player_49 = temp[48]
#         # self.audio_for_player_50 = temp[49]
#         # self.audio_for_player_51 = temp[50]
#         # self.audio_for_player_52 = temp[51]
#         # self.audio_for_player_53 = temp[52]
#         # self.audio_for_player_54 = temp[53]
#         # self.audio_for_player_55 = temp[54]
#         # self.audio_for_player_56 = temp[55]
#         # self.audio_for_player_57 = temp[56]
#         # self.audio_for_player_58 = temp[57]
#         # self.audio_for_player_59 = temp[58]
#         # self.audio_for_player_60 = temp[59]
#         # self.audio_for_player_61 = temp[60]
#         # self.audio_for_player_62 = temp[61]
#         # self.audio_for_player_63 = temp[62]
#         # self.audio_for_player_64 = temp[63]
#         # self.audio_for_player_65 = temp[64]
#         # self.audio_for_player_66 = temp[65]
#
#         return could
#
#
#
# print(player.audio_for_player_1)
# name_list_1 = [['Very Unattractive', 'Very Attractive'], ['Not At All Masculine', 'Very Masculine'],
#                ['Not Intelligent', 'Intelligent'], ['Very Unaggressive', 'Very Aggressive'],
#                ['Not Trustworthy', 'Trustworthy'], ['Very Timid', 'Very Confident'],
#                ['Will Definitely Loss', 'Will Definitely Win'], ['Very Bad', 'Very Good']]
#
#
# def get_question(name_list_1):
#     temp = []
#     name_list_2 = []
#     direction = []
#
#     for i in range(len(name_list_1)):
#         random.shuffle(name_list_1[i])
#         temp.append(name_list_1[i])
#         if len(temp[i][0]) > len(temp[i][1]) and temp[i][0] != 'Very Confident' and temp[i][0] != 'Very Good':
#             direction.append('ascending')
#         elif temp[i][0] == 'Very Timid' or temp[i][0] == 'Very Bad':
#             direction.append('ascending')
#         else:
#             direction.append('descending')
#
#         name_list_2.append([i, temp[i][0], temp[i][1]])
#
#     name_list_3 = name_list_2[0:6]
#
#     random.shuffle(name_list_3)
#     name_list_3.extend(name_list_2[6:8])
#
#     for i in range(len(direction)):
#         for j in range(len(name_list_3)):
#             if name_list_3[j][0] == i:
#                 name_list_3[j].append(direction[i])
#             else:
#                 pass
#
#     name = {0: 'attractive', 1: 'masculine', 2: 'intelligent', 3: 'aggressive', 4: 'trustworthy', 5: 'confident',
#             6: 'win', 7: 'quality'}
#     for i in range(len(name_list_3)):
#         if name_list_3[i][0] in name:
#             name_list_3[i][0] = name[name_list_3[i][0]]
#
#     value_1 = [1, 2, 3, 4, 5, 6, 7]
#     value_2 = [7, 6, 5, 4, 3, 2, 1]
#     name_list_left = []
#     name_list_right = []
#     name_list = []
#     value = []
#
#     for i in range(len(name_list_3)):
#         if name_list_3[i][3] == 'ascending':
#             value.append(value_1)
#         else:
#             value.append(value_2)
#         name_list_left.append(name_list_3[i][1])
#         name_list_right.append(name_list_3[i][2])
#         name_list.append(name_list_3[i][0])
#
#     name_list_left_1 = name_list_left[0:6]
#     name_list_right_1 = name_list_right[0:6]
#     name_1 = name_list[0:6]
#     value_1 = value[0:6]
#     name_list_left_2 = name_list_left[6]
#     name_list_right_2 = name_list_right[6]
#     name_2 = name_list[6]
#     value_2 = value[6]
#     name_list_left_3 = name_list_left[7]
#     name_list_right_3 = name_list_right[7]
#     name_3 = name_list[7]
#     value_3 = value[7]
#
#     return name_list_left_1, name_list_right_1, name_1, value_1, name_list_left_2, name_list_right_2, \
#            name_2, value_2, name_list_left_3, name_list_right_3, name_3, value_3
#
# name_list_left_1, name_list_right_1, name_1, value_1, name_list_left_2, name_list_right_2, name_2, value_2, \
# name_list_left_3, name_list_right_3, name_3, value_3 = get_question(name_list_1)

# name_list_2 = [[1], [2], [3], [4], [5], [6], [7], [8]]
# name_list_3 = name_list_2[0:6]
# print(name_list_3)
# random.shuffle(name_list_3)
# name_list_3.append(name_list_2[6:8])
# print(name_list_3)

# print(name_list_left_1)
# print(name_list_left_2)
# print(name_list_left_3)
# print(name_list_right_1)
# print(name_list_right_2)
# print(name_list_right_3)
# print(name_1)
# print(name_2)
# print(name_3)
# print(value_1)
# print(value_2)
# print(value_3)

# path = "/Users/Nicole/Documents/oTree/covering_test/static/covering_test/test"  # insert the path to your directory
# collection = os.listdir(path)
#
# print('yes/'+collection[0])

mylist = [1, 2, 3, 4]
result = []
for i, g in enumerate(mylist):
    result.append(mylist[i])

print(result)