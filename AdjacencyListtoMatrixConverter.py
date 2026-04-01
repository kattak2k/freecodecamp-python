def adjacency_list_to_matrix(adj_graph):
    final_list = []
    nodes = len(adj_graph)  # Fix 1: derive node count from keys, not values
    
    for x in adj_graph.items():
        adj_list = [0] * nodes  # Fix 2: reset inside loop with correct size
        for y in x[1]:
            adj_list[y] = 1
        print(adj_list)
        final_list.append(adj_list)
    
    return final_list

# adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
# adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
# print(adjacency_list_to_matrix({0: [], 1: [], 2: []}))

# 9. When given the adjacency list {0: [], 1: [], 2: []}, the function should return [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
# 7. When given the adjacency list {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}, the function should return [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]].
# 8. When given the adjacency list {0: [1], 1: [0]}, the function should return [[0, 1], [1, 0]].
