def difference(line):
    mini, maxi = line[0], line[0]
    for value in line:
        if value < mini:
            mini = value

        if value > maxi:
            maxi = value

    return maxi - mini


def divisible(line):
    for i in range(len(line)-1):
        x = line[i]
        for y in line[i+1:]:
            if x % y == 0:
                return x // y

            if y % x == 0:
                return y // x


def solve(func, spreadsheet):
    checksum = 0
    for line in spreadsheet:
        checksum += func(line)

    return checksum


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
