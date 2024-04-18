import itertools

def tsp_brute_force(graph):
    n = len(graph)
    
    all_permutations = itertools.permutations(range(1, n))
    
    min_cost = float('inf')
    min_path = None
    
    for perm in all_permutations:

        cost = graph[0][perm[0]] 
        
        for i in range(len(perm) - 1):
            cost += graph[perm[i]][perm[i + 1]]
        

        cost += graph[perm[-1]][0]
        

        if cost < min_cost:
            min_cost = cost
            min_path = (0,) + perm + (0,)
    
    return min_path, min_cost

example_graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_path, min_cost = tsp_brute_force(example_graph)
print("최단 경로:", min_path)
print("최소 비용:", min_cost)