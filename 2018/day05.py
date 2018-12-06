import string


def opposites(a, b):
    return ord(a) ^ ord(b) == 32


def react(polymer, ignore=None):
    stack = []
    for unit in polymer:
        if unit.lower() == ignore:
            continue

        if len(stack) > 0 and opposites(unit, stack[-1]):
            stack.pop()
        else:
            stack.append(unit)

    return len(stack)


def part_one(polymer):
    return react(polymer)


def part_two(polymer):
    return min(react(polymer, c) for c in string.ascii_lowercase)


def main():
    example = 'dabAcCaCBAcCcaDA'
    assert part_one(example) == 10
    assert part_two(example) == 4

    with open('inputs/day05.txt', 'r') as f:
        polymer = f.read().rstrip()

    print('Part one:', part_one(polymer))
    print('Part two:', part_two(polymer))


if __name__ == '__main__':
    main()
