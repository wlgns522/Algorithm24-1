def dfs(graph, start, visited, spanning_tree):
    visited[start] = True 

    for neighbor in range(len(graph[start])):
        if graph[start][neighbor] != 0 and not visited[neighbor]:
            spanning_tree[start][neighbor] = 1  
            spanning_tree[neighbor][start] = 1  
            dfs(graph, neighbor, visited, spanning_tree)

def prim(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices 
    spanning_tree = [[0] * num_vertices for _ in range(num_vertices)] 

    start_vertex = 0
    dfs(graph, start_vertex, visited, spanning_tree)

    return spanning_tree

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
spanning_tree = prim(graph)

print("신장 트리:")
for row in spanning_tree:
    print(row)