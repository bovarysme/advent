def group(links, start):
    todo = set(links[start])
    visited = set([start])

    while todo:
        for elem in todo.copy():
            todo.remove(elem)
            visited.add(elem)

            todo |= set(links[elem]) - visited

    return visited


def part_one(links):
    group0 = group(links, 0)
    return len(group0)


def part_two(links):
    total = 0

    i = 0
    visited = set()

    while i < len(links):
        visited |= group(links, i)
        total += 1

        while i in visited:
            i += 1

    return total


if __name__ == '__main__':
    example = [
        [2],
        [1],
        [0, 3, 4],
        [2, 4],
        [2, 3, 6],
        [6],
        [4, 5],
    ]

    assert part_one(example) == 6
    assert part_two(example) == 2

    with open('inputs/day12.txt', 'r') as f:
        links = [
            [int(elem) for elem in line.rstrip().split(' <-> ')[1].split(', ')]
            for line in f
        ]

    print('Answer for part one:', part_one(links))
    print('Answer for part two:', part_two(links))
