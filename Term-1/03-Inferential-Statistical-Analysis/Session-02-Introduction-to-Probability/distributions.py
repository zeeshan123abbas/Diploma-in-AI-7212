# distributions.py
# Binomial, Poisson and Normal distributions with scipy.stats
from scipy import stats

# Binomial: 10 MCQs, each guessed with p = 0.25. P(exactly 3 correct)?
p_three = stats.binom.pmf(k=3, n=10, p=0.25)
print("Binomial  P(X = 3)      =", round(p_three, 4))

# Poisson: a shop gets 4 customers per hour on average. P(exactly 6)?
p_six = stats.poisson.pmf(k=6, mu=4)
print("Poisson   P(X = 6)      =", round(p_six, 4))

# Normal: heights with mean 165 cm, sd 8 cm. P(height < 175)?
p_short = stats.norm.cdf(175, loc=165, scale=8)
print("Normal    P(X < 175)    =", round(p_short, 4))

# Expected value (mean) of each distribution
print("E[binomial] =", stats.binom.mean(n=10, p=0.25))
print("E[poisson]  =", stats.poisson.mean(mu=4))
