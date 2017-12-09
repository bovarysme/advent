def solve(stream):
    chars = 0
    score = 0
    level = 1

    garbage = False
    skip = False

    for char in stream:
        if garbage:
            if skip:
                skip = False
            elif char == '>':
                garbage = False
            elif char == '!':
                skip = True
            else:
                chars += 1
        else:
            if char == '<':
                garbage = True
            if char == '{':
                score += level
                level += 1
            elif char == '}':
                level -= 1

    return score, chars


if __name__ == '__main__':
    tests = {
        '{}': (1, 0),
        '{{{}}}': (6, 0),
        '{{},{}}': (5, 0),
        '{{{},{},{{}}}}': (16, 0),
        '{<a>,<a>,<a>,<a>}': (1, 4),
        '{{<ab>},{<ab>},{<ab>},{<ab>}}': (9, 8),
        '{{<!!>},{<!!>},{<!!>},{<!!>}}': (9, 0),
        '{{<a!>},{<a!>},{<a!>},{<ab>}}': (3, 17),

        '<>': (0, 0),
        '<random characters>': (0, 17),
        '<<<<>': (0, 3),
        '<{!>}>': (0, 2),
        '<!!>': (0, 0),
        '<!!!>>': (0, 0),
        '<{o"i!a,<{i<a>': (0, 10),
    }

    for k, v in tests.items():
        assert solve(k) == v

    with open('inputs/day9.txt', 'r') as f:
        stream = f.read().rstrip()

    print('Answers for both parts:', *solve(stream))
