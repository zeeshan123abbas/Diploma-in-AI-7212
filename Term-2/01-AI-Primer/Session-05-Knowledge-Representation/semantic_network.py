# semantic_network.py
# A SEMANTIC NETWORK stores knowledge as a graph: (subject, relation, object).
# Properties are INHERITED along "is_a" links.
# Command:  python semantic_network.py

# Each fact is a triple: (thing, relation, value)
facts = [
    ("Animal", "has", "skin"),
    ("Bird", "is_a", "Animal"),
    ("Bird", "can", "fly"),
    ("Bird", "has", "feathers"),
    ("Penguin", "is_a", "Bird"),
    ("Penguin", "cannot", "fly"),      # an exception to the general rule
    ("Sparrow", "is_a", "Bird"),
    ("Tweety", "is_a", "Sparrow"),
]

def parent_of(thing):
    """Return the class this thing belongs to (follow the is_a link)."""
    for subject, relation, value in facts:
        if subject == thing and relation == "is_a":
            return value
    return None

def ask(thing, relation, value):
    """Walk up the is_a chain until we find an answer."""
    current = thing
    while current is not None:
        if (current, relation, value) in facts:
            return True, current
        # An exception lower in the chain blocks the inherited fact
        if relation == "can" and (current, "cannot", value) in facts:
            return False, current
        current = parent_of(current)
    return False, None

questions = [("Tweety", "can", "fly"), ("Tweety", "has", "skin"),
             ("Penguin", "can", "fly"), ("Penguin", "has", "feathers")]

for thing, relation, value in questions:
    answer, found_at = ask(thing, relation, value)
    print(f"Query: {thing} {relation} {value:<9} -> {answer}  (decided at: {found_at})")
