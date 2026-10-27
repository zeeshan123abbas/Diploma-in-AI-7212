# ml_types_demo.py
# One tiny example of each main type of Machine Learning.
# Command:  python ml_types_demo.py

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# 1) Supervised learning (we have the answers) -> predict house price from size
sizes = np.array([[500], [800], [1000], [1200], [1500]])   # square feet
prices = np.array([50, 78, 100, 118, 152])                  # lakh rupees
reg = LinearRegression().fit(sizes, prices)
print("Supervised: price of 1100 sq ft =", round(reg.predict([[1100]])[0], 1), "lakh")

# 2) Unsupervised learning (no answers) -> group customers by spending
spending = np.array([[2], [3], [2.5], [20], [22], [21]])    # thousand rupees per month
groups = KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(spending)
print("Unsupervised: customer groups =", groups)

# 3) Reinforcement learning (learn by reward) -> pick the best of 3 slot machines
rng = np.random.default_rng(0)
true_win_rates = [0.2, 0.5, 0.8]      # hidden from the agent
estimates = [0.0, 0.0, 0.0]           # what the agent believes
counts = [0, 0, 0]
for step in range(500):
    if rng.random() < 0.1:                     # 10% of the time: explore randomly
        arm = int(rng.integers(3))
    else:                                      # 90% of the time: use the best guess
        arm = int(np.argmax(estimates))
    reward = 1 if rng.random() < true_win_rates[arm] else 0
    counts[arm] += 1
    estimates[arm] += (reward - estimates[arm]) / counts[arm]   # running average
print("Reinforcement: agent's estimates =", [round(e, 2) for e in estimates])
print("Reinforcement: best machine found =", int(np.argmax(estimates)))
