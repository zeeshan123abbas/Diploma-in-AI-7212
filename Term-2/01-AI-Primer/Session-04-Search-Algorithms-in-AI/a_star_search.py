# a_star_search.py
# INFORMED search: Greedy Best-First and A* use a HEURISTIC h(n) =
# estimated straight-line km from a place to Clifton (the goal).
# Command:  python a_star_search.py

import heapq

road_km = {
    "Gulshan":    {"NIPA": 3, "Johar": 4},
    "NIPA":       {"Gulshan": 3, "Nazimabad": 5, "Saddar": 13},
    "Johar":      {"Gulshan": 4, "Shahrah-e-Faisal": 5},
    "Nazimabad":  {"NIPA": 5, "Saddar": 7},
    "Shahrah-e-Faisal": {"Johar": 5, "Saddar": 9, "Clifton": 10},
    "Saddar":     {"NIPA": 13, "Nazimabad": 7, "Shahrah-e-Faisal": 9, "Clifton": 5},
    "Clifton":    {"Saddar": 5, "Shahrah-e-Faisal": 10},
}

# Straight-line estimate to Clifton. It never OVER-estimates the real road distance,
# so A* is guaranteed to find the cheapest path (the heuristic is "admissible").
straight_line_to_clifton = {
    "Gulshan": 14, "NIPA": 11, "Johar": 12, "Nazimabad": 10,
    "Shahrah-e-Faisal": 8, "Saddar": 4, "Clifton": 0,
}

def best_first(start, goal, use_path_cost):
    """use_path_cost=False -> Greedy (f = h).  True -> A* (f = g + h)."""
    frontier = [(straight_line_to_clifton[start], 0, [start])]   # (f, g, path)
    visited = set()
    expanded = 0
    while frontier:
        f, g, path = heapq.heappop(frontier)
        node = path[-1]
        if node == goal:
            return path, g, expanded
        if node in visited:
            continue
        visited.add(node)
        expanded += 1
        for neighbour, km in road_km[node].items():
            new_g = g + km                                  # real distance so far
            h = straight_line_to_clifton[neighbour]         # estimate to goal
            new_f = new_g + h if use_path_cost else h
            heapq.heappush(frontier, (new_f, new_g, path + [neighbour]))
    return None, None, expanded

for name, flag in [("Greedy best-first", False), ("A*", True)]:
    path, km, expanded = best_first("Gulshan", "Clifton", flag)
    print(f"{name:<18}: {' -> '.join(path)} | {km} km | expanded {expanded}")
