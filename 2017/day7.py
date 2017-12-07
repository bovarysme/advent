class Node(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

        self.parent = None
        self.subweight = 0


def parse(line):
    line = line.rstrip()

    parts = line.split(' -> ')

    name, weight = parts[0].split()
    weight = int(weight[1:-1])

    children = []
    if len(parts) >= 2:
        children = parts[1].split(', ')

    return Node(name, weight, children)


def subweight(nodes, name):
    sw = 0
    for child in nodes[name].children:
        sw += subweight(nodes, child)

    nodes[name].subweight = sw

    return nodes[name].weight + sw


def part_one(nodes):
    key = list(nodes)[0]
    node = nodes[key]
    while node.parent:
        node = nodes[node.parent]

    return node.name


def part_two(nodes, root):
    subweight(nodes, root)

    # LOOK MOM, NO COMPUTERS!!
    root = 'cwwwj'  # 'boropxd' <- 'qjvtm' <- root

    current = nodes[root]
    totals = {}
    for child in current.children:
        total = nodes[child].subweight + nodes[child].weight
        totals[child] = total

    #print(totals)

    return nodes[root].weight - 8


if __name__ == '__main__':
    nodes = {}
    with open('inputs/day7.txt', 'r') as f:
        for line in f.readlines():
            node = parse(line)
            nodes[node.name] = node

    for node in nodes.values():
        for child in node.children:
            nodes[child].parent = node.name

    root = part_one(nodes)
    print('Answer for part one:', root)
    print('Answer for part two:', part_two(nodes, root))
