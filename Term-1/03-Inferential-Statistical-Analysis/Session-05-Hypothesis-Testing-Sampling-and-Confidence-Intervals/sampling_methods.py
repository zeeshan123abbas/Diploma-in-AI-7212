# sampling_methods.py
# Four common ways to pick a sample from a population
import pandas as pd

# Step 1: a population of 20 employees in three departments
population = pd.DataFrame({
    "emp_id": range(1, 21),
    "dept": ["IT"] * 8 + ["HR"] * 4 + ["Sales"] * 8,
})

# Step 2: simple random sampling - every person has an equal chance
simple = population.sample(n=5, random_state=1)
print("Simple random:", simple["emp_id"].tolist())

# Step 3: systematic sampling - every k-th person
k = 4
systematic = population.iloc[::k]
print("Systematic   :", systematic["emp_id"].tolist())

# Step 4: stratified sampling - same share from each department (25%)
stratified = population.groupby("dept").sample(frac=0.25, random_state=1)
print("Stratified   :", stratified[["emp_id", "dept"]].values.tolist())

# Step 5: cluster sampling - pick a whole group (department) at random
chosen_dept = population["dept"].drop_duplicates().sample(n=1, random_state=3).iloc[0]
cluster = population[population["dept"] == chosen_dept]
print("Cluster (" + chosen_dept + "):", cluster["emp_id"].tolist())
