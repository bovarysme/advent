from collections import Counter
from itertools import combinations


def part_one(words):
    two = 0
    three = 0
    for word in words:
        counter = Counter(word)

        occurences = set(elem[1] for elem in counter.most_common())
        if 2 in occurences:
            two += 1
        if 3 in occurences:
            three += 1

    return two * three


def distance(words):
    return sum(elem[0] != elem[1] for elem in zip(*words))


def part_two(words):
    correct = min(combinations(words, 2), key=distance)
    return ''.join(elem[0] for elem in zip(*correct) if elem[0] == elem[1])


def main():
    example = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    assert part_one(example) == 12

    example = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    assert part_two(example) == 'fgij'

    with open('inputs/day02.txt') as f:
        words = [word.rstrip() for word in f]

    print('Part one:', part_one(words))
    print('Part two:', part_two(words))


if __name__ == '__main__':
    main()
