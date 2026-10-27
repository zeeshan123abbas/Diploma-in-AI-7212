# lab1_ci_and_t_tests.py
# Practice for Session 05 and 06: confidence interval and t-tests
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("campaign.csv")
orders = df["order_value"]

# Step 1: 95% confidence interval for the average order value
n = len(orders)
se = orders.std(ddof=1) / np.sqrt(n)
low, high = stats.t.interval(0.95, df=n - 1, loc=orders.mean(), scale=se)
print(f"Average order = Rs. {orders.mean():.0f}, 95% CI = ({low:.0f}, {high:.0f})")

# Step 2: one-sample t-test: is the average order different from Rs. 2,300?
t, p = stats.ttest_1samp(orders, popmean=2300)
print(f"One-sample t-test vs 2300: t = {t:.2f}, p = {p:.4f}")

# Step 3: independent t-test: Social vs Email channel
social = df[df["channel"] == "Social"]["order_value"]
email = df[df["channel"] == "Email"]["order_value"]
t, p = stats.ttest_ind(social, email, equal_var=False)
print(f"Social vs Email: t = {t:.2f}, p = {p:.4f}")
print("Social orders are different" if p < 0.05 else "No significant difference")
