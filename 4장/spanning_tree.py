def dfs(graph, vertex, visited, spanning_tree):

    visited[vertex] = True
    
    for adjacent, weight in enumerate(graph[vertex]):
        if weight != 0 and not visited[adjacent]:
            spanning_tree[vertex][adjacent] = weight
            spanning_tree[adjacent][vertex] = weight
            dfs(graph, adjacent, visited, spanning_tree)

def find_spanning_tree(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    spanning_tree = [[0] * num_vertices for _ in range(num_vertices)]

    start_vertex = 0
    dfs(graph, start_vertex, visited, spanning_tree)

    return spanning_tree
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 4, 0],
    [0, 3, 0, 0, 5],
    [1, 4, 0, 0, 6],
    [0, 0, 5, 6, 0]
]
spanning_tree = find_spanning_tree(graph)
print("신장 트리:")
for row in spanning_tree:
    print(row)