def dfs(adj_matrix, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # Add neighbors in reverse order to maintain standard DFS traversal order
            # (Visiting the first available neighbor first)
            for neighbor, connected in enumerate(adj_matrix[node]):
                if connected == 1 and neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited


# Passed:1. You should have a function named dfs that takes two arguments.
# Passed:2. dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1) should return a list with 1, 2, 3, and 0.
# Passed:3. dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3) should return a list with 1, 2, 3, and 0.
# Passed:4. dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3) should return [3].
# Passed:5. dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3) should return a list with 3 and 2.
# Passed:6. dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0) should return a list with 0 and 1.
# Passed:7. The dfs function should return the correct results.
