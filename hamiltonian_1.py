def is_valid(v, pos, path, graph):

    if v not in graph[path[pos - 1]]:
        return False

    if v in path:
        return False
    return True

def hamiltonian_cycles_util(graph, path, pos, cycles):

    if pos == len(graph):
        if path[0] in graph[path[-1]]:
            cycles.append(path[:])
        return

    for v in graph[path[pos - 1]]:
        if is_valid(v, pos, path, graph):
            path[pos] = v
            hamiltonian_cycles_util(graph, path, pos + 1, cycles)
            path[pos] = -1 
def find_hamiltonian_cycles(graph):
    start_vertex = list(graph.keys())[0]
    path = [-1] * len(graph)
    path[0] = start_vertex
    cycles = []
    hamiltonian_cycles_util(graph, path, 1, cycles)
    return cycles

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}
cycles = find_hamiltonian_cycles(graph)
if cycles:
    print("해밀토니안 사이클:")
    for cycle in cycles:
        print(cycle)
else:
    print("해밀토니안 사이클을 찾지 못했습니다.")