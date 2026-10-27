# goal_based_agent.py
# A MODEL-BASED + GOAL-BASED agent: it remembers what it has seen (internal model)
# and stops when its goal "all rooms clean" is reached.
# Command:  python goal_based_agent.py

world = {"A": "Dirty", "B": "Clean", "C": "Dirty"}   # three rooms in a row
rooms_in_order = ["A", "B", "C"]
location = "A"

memory = {"A": "Unknown", "B": "Unknown", "C": "Unknown"}   # the agent's internal model

def goal_reached(model):
    """Goal test: every room is known to be clean."""
    return all(status == "Clean" for status in model.values())

steps = 0
while not goal_reached(memory):
    steps += 1
    status = world[location]          # sense the current room
    memory[location] = status         # update the internal model

    if status == "Dirty":
        world[location] = "Clean"
        memory[location] = "Clean"
        print(f"Step {steps}: cleaned room {location}")
        continue

    # Choose the next room that is not yet known to be clean
    targets = [room for room in rooms_in_order if memory[room] != "Clean"]
    if not targets:
        break
    next_room = targets[0]
    print(f"Step {steps}: room {location} is clean, moving to {next_room}")
    location = next_room

print("Goal reached in", steps, "steps. Memory:", memory)
