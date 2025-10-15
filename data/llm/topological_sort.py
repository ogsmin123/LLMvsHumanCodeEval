# The task is to perform a topological sort on a directed acyclic graph (DAG).
# A topological sort is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.

def topological_sort(graph):
    # This function performs a topological sort on a directed acyclic graph (DAG).
    # graph: A dictionary where keys are node identifiers and values are lists of adjacent nodes.
    
    visited = set()  # A set to keep track of visited nodes to avoid processing a node more than once.
    stack = []  # A list to store the topological order of nodes.

    def dfs(node):
        # Helper function to perform depth-first search.
        if node in visited:
            return  # If the node is already visited, return to avoid cycles.
        visited.add(node)  # Mark the node as visited.
        for neighbor in graph.get(node, []):
            dfs(neighbor)  # Recursively visit all the adjacent nodes.
        stack.append(node)  # Add the node to the stack after visiting all its neighbors.

    for node in graph:
        if node not in visited:
            dfs(node)  # Perform DFS for each unvisited node.

    stack.reverse()  # Reverse the stack to get the correct topological order.
    return stack  # Return the topological order of nodes.

# Example usage:
# graph = {
#     'a': ['b', 'c'],
#     'b': ['d', 'e'],
#     'c': [],
#     'd': [],
#     'e': []
# }
# print(topological_sort(graph))  # Output: ['a', 'b', 'e', 'd', 'c'] or any other valid topological order.