from collections import defaultdict
from math import sqrt


def part_one(instructions):
    regs = defaultdict(int)
    regs['1'] = 1
    ptr = 0

    count = 0

    while ptr >= 0 and ptr < len(instructions):
        op, reg, val = instructions[ptr].split()
        if val.isalpha():
            val = regs[val]
        else:
            val = int(val)

        if op == 'set':
            regs[reg] = val
        elif op == 'sub':
            regs[reg] -= val
        elif op == 'mul':
            regs[reg] *= val
            count += 1
        elif op == 'jnz' and regs[reg] != 0:
            ptr += val
            continue

        ptr += 1

    return count


def part_two():
    count = 0

    for number in range(107900, 124901, 17):
        sup = int(sqrt(number))
        for divisor in range(2, sup):
            if number % divisor == 0:
                count += 1
                break

    return count


if __name__ == '__main__':
    with open('inputs/day23.txt', 'r') as f:
        instructions = [line.rstrip() for line in f]

    print('Answer for part one:', part_one(instructions))
    print('Answer for part two:', part_two())
