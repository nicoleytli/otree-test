mylist = ['1A', '1B', '2B']
herlist = []
for i in mylist:
    if i == '1A' or i == '1B':
        herlist.append('1')

names = locals()
print(names['mylist'])

group_matrix = []

players_1A = [1, 1, 1]
players_1B = [2, 2, 2]
players_2A = [3, 3, 3]
players_2B = [4, 4, 4]
players_3A = [5, 5, 5]
players_3B = [6, 6, 6]


for i in range(1, 4):
    while names['players_%sA' % i]:
        new_group = [
            names['players_%sA' % i].pop(),
            names['players_%sA' % i].pop(),
            names['players_%sA' % i].pop(),
            names['players_%sB' % i].pop(),
            names['players_%sB' % i].pop(),
            names['players_%sB' % i].pop(),
        ]
        group_matrix.append(new_group)

print(group_matrix)
