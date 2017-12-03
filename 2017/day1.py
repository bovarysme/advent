def iter_pairs(digits):
    for i in range(len(digits) - 1):
        yield digits[i], digits[i+1]

    yield digits[-1], digits[0]


def iter_halfway(digits):
    half = len(digits) // 2
    for i in range(half):
        yield digits[i], digits[half+i]

    for i in range(half, len(digits)):
        yield digits[i], digits[i-half]


def solve(iterator, digits):
    captcha = 0
    for x, y in iterator(digits):
        if x == y:
            captcha += int(x)

    return captcha


def part_one(digits):
    return solve(iter_pairs, digits)


def part_two(digits):
    return solve(iter_halfway, digits)


if __name__ == '__main__':
    assert part_one('1122') == 3
    assert part_one('1111') == 4
    assert part_one('1234') == 0
    assert part_one('91212129') == 9

    assert part_two('1212') == 6
    assert part_two('1221') == 0
    assert part_two('123425') == 4
    assert part_two('123123') == 12
    assert part_two('12131415') == 4

    with open('inputs/day1.txt', 'r') as f:
        digits = f.read().rstrip()

    print('Answer for part one:', part_one(digits))
    print('Answer for part two:', part_two(digits))
