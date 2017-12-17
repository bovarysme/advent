def part_one(step):
    buf = [0]
    ptr = 0

    for i in range(1, 2018):
        ptr = (ptr + step) % len(buf) + 1
        buf.insert(ptr, i)

    return buf[(ptr + 1) % len(buf)]


def part_two(step):
    ptr = 0
    val = 0

    for length in range(1, 50000001):
        ptr = (ptr + step) % length + 1
        if ptr == 1:
            val = length

    return val


if __name__ == '__main__':
    assert part_one(3) == 638

    print('Answer for part one:', part_one(370))
    print('Answer for part two:', part_two(370))
