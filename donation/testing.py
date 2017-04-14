import random


# if len(clot) == 0:
#     if len(cmiddle) == 0 and len(clittle) != 0:
#         temp1 = random.choice(clittle)
#         temp2 = temp1
#         temp3 = temp1
#     elif len(cmiddle) != 0 and len(clittle) == 0:
#         temp1 = random.choice(cmiddle)
#         temp2 = temp1
#         temp3 = temp1
#     elif len(cmiddle) != 0 and len(clittle) != 0:
#         temp1 = random.choice(cmiddle)
#         temp2 = random.choice(clittle)
#         temp3 = random.choice(cmiddle + clittle)
#     else:
#         pass
# else:
#     if len(cmiddle) == 0 and len(clittle) != 0:
#         temp1 = random.choice(clot)
#         temp2 = random.choice(clittle)
#         temp3 = random.choice(clot + clittle)
#     elif len(cmiddle) != 0 and len(clittle) == 0:
#         temp1 = random.choice(clot)
#         temp2 = random.choice(cmiddle)
#         temp3 = random.choice(clot + cmiddle)
#     elif len(cmiddle) != 0 and len(clittle) != 0:
#         temp1 = random.choice(clot)
#         temp2 = random.choice(clittle)
#         temp3 = random.choice(clot + clittle)
#     else:
#         pass
# #
# print(temp1)
# print(temp2)
# print(temp3)

# clittle.append([4, 4])
# clittle.append([5, 5])
# print(clittle)
# print(len(clittle))
# print(random.choice(clittle))

# temp = []
# temp1 = [[5, 5]]
# if len(clot) == 0:
#     if len(cmiddle) == 0 and len(clittle) != 0:
#         if len(clittle) <= 3:
#             temp = random.sample(clittle, len(clittle))
#         else:
#             temp = random.sample(clittle, 3)
#     elif len(cmiddle) != 0 and len(clittle) == 0:
#         if len(cmiddle) <= 3:
#             temp = random.sample(cmiddle, len(cmiddle))
#         else:
#             temp = random.sample(cmiddle, 3)
#     elif len(cmiddle) != 0 and len(clittle) != 0:
#         temp += random.sample(cmiddle, 1)
#         temp += random.sample(clittle, 1)
#         temp1 = [i for i in cmiddle if i not in temp]
#         temp2 = [i for i in clittle if i not in temp]
#         temp += random.sample(temp1 + temp2, 1)
#     else:
#         biglist = [['test', 1], ['test', 2], ['test', 3], ['test', 4], ['test', 5]]
#         temp = random.sample(biglist, 3)
# else:
#     if len(cmiddle) == 0 and len(clittle) != 0:
#         temp += random.sample(clot, 1)
#         temp += random.sample(clittle, 1)
#         temp1 = [i for i in clot if i not in temp]
#         temp2 = [i for i in clittle if i not in temp]
#         temp += random.sample(temp1 + temp2, 1)
#     elif len(cmiddle) != 0 and len(clittle) == 0:
#         temp += random.sample(clot, 1)
#         temp += random.sample(cmiddle, 1)
#         temp1 = [i for i in cmiddle if i not in temp]
#         temp2 = [i for i in clot if i not in temp]
#         temp += random.sample(temp1 + temp2, 1)
#     elif len(cmiddle) != 0 and len(clittle) != 0:
#         temp += random.sample(clot, 1)
#         temp += random.sample(clittle, 1)
#         temp1 = [i for i in clittle if i not in temp]
#         temp2 = [i for i in clot if i not in temp]
#         temp += random.sample(temp1 + temp2, 1)
#     else:
#         if len(clot) <= 3:
#             temp = random.sample(clot, len(clot))
#         else:
#             temp = random.sample(clot, 3)
#
# print(temp)
# print(temp[1][1])

list_question = [[1, 'Reduce the difference in income'], [2, 'limit imports'], [3, 'Send troops to fight ISIS'],
                 [4, 'Protect gays and lesbians against job discrimination'], [5, 'The death penalty for murder'],
                 [6, 'Change access to citizenship for children of illegal immigrants'],
                 [7, 'Build a wall on the US-Mexico border'],
                 [8, 'Paid leave for parents of new children'],
                 [9, 'Increase number of black students at universities'],
                 [10, 'Pay women and men the same amount for the same work']]

random.shuffle(list_question)
print(list_question)