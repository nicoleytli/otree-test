import random

class Player:
    def __init__(self, i):
        self.id = i

    option1 = 3
    option2 = 2
    option3 = 1
    option4 = 0
    decision = '♡'
    option_temp = [option1, option2, option3, option4]
    option = option_temp.index(max(option_temp))

p = []
for i in range(0, 4):
    p.append(Player(i))

class Group:

    coin = random.choice(['head', 'tail'])

    def set_payoffs(self):

        for player in p:
            result1 = []
            result2 = []
            if player.option == 3 or player.option == 2:
                for i in p:
                    if i.id != player.id:
                        if player.decision == '♡':
                            result1.extend([player.decision])
                        else:
                            result2.extend([player.decision])
                    else:
                        continue
                if len(result1) > len(result2):
                    player.yourresult = bool(player.option == 0)
                else:
                    player.yourresult = bool(player.option == 1)
            else:
                if Group.coin == 'head':
                    player.yourresult = bool(player.option == 0)
                else:
                    player.yourresult = bool(player.option == 1)
            player.payoff = player.yourresult * 4
            print(len(result1))
            print(len(result2))
            print(Group.coin)



g = Group.set_payoffs('head')

print(p[0].payoff)
print(p[1].payoff)
print(p[2].payoff)
print(p[3].payoff)
print(Group.coin)

# p = random.randint(0, 2)
#
#
# if p == 0 or p == 1:
#     coin = 'head'
# else:
#     coin = 'tail'
#
# print(coin)
# print(p)