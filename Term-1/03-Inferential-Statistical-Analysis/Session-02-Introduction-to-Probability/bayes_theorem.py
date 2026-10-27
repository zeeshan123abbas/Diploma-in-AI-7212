# bayes_theorem.py
# Bayes' theorem: update a probability when new evidence arrives.
# Problem: 1% of emails are spam-like "lottery" scams.
# A filter flags 95% of scams, but also wrongly flags 4% of normal emails.
# If an email is flagged, what is the chance it really is a scam?

# Step 1: what we know
p_scam = 0.01                 # prior: P(scam)
p_flag_given_scam = 0.95      # P(flag | scam)
p_flag_given_normal = 0.04    # P(flag | normal)

# Step 2: total probability of being flagged
p_normal = 1 - p_scam
p_flag = p_flag_given_scam * p_scam + p_flag_given_normal * p_normal

# Step 3: Bayes' theorem  P(scam | flag) = P(flag | scam) * P(scam) / P(flag)
p_scam_given_flag = p_flag_given_scam * p_scam / p_flag

print("P(flag)        =", round(p_flag, 4))
print("P(scam | flag) =", round(p_scam_given_flag, 4))
# Only about 19%! Because scams are rare, most flags are false alarms.
