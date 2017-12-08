from enum import Enum


class Direction(Enum):
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4


def update(direction, limit):
    if direction == Direction.RIGHT:
        direction = Direction.UP
    elif direction == Direction.UP:
        direction = Direction.LEFT
        limit += 1
    elif direction == Direction.LEFT:
        direction = Direction.DOWN
    else:
        direction = Direction.RIGHT
        limit += 1

    return direction, limit


def positions(value):
    direction = Direction.RIGHT
    pos = [0, 0]

    limit = 1
    traveled = 0

    for _ in range(1, value):
        if direction == Direction.RIGHT:
            pos[0] += 1
        elif direction == Direction.UP:
            pos[1] += 1
        elif direction == Direction.LEFT:
            pos[0] -= 1
        else:
            pos[1] -= 1

        yield pos[0], pos[1]

        traveled += 1
        if traveled >= limit:
            direction, limit = update(direction, limit)
            traveled = 0


def neighbors(pos):
    for x in range(pos[0]-1, pos[0]+2):
        for y in range(pos[1]-1, pos[1]+2):
            if (x, y) == pos:
                continue

            yield x, y


def part_one(value):
    pos = (0, 0)
    for pos in positions(value):
        pass

    return abs(pos[0]) + abs(pos[1])


def part_two(value):
    values = {
        (0, 0): 1
    }

    # Ensure there are enough iterations
    iterator = positions((value + 1) * 2)

    while True:
        pos = next(iterator)

        total = 0
        for neighbor in neighbors(pos):
            if neighbor in values:
                total += values[neighbor]

        if total > value:
            return total

        values[pos] = total


if __name__ == '__main__':
    assert part_one(1) == 0
    assert part_one(12) == 3
    assert part_one(23) == 2
    assert part_one(1024) == 31

    assert part_two(1) == 2
    assert part_two(10) == 11
    assert part_two(20) == 23
    assert part_two(30) == 54
    assert part_two(100) == 122
    assert part_two(300) == 304
    assert part_two(400) == 747
    assert part_two(800) == 806

    print('Answer for part one:', part_one(277678))
    print('Answer for part two:', part_two(277678))
