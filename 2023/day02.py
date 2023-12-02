import functools
import operator

from collections import defaultdict


def parse(games):
    for game in games:
        cubes = []
        header, body = game.split(":")

        sets = body.split(";")
        for s in sets:
            elems = s.split(",")
            for elem in elems:
                num, color = elem.split()
                cubes.append((int(num), color))

        ident = int(header.split()[1])
        yield ident, cubes


def score(ident, cubes):
    limits = {"red": 12, "green": 13, "blue": 14}
    return ident if all(num <= limits[color] for num, color in cubes) else 0


def part_one(games):
    return sum(score(ident, cubes) for ident, cubes in parse(games))


def power(cubes):
    maxes = defaultdict(int)
    for num, color in cubes:
        if num > maxes[color]:
            maxes[color] = num

    return functools.reduce(operator.mul, maxes.values(), 1)


def part_two(games):
    return sum(power(cubes) for _, cubes in parse(games))


def main():
    with open("inputs/day02.txt") as f:
        games = list(f)

    # Testing is doubting.
    print("Part one:", part_one(games))
    print("Part two:", part_two(games))


if __name__ == "__main__":
    main()
