def val(value, factor):
    return (value * factor) % 2147483647


def val_a(value):
    return val(value, 16807)


def val_b(value):
    return val(value, 48271)


def match(a, b):
    return a & 0xffff == b & 0xffff


def generator(value, f, multiple):
    while True:
        value = f(value)
        if value & (multiple - 1) == 0:
            yield value


def part_one(a, b):
    matches = 0

    for i in range(40000000):
        a = val_a(a)
        b = val_b(b)

        if match(a, b):
            matches += 1

    return matches


def part_two(a, b):
    matches = 0

    ga = generator(a, val_a, 4)
    gb = generator(b, val_b, 8)

    for i in range(5000000):
        a = next(ga)
        b = next(gb)

        if match(a, b):
            matches += 1

    return matches


if __name__ == '__main__':
    example = (65, 8921)

    assert part_one(*example) == 588
    assert part_two(*example) == 309

    input_ = (591, 393)

    print('Answer for part one:', part_one(*input_))
    print('Answer for part two:', part_two(*input_))
