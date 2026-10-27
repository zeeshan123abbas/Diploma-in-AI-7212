# uniform_cost_search.py
# UNINFORMED search with costs: Uniform Cost Search (UCS) always expands the
# path with the LOWEST total distance so far. Distances (km) are made up for practice.
# Command:  python uniform_cost_search.py

import heapq   # a priority queue: always gives back the smallest item first

road_km = {
    "Gulshan":    {"NIPA": 3, "Johar": 4},
    "NIPA":       {"Gulshan": 3, "Nazimabad": 5, "Saddar": 13},
    "Johar":      {"Gulshan": 4, "Shahrah-e-Faisal": 5},
    "Nazimabad":  {"NIPA": 5, "Saddar": 7},
    "Shahrah-e-Faisal": {"Johar": 5, "Saddar": 9, "Clifton": 10},
    "Saddar":     {"NIPA": 13, "Nazimabad": 7, "Shahrah-e-Faisal": 9, "Clifton": 5},
    "Clifton":    {"Saddar": 5, "Shahrah-e-Faisal": 10},
}

def uniform_cost_search(start, goal):
    frontier = [(0, [start])]          # (cost so far, path)
    best_cost = {start: 0}
    expanded = 0
    while frontier:
        cost, path = heapq.heappop(frontier)   # cheapest path first
        node = path[-1]
        expanded += 1
        if node == goal:
            return path, cost, expanded
        for neighbour, km in road_km[node].items():
            new_cost = cost + km
            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                heapq.heappush(frontier, (new_cost, path + [neighbour]))
    return None, None, expanded

path, total, expanded = uniform_cost_search("Gulshan", "Clifton")
print("Cheapest path:", " -> ".join(path))
print("Total distance:", total, "km | nodes expanded:", expanded)
