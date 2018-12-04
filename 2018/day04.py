from collections import defaultdict, namedtuple
from datetime import datetime

Record = namedtuple('Record', ['datetime', 'message'])


class Nap:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def duration(self):
        delta = self.end - self.start
        return delta.seconds // 60


def part_one(log):
    sleepyboi = max(log.items(), key=lambda e: sum(nap.duration() for nap in e[1]))
    number, naps = sleepyboi

    table = [0] * 60
    for nap in naps:
        for minute in range(nap.start.minute, nap.end.minute):
            table[minute] += 1

    minute = table.index(max(table))

    return number * minute


def part_two(log):
    tables = defaultdict(lambda: [0] * 60)
    for number, naps in log.items():
        for nap in naps:
            for minute in range(nap.start.minute, nap.end.minute):
                tables[number][minute] += 1

    sleepyboi = max(tables.items(), key=lambda e: max(e[1]))
    number, table = sleepyboi

    minute = table.index(max(table))

    return number * minute


def build_log(records):
    log = defaultdict(list)

    number, start, end = None, None, None
    for record in records:
        words = record.message.split()

        command = words[0].lower()
        if command == 'guard':
            number = int(words[1].lstrip('#'))
        elif command == 'falls':
            start = record.datetime
        elif command == 'wakes':
            end = record.datetime
            nap = Nap(start, end)
            log[number].append(nap)

    return log


def parse_record(line):
    line = line.rstrip()
    record = line.split(maxsplit=2)

    timestamp = ' '.join(record[:2])
    dt = datetime.strptime(timestamp, '[%Y-%m-%d %H:%M]')

    message = record[2]

    return Record(dt, message)


def main():
    with open('inputs/day04.txt', 'r') as f:
        records = [parse_record(line) for line in f]
    records.sort()

    log = build_log(records)

    print('Part one:', part_one(log))
    print('Part two:', part_two(log))


if __name__ == '__main__':
    main()
