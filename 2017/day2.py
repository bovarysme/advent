def difference(line):
    mini, maxi = line[0], line[0]
    for value in line[1:]:
        if value < mini:
            mini = value

        if value > maxi:
            maxi = value

    return maxi - mini


def couples(line):
    for i, x in enumerate(line):
        for y in line[i+1:]:
            yield x, y
            yield y, x


def divisible(line):
    for x, y in couples(line):
        q, r = divmod(x, y)
        if r == 0:
            return q


def solve(func, spreadsheet):
    return sum(func(line) for line in spreadsheet)


def part_one(spreadsheet):
    return solve(difference, spreadsheet)


def part_two(spreadsheet):
    return solve(divisible, spreadsheet)


if __name__ == '__main__':
    assert part_one([
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8],
    ]) == 18

    assert part_two([
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5],
    ]) == 9

    with open('inputs/day2.txt', 'r') as f:
        spreadsheet = [
            [int(value) for value in line.rstrip().split()]
            for line in f.readlines()
        ]

    print('Answer for part one:', part_one(spreadsheet))
    print('Answer for part two:', part_two(spreadsheet))
