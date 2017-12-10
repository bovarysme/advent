import operator
from functools import reduce


class KnotHash(object):
    def __init__(self, lengths, n=256):
        self.lengths = lengths
        self.n = n

        self.list = list(range(n))
        self.ptr = 0
        self.skip = 0

    def hash(self):
        for length in self.lengths:
            for i in range(length//2):
                begin = (self.ptr + i) % self.n
                end = (self.ptr + (length - 1) - i) % self.n
                self.list[begin], self.list[end] = self.list[end], self.list[begin]

            self.ptr = (self.ptr + length + self.skip) % self.n
            self.skip += 1

    def digest(self):
        numbers = [reduce(operator.xor, self.list[i:i+16]) for i in range(0, self.n, 16)]

        return ''.join([format(number, '02x') for number in numbers])


def part_one(lengths, n=256):
    knot = KnotHash(lengths, n)
    knot.hash()

    return knot.list[0] * knot.list[1]


def part_two(data):
    lengths = [ord(char) for char in data] + [17, 31, 73, 47, 23]
    knot = KnotHash(lengths)

    for _ in range(64):
        knot.hash()

    return knot.digest()


if __name__ == '__main__':
    assert part_one([3, 4, 1, 5], 5) == 12

    assert part_two('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert part_two('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert part_two('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert part_two('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

    with open('inputs/day10.txt', 'r') as f:
        data = f.read().rstrip()

    lengths = [int(length) for length in data.split(',')]

    print('Answer for part one:', part_one(lengths))
    print('Answer for part two:', part_two(data))
