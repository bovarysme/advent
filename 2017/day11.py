def distance(x, y):
    return (abs(x) + abs(x + y) + abs(y)) // 2


def solve(path):
    moves = {
        'n': (0, -1),
        'ne': (1, -1),
        'se': (1, 0),
        's': (0, 1),
        'sw': (-1, 1),
        'nw': (-1, 0),
    }

    x, y = 0, 0
    maxi = 0

    for step in path:
        move = moves[step]
        x += move[0]
        y += move[1]

        dist = distance(x, y)
        if dist > maxi:
            maxi = dist

    return distance(x, y), maxi


if __name__ == '__main__':
    tests = {
        ('ne', 'ne', 'ne'): (3, 3),
        ('ne', 'ne', 'sw', 'sw'): (0, 2),
        ('ne', 'ne', 's', 's'): (2, 2),
        ('se', 'sw', 'se', 'sw', 'sw'): (3, 3),
    }

    for k, v in tests.items():
        assert solve(k) == v

    with open('inputs/day11.txt') as f:
        path = f.read().rstrip().split(',')

    print('Answers for both parts:', *solve(path))
