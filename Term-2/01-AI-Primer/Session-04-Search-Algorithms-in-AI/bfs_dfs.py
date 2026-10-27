# bfs_dfs.py
# UNINFORMED search: Breadth-First Search (BFS) and Depth-First Search (DFS).
# The graph is a simplified map of some Karachi areas (who is connected to whom).
# Command:  python bfs_dfs.py

from collections import deque

city_map = {
    "Gulshan":    ["NIPA", "Johar"],
    "NIPA":       ["Gulshan", "Nazimabad", "Saddar"],
    "Johar":      ["Gulshan", "Shahrah-e-Faisal"],
    "Nazimabad":  ["NIPA", "Saddar"],
    "Shahrah-e-Faisal": ["Johar", "Saddar", "Clifton"],
    "Saddar":     ["NIPA", "Nazimabad", "Shahrah-e-Faisal", "Clifton"],
    "Clifton":    ["Saddar", "Shahrah-e-Faisal"],
}

def bfs(start, goal):
    """Explore level by level using a QUEUE (first in, first out)."""
    frontier = deque([[start]])        # each item is a full path
    visited = {start}
    while frontier:
        path = frontier.popleft()      # take the OLDEST path
        node = path[-1]
        if node == goal:
            return path
        for neighbour in city_map[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                frontier.append(path + [neighbour])
    return None

def dfs(start, goal):
    """Go as deep as possible first using a STACK (last in, first out)."""
    frontier = [[start]]
    visited = set()
    while frontier:
        path = frontier.pop()          # take the NEWEST path
        node = path[-1]
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbour in city_map[node]:
            if neighbour not in visited:
                frontier.append(path + [neighbour])
    return None

print("BFS path:", " -> ".join(bfs("Gulshan", "Clifton")))
print("DFS path:", " -> ".join(dfs("Gulshan", "Clifton")))
# BFS always finds the path with the FEWEST stops.
# DFS finds A path quickly but it may be longer.
