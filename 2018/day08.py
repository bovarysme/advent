class Node:
    def __init__(self):
        self.children = []
        self.metadata = []
        self.value = 0

    def __iter__(self):
        yield self

        for child in self.children:
            yield from child

    def add_child(self, node):
        self.children.append(node)

    def add_metadatum(self, metadatum):
        self.metadata.extend(metadatum)

    def update_value(self):
        if self.children:
            for index in self.metadata:
                index = index - 1
                if index < len(self.children):
                    self.value += self.children[index].value
        else:
            self.value = sum(self.metadata)


def build_tree2(parent, numbers, index):
    node = Node()
    parent.add_child(node)

    children = numbers[index]
    index += 1

    entries = numbers[index]
    index += 1

    for _ in range(children):
        index = build_tree2(node, numbers, index)

    node.add_metadatum(numbers[index:index+entries])
    index += entries

    node.update_value()

    return index


def build_tree(numbers):
    root = Node()
    build_tree2(root, numbers, 0)

    return root.children[0]


def solve(numbers):
    tree = build_tree(numbers)

    checksum = 0
    for node in tree:
        checksum += sum(node.metadata)

    return checksum, tree.value


def main():
    example = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    assert solve(example) == (138, 66)

    with open('inputs/day08.txt', 'r') as f:
        numbers = [int(n) for n in f.read().split()]

    print('Both parts:', *solve(numbers))


if __name__ == '__main__':
    main()
