def solve(rule, offsets):
    jumps = 0
    ptr = 0

    while ptr >= 0 and ptr < len(offsets):
        offset = offsets[ptr]
        offsets[ptr] = rule(offsets[ptr])
        ptr += offset

        jumps += 1

    return jumps


def part_one(offsets):
    return solve(lambda x: x+1, offsets)


def part_two(offsets):
    return solve(lambda x: x-1 if x >= 3 else x+1, offsets)


if __name__ == '__main__':
    assert part_one([0, 3, 0, 1, -3]) == 5

    assert part_two([0, 3, 0, 1, -3]) == 10

    with open('inputs/day5.txt', 'r') as f:
        offsets = [int(offset.rstrip()) for offset in f]

    print('Answer for part one:', part_one(offsets[:]))
    print('Answer for part two:', part_two(offsets[:]))
