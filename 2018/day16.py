import operator
from collections import defaultdict


def reg(operands, op, regs):
    """R/R instructions."""
    a, b, c = operands
    regs[c] = int(op(regs[a], regs[b]))


def imm(operands, op, regs):
    """R/I instructions."""
    a, b, c = operands
    regs[c] = int(op(regs[a], b))


def immr(operands, op, regs):
    """I/R instructions."""
    a, b, c = operands
    regs[c] = int(op(a, regs[b]))


def setr(operands, op, regs):
    a, b, c = operands
    regs[c] = regs[a]


def seti(operands, op, regs):
    a, b, c = operands
    regs[c] = a


instructions = {
    'addr': (reg, operator.add),
    'addi': (imm, operator.add),
    'mulr': (reg, operator.mul),
    'muli': (imm, operator.mul),
    'banr': (reg, operator.and_),
    'bani': (imm, operator.and_),
    'borr': (reg, operator.or_),
    'bori': (imm, operator.or_),
    'gtir': (immr, operator.gt),
    'gtri': (imm, operator.gt),
    'gtrr': (reg, operator.gt),
    'eqir': (immr, operator.eq),
    'eqri': (imm, operator.eq),
    'eqrr': (reg, operator.eq),
    'setr': (setr, None),
    'seti': (seti, None),
}


def execute(instruction, regs, doc=None, name=None):
    opcode, operands = instruction[0], instruction[1:]

    if doc is not None:
        name = doc[opcode]

    func, op = instructions[name]
    func(operands, op, regs)


def part_one(samples, decode=False):
    doc = defaultdict(set)

    score = 0
    for sample in samples:
        regs, instruction, expected = sample

        matches = 0
        for name in instructions:
            copy = regs[:]
            execute(instruction, copy, name=name)

            if copy == expected:
                opcode = instruction[0]
                doc[opcode].add(name)
                matches += 1

        if matches >= 3:
            score += 1

    if decode:
        while not all(len(names) == 1 for names in doc.values()):
            for opcode, names in doc.items():
                if len(names) == 1:
                    for opcode2 in doc:
                        if opcode != opcode2:
                            doc[opcode2] -= names

        for opcode, names in doc.items():
            doc[opcode] = names.pop()

    return score, doc


def part_two(program, doc):
    regs = [0, 0, 0, 0]
    for instruction in program:
        execute(instruction, regs, doc=doc)

    return regs[0]


def parse_line(line):
    return [int(val) for val in line[9:19].split(',')]


def parse_sample(sample):
    lines = sample.split('\n')

    before = parse_line(lines[0])
    opcode = [int(val) for val in lines[1].split()]
    after = parse_line(lines[2])

    return before, opcode, after


def main():
    example = [(
        [3, 2, 1, 1],
        [9, 2, 1, 2],
        [3, 2, 2, 1],
    )]
    assert part_one(example)[0] == 1

    with open('inputs/day16.txt', 'r') as f:
        samples, program = f.read().rstrip().split('\n\n\n\n')
        samples = [parse_sample(sample) for sample in samples.split('\n\n')]
        program = [
            [int(val) for val in line.split()]
            for line in program.split('\n')
        ]

    score, doc = part_one(samples, decode=True)
    print('Part one:', score)
    print('Part two:', part_two(program, doc))


if __name__ == '__main__':
    main()
