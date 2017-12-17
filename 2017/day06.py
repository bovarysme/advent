def redistribute(blocks):
    """Redistribute the blocks in-place."""
    ptr = 0
    maxi = blocks[0]

    for i, value in enumerate(blocks[1:], 1):
        if value > maxi:
            ptr = i
            maxi = value

    value = blocks[ptr]
    blocks[ptr] = 0

    while value > 0:
        ptr = (ptr + 1) % len(blocks)
        blocks[ptr] += 1
        value -= 1


def solve(blocks):
    configs = {
        tuple(blocks): 0,
    }
    steps = 0

    while True:
        redistribute(blocks)
        steps += 1

        key = tuple(blocks)
        if key in configs:
            return steps, steps - configs[key]

        configs[key] = steps


if __name__ == '__main__':
    assert solve([0, 2, 7, 0]) == (5, 4)

    with open('inputs/day6.txt', 'r') as f:
        blocks = [int(block) for block in f.read().rstrip().split()]

    print('Answers for both parts:', *solve(blocks[:]))
