from collections import defaultdict


class List:
    def __init__(self):
        node = Node(0, None, None)
        node.previous = node
        node.next = node

        self.head = node
        self.current = node

    def __iter__(self):
        yield self.head

        current = self.head.next
        while current is not self.head:
            yield current
            current = current.next

    def __str__(self):
        return '[{}]'.format(
            ', '.join(str(node.number) for node in self)
        )

    def add(self, number):
        node = Node(number, self.current.next, self.current.next.next)
        self.current.next.next.previous = node
        self.current.next.next = node
        self.current = node

    def remove(self):
        current = self.current
        for _ in range(7):
            current = current.previous

        current.previous.next = current.next
        current.next.previous = current.previous
        self.current = current.next

        return current.number


class Node:
    def __init__(self, number, previous, next_):
        self.number = number
        self.previous = previous
        self.next = next_


def solve(players, highest):
    scores = defaultdict(int)
    marbles = List()

    current = 0
    for number in range(1, highest+1):
        if number % 23 == 0:
            scores[current] += number + marbles.remove()
        else:
            marbles.add(number)

        current = (current + 1) % players

    return max(scores.values())


def main():
    examples = {
        (10, 1618): 8317,
        (13, 7999): 146373,
        (17, 1104): 2764,
        (21, 6111): 54718,
        (30, 5807): 37305,
    }

    for k, v in examples.items():
        assert solve(*k) == v

    players, highest = 452, 71250
    print('Part one:', solve(players, highest))
    print('Part two:', solve(players, highest*100))


if __name__ == '__main__':
    main()
