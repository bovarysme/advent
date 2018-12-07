class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.parents = set()

    def add_edge(self, node):
        self.edges.append(node)
        node.add_parent(self)

    def add_parent(self, parent):
        self.parents.add(parent)


def build_graph(edges):
    graph = {}
    for p, q in edges:
        if p not in graph:
            graph[p] = Node(p)

        if q not in graph:
            graph[q] = Node(q)

        graph[p].add_edge(graph[q])

    return graph


def roots(edges):
    return list(set(e[0] for e in edges) - set(e[1] for e in edges))


def part_one(edges):
    graph = build_graph(edges)
    available = [graph[root] for root in roots(edges)]
    done = []

    while available:
        available.sort(key=lambda n: n.name, reverse=True)
        current = available.pop()

        for child in current.edges:
            child.parents.remove(current)
            if not len(child.parents):
                available.append(child)

        done.append(current.name)

    return ''.join(done)


def main():
    example = [
        ('C', 'A'),
        ('C', 'F'),
        ('A', 'B'),
        ('A', 'D'),
        ('B', 'E'),
        ('D', 'E'),
        ('F', 'E'),
    ]
    assert part_one(example) == 'CABDFE'

    edges = []
    with open('inputs/day07.txt', 'r') as f:
        for line in f:
            words = line.split()
            edges.append((words[1], words[7]))

    print('Part one:', part_one(edges))


if __name__ == '__main__':
    main()
