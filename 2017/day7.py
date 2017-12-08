from collections import defaultdict


class Node(object):
    def __init__(self, weight, children):
        self.weight = weight
        self.children = children

        self.subweight = 0


def parse(lines):
    nodes = {}
    for line in lines:
        parts = line.split(' -> ')

        name, weight = parts[0].split()
        weight = int(weight[1:-1])

        children = set()
        if len(parts) >= 2:
            children = set(parts[1].split(', '))

        nodes[name] = Node(weight, children)

    return nodes


def find_root(nodes):
    roots = set(nodes)
    for node in nodes.values():
        roots -= node.children

    assert len(roots) == 1

    return list(roots)[0]


def compute_weights(nodes, name):
    current = nodes[name]
    current.subweight = sum(compute_weights(nodes, child) for child in current.children)

    return current.weight + current.subweight


def find_unbalanced(nodes, name):
    weights = defaultdict(list)
    for child in nodes[name].children:
        weight = nodes[child].weight + nodes[child].subweight
        weights[weight].append(child)

    if len(weights) == 1:
        return None
    else:
        faulty = [v[0] for v in weights.values() if len(v) == 1][0]

        result = find_unbalanced(nodes, faulty)
        if result is None:
            keys = list(weights)
            diff = abs(keys[0] - keys[1])

            return nodes[faulty].weight - diff
        else:
            return result


def part_one(nodes):
    return find_root(nodes)


def part_two(nodes):
    root = find_root(nodes)
    compute_weights(nodes, root)

    return find_unbalanced(nodes, root)


if __name__ == '__main__':
    nodes = parse([
        'pbga (66)',
        'xhth (57)',
        'ebii (61)',
        'havc (66)',
        'ktlj (57)',
        'fwft (72) -> ktlj, cntj, xhth',
        'qoyq (66)',
        'padx (45) -> pbga, havc, qoyq',
        'tknk (41) -> ugml, padx, fwft',
        'jptl (61)',
        'ugml (68) -> gyxo, ebii, jptl',
        'gyxo (61)',
        'cntj (57)',
    ])

    assert part_one(nodes) == 'tknk'
    assert part_two(nodes) == 60

    with open('inputs/day7.txt', 'r') as f:
        nodes = parse([line.rstrip() for line in f])

    print('Answer for part one:', part_one(nodes))
    print('Answer for part two:', part_two(nodes))
