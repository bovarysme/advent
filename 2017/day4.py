def duplicates(passphrase):
    words = set()
    for word in passphrase.split():
        if word in words:
            return False

        words.add(word)

    return True


def anagrams(passphrase):
    words = set()
    for word in passphrase.split():
        word = ''.join(sorted(word))
        if word in words:
            return False

        words.add(word)

    return True


def solve(validator, passphrases):
    return sum(validator(passphrase) for passphrase in passphrases)


def part_one(passphrases):
    return solve(duplicates, passphrases)


def part_two(passphrases):
    return solve(anagrams, passphrases)


if __name__ == '__main__':
    assert part_one(['aa bb cc dd ee']) == 1
    assert part_one(['aa bb cc dd aa']) == 0
    assert part_one(['aa bb cc dd aaa']) == 1

    assert part_two(['abcde fghij']) == 1
    assert part_two(['abcde xyz ecdab']) == 0
    assert part_two(['a ab abc abd abf abj']) == 1
    assert part_two(['iiii oiii ooii oooi oooo']) == 1
    assert part_two(['oiii ioii iioi iiio']) == 0

    with open('inputs/day4.txt', 'r') as f:
        passphrases = [line.rstrip() for line in f.readlines()]

    print('Answer for part one:', part_one(passphrases))
    print('Answer for part two:', part_two(passphrases))
