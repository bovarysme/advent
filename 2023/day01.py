import string
import itertools


def numbers(values):
    for value in values:
        number = 0
        for char in value:
            if char.isdecimal():
                number += int(char) * 10
                break
        for char in reversed(value):
            if char.isdecimal():
                number += int(char)
                break
        yield number


def part_one(values):
    return sum(numbers(values))


def lfind(sub, value):
    index = value.find(sub)
    return index if index > -1 else len(value)


def numbers2(values):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    translations = list(
        itertools.chain(enumerate(string.digits[1:], 1), enumerate(words, 1))
    )
    for value in values:
        first_translation = min(translations, key=lambda t: lfind(t[1], value))
        last_translation = max(translations, key=lambda t: value.rfind(t[1]))
        yield first_translation[0] * 10 + last_translation[0]


def part_two(values):
    return sum(numbers2(values))


def main():
    assert part_one(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142
    assert (
        part_two(
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )
        == 281
    )

    with open("inputs/day01.txt") as f:
        values = list(f)

    print("Part one:", part_one(values))
    print("Part two:", part_two(values))


if __name__ == "__main__":
    main()
