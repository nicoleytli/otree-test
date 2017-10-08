import random

number_of_random = 30
# a list of random answers' location
random_loc = random.sample(list(range(36)), number_of_random)
# a list of drawn random answers
pics_loc = random_loc
random_loc = random.sample(random_loc, len(random_loc))

print(pics_loc)
print(random_loc)

final_list = list(range(36))

for i, j in zip(range(len(random_loc)), pics_loc):
    final_list[j] = random_loc[i]

order_list = list(range(36))
order_list = random.sample(order_list, len(order_list))

pic_final_list = list(range(36))
for i in range(len(pic_final_list)):
    pic_final_list[i] = final_list[order_list[i]]

print(order_list)
print(pic_final_list)