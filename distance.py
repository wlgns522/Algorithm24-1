import itertools

def total_distance(path, graph):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]
    return distance

def tsp_brute_force(graph):
    cities = list(graph.keys())
    shortest_path = None
    shortest_distance = float('inf')

    for path in itertools.permutations(cities):
        distance = total_distance(path, graph)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
shortest_path, shortest_distance = tsp_brute_force(graph)
if shortest_path:
    print("최단 경로:", shortest_path)
    print("최단 거리:", shortest_distance)
else:
    print("최단 경로를 찾지 못했습니다.")