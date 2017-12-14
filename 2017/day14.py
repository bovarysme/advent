from day10 import part_two


def bits(value):
    for i in reversed(range(128)):
        yield value >> i & 1


def print_grid(grid):
    for row in grid:
        for square in row:
            if square:
                print('#', end='')
            else:
                print('.', end='')
        print()


def neighbors(grid, coords):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = coords[0] + dx, coords[1] + dy
        if 0 <= x < 128 and 0 <= y < 128 and grid[y][x]:
            yield x, y


def clear_region(grid, x, y):
    todo = set([(x, y)])
    visited = set()

    while todo:
        coords = todo.pop()
        visited.add(coords)

        todo |= set(neighbors(grid, coords)) - visited

    for x, y in visited:
        grid[y][x] = 0


def solve(base):
    squares = 0

    grid = []
    regions = 0

    print('Generating the grid...')

    for row in range(128):
        digest = part_two('{}-{}'.format(base, row))
        value = int(digest, 16)

        line = list(bits(value))
        squares += sum(line)

        grid.append(line)

    print('Counting regions...')

    for x in range(128):
        for y in range(128):
            if grid[y][x]:
                clear_region(grid, x, y)
                regions += 1

    return squares, regions


if __name__ == '__main__':
    assert solve('flqrgnkx') == (8108, 1242)

    print('Answers for both parts:', *solve('ffayrhll'))
