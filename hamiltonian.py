import random
def is_hamiltonian_cycle(graph, path):
    return len(path) == len(graph) and path[0] in graph[path[-1]]

def find_hamiltonian_cycle(graph):
    for _ in range(1000):
        start_vertex = random.choice(list(graph.keys()))
        path = [start_vertex]

        for _ in range(len(graph) - 1):
            neighbors = [v for v in graph[path[-1]] if v not in path]
            if not neighbors:
                break
            next_vertex = random.choice(neighbors)
            path.append(next_vertex)
        if is_hamiltonian_cycle(graph, path):
            return path  
    return None  
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}
cycle = find_hamiltonian_cycle(graph)
if cycle:
    print("해밀토니안 사이클:", cycle)
else:
    print("해밀토니안 사이클을 찾지 못했습니다.")