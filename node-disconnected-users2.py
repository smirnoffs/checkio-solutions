from collections import defaultdict


def reachable_nodes(graph, start, reached):
    reached.add(start)
    for node in graph.get(start, []):
        if node not in reached:
            for reached_node in reachable_nodes(graph, node, reached):
                reached.add(reached_node)
    return reached


def disconnected_users(net, users, source, crushes):
    reachable_net = defaultdict(list)
    total_population = sum(users.values())
    if source in crushes:
        # In case if the sending node is crushed
        return total_population
    for start, end in net:
        if not {start, end} & set(crushes):
            reachable_net[start].append(end)
    available_nodes = reachable_nodes(reachable_net, source, set())
    reachable_population = sum(users[node] for node in available_nodes)
    return total_population - reachable_population


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    assert disconnected_users([["A", "B"], ["B", "C"], ["C", "D"]],
                              {"A": 10, "C": 30, "B": 20, "D": 40},
                              "A",
                              ["B"]) == 90
    assert disconnected_users([["A", "B"], ["B", "C"], ["C", "D"]],
                              {"A": 10, "C": 30, "B": 20, "D": 40},
                              "A",
                              ["A"]) == 100
    print('Done. Try to check now. There are a lot of other tests')
