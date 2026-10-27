# forward_chaining.py
# PRODUCTION RULES + FORWARD CHAINING: start from known facts, keep firing
# IF-THEN rules until no new fact appears. This is how simple expert systems decide.
# Command:  python forward_chaining.py

# Knowledge base: each rule is (set of conditions, conclusion)
rules = [
    ({"has_fever", "has_cough"}, "possible_flu"),
    ({"possible_flu", "body_ache"}, "likely_flu"),
    ({"likely_flu"}, "advise_rest_and_fluids"),
    ({"has_rash", "has_fever"}, "possible_measles"),
    ({"possible_measles"}, "advise_doctor_visit"),
]

# Facts observed about one patient (the "working memory")
facts = {"has_fever", "has_cough", "body_ache"}
print("Starting facts:", sorted(facts))

round_number = 0
new_fact_added = True
while new_fact_added:                       # repeat until nothing changes
    new_fact_added = False
    round_number += 1
    for conditions, conclusion in rules:
        # A rule FIRES when all its conditions are already known facts
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            new_fact_added = True
            print(f"Round {round_number}: {sorted(conditions)} => {conclusion}")

print("Final facts:", sorted(facts))
print("Advice:", [f for f in facts if f.startswith("advise")])
# Note: this toy system is for learning AI concepts, not for real medical advice.
