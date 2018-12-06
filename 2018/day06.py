from collections import defaultdict


def bounds(points):
    x = (min(p[0] for p in points), max(p[0] for p in points))
    y = (min(p[1] for p in points), max(p[1] for p in points))

    return x, y


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def closest(points, key):
    dupes = False

    candidate = None
    value = float('inf')

    for point in points:
        result = key(point)
        if result < value:
            dupes = False

            candidate = point
            value = result
        elif result == value:
            dupes = True

    return None if dupes else candidate


def part_one(points):
    scores = defaultdict(int)

    xbounds, ybounds = bounds(points)
    for y in range(*ybounds):
        for x in range(*xbounds):
            point = closest(points, lambda p: distance((x, y), p))
            if point is not None:
                scores[point] += 1

    # XXX: ignore infinite areas
    return max(scores.values())


def part_two(points):
    size = 0

    xbounds, ybounds = bounds(points)
    for y in range(*ybounds):
        for x in range(*xbounds):
            total = sum(distance((x, y), p) for p in points)
            if total < 10000:
                size += 1

    return size


def main():
    with open('inputs/day06.txt', 'r') as f:
        points = [tuple(map(int, line.split(','))) for line in f]

    print('Part one:', part_one(points))
    print('Part two:', part_two(points))


if __name__ == '__main__':
    main()
