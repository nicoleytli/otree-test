
class player(object):
    score = 0


def compute(player):
    answer = ['Playful', 'Upset', 'ok', 'ok', 'ok', 'Fantasizing', 'Uneasy', 'ok']

    correction = ['Playful', 'Upset', 'Desire', 'Insisting', 'Worried', 'Fantasizing', 'Uneasy', 'Despondent']
    filtered = filter(lambda x: x[0] == x[1], zip(answer, correction))

    player.score = len(list(filtered))

    return player.score

p = []
for i in range(0, 3):
    p.append(player())

for i in range(0, 3):
    p[i].score = compute(p[i])

print(p[2].score)