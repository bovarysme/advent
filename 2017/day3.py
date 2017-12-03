def ulam_position(value):
    # TODO
    return (0, 0)


def solve(value):
    pos = ulam_position(value)
    return abs(pos[0]) + abs(pos[1])


if __name__ == '__main__':
    assert solve(1) == 0
    assert solve(12) == 3
    assert solve(23) == 2
    assert solve(1024) == 31

    print('Answer for part one:', solve(277678))
