import operator
from collections import defaultdict


def solve(instructions):
    opcodes = {
        'inc': operator.add,
        'dec': operator.sub,

        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>': operator.gt,
    }

    registers = defaultdict(int)

    maxi = 0
    for instruction in instructions:
        reg, op, val, _, c_reg, c_op, c_val = instruction.split()
        val, c_val = int(val), int(c_val)

        if opcodes[c_op](registers[c_reg], c_val):
            registers[reg] = opcodes[op](registers[reg], val)
            if registers[reg] > maxi:
                maxi = registers[reg]

    return max(registers.values()), maxi


if __name__ == '__main__':
    assert solve([
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10',
    ]) == (1, 10)

    with open('inputs/day8.txt', 'r') as f:
        instructions = [line.rstrip() for line in f]

    print('Answers for both parts:', *solve(instructions))
