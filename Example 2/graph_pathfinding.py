"""
Graph Pathfinding Algorithms
Shows BFS and DFS traversal using adjacency lists.
"""

from collections import deque
from typing import Dict, List, Set


def dfs(graph: Dict[str, List[str]], start: str, visited=None) -> List[str]:
    """Depth-First Search (recursive)."""
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order


def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """Breadth-First Search (iterative)."""
    visited: Set[str] = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    print("DFS:", dfs(graph, "A"))
    print("BFS:", bfs(graph, "A"))

