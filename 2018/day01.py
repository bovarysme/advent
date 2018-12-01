def part_one(freqs):
    return sum(freqs)


def part_two(freqs):
    result = 0
    running = True
    visited = set([0])

    while running:
        for freq in freqs:
            result += freq
            if result in visited:
                running = False
                break

            visited.add(result)

    return result


def main():
    assert part_one([1, -2, 3, 1]) == 3
    assert part_two([1, -1]) == 0
    assert part_two([3, 3, 4, -2, -4]) == 10

    with open('inputs/day01.txt') as f:
        freqs = f.readlines()
    freqs = list(map(int, freqs))

    print('Part one:', part_one(freqs))
    print('Part two:', part_two(freqs))


if __name__ == '__main__':
    main()
