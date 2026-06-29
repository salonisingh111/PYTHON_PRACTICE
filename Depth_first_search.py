def dfs(graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)

            row = graph[current_node]
            for neighbor in range(len(row) - 1, -1, -1):
                if row[neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
            