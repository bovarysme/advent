import string


def solve(moves, size=16):
    group = list(string.ascii_lowercase[:size])

    for move in moves:
        if move[0] == 's':
            size = int(move[1:])
            group = group[-size:] + group[:-size]
        elif move[0] == 'x':
            i, j = map(int, move[1:].split('/'))
            group[i], group[j] = group[j], group[i]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            i, j = group.index(a), group.index(b)
            group[i], group[j] = group[j], group[i]

    return ''.join(group)


if __name__ == '__main__':
    example = ['s1', 'x3/4', 'pe/b']

    assert solve(example, 5) == 'baedc'

    with open('inputs/day16.txt', 'r') as f:
        moves = f.read().rstrip().split(',')

    print('Answer for part one:', solve(moves))
