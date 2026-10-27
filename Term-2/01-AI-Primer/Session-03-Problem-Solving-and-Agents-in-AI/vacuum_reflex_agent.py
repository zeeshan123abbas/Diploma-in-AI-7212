# vacuum_reflex_agent.py
# A SIMPLE REFLEX AGENT: it looks only at what it senses right now and follows
# condition -> action rules. World: two rooms, A and B, each Clean or Dirty.
# Command:  python vacuum_reflex_agent.py

# The environment (the world the agent lives in)
world = {"A": "Dirty", "B": "Dirty"}
agent_location = "A"

def reflex_vacuum_agent(location, status):
    """Percept = (location, status). Returns an action using fixed rules."""
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "MoveRight"
    else:
        return "MoveLeft"

# Run the agent for 6 time steps
score = 0
for step in range(1, 7):
    percept = (agent_location, world[agent_location])   # 1) SENSE
    action = reflex_vacuum_agent(*percept)              # 2) THINK (rule lookup)

    # 3) ACT: the action changes the environment
    if action == "Suck":
        world[agent_location] = "Clean"
        score += 10                                     # reward for cleaning
    elif action == "MoveRight":
        agent_location = "B"
        score -= 1                                      # small cost for moving
    elif action == "MoveLeft":
        agent_location = "A"
        score -= 1

    print(f"Step {step}: percept={percept} action={action:<9} world={world}")

print("Performance score:", score)
# Notice: after both rooms are clean the agent keeps moving back and forth,
# wasting points. It has no memory, so it does not know the job is finished.
