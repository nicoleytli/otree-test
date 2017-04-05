

my_list = ['E1', 'E3', 'P1']
p = []
for i in my_list:
    p.append(bool(i == 'E1' or i == 'P1'))

print(p)

