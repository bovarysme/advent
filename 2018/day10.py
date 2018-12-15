class Point:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed


def display(points):
    width, height = 62, 10

    grid = [['.'] * width for _ in range(height)]
    for point in points:
        x, y = point.pos[0] - 126, point.pos[1] - 135
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = '#'

    for y in range(height):
        for x in range(width):
            print(grid[y][x], end='')
        print()
    print()


def part_one(points):
    # Correct number of iterations found empirically
    dt = 10009

    for point in points:
        point.pos[0] += dt * point.speed[0]
        point.pos[1] += dt * point.speed[1]

    display(points)


def main():
    points = []
    with open('inputs/day10.txt', 'r') as f:
        for line in f:
            pos = [int(val) for val in line[10:24].split(',')]
            speed = [int(val) for val in line[36:42].split(',')]
            point = Point(pos, speed)
            points.append(point)

    print('Part one:')
    part_one(points)

    print('Part two:', 10009)


if __name__ == '__main__':
    main()
