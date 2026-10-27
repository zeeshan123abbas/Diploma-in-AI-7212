# lab2_probability_practice.py
# Practice for Session 02: probability from data and from distributions
import pandas as pd
from scipy import stats

df = pd.read_csv("students.csv")
total = len(df)

# Step 1: simple probability from data: P(student is from Karachi)
p_karachi = (df["city"] == "Karachi").sum() / total
print("P(Karachi)            =", round(p_karachi, 3))

# Step 2: P(pass) where pass means marks >= 60
p_pass = (df["marks"] >= 60).sum() / total
print("P(pass)               =", round(p_pass, 3))

# Step 3: conditional probability P(pass | Evening batch)
evening = df[df["batch"] == "Evening"]
p_pass_given_evening = (evening["marks"] >= 60).sum() / len(evening)
print("P(pass | Evening)     =", round(p_pass_given_evening, 3))

# Step 4: binomial: if P(pass) is as above, chance that 8 of 10 new students pass
print("P(8 of 10 pass)       =", round(stats.binom.pmf(8, 10, p_pass), 4))

# Step 5: normal model of marks: P(marks > 90)
mu, sigma = df["marks"].mean(), df["marks"].std()
print("P(marks > 90) normal  =", round(1 - stats.norm.cdf(90, mu, sigma), 4))

# Step 6: z-score of the top student
top = df["marks"].max()
print("z-score of top marks  =", round((top - mu) / sigma, 2))
