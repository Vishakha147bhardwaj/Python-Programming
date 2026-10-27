import numpy as np

# Set simulation parameters
num_trials = 100_000

# Event A: Coin Flip (0 = Tails, 1 = Heads) -> P(Heads) = 0.50
coin_flips = np.random.choice([0, 1], size=num_trials, p=[0.5, 0.5])

# Event B: Die Roll (1 through 6) -> P(Roll a 6) = 1/6 ≈ 0.1667
die_rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=num_trials)

# Empirical calculations from simulation
p_a = np.mean(coin_flips == 1)
p_b = np.mean(die_rolls == 6)

# Joint Event: Both Heads AND Roll a 6 happen simultaneously
joint_occurrence = (coin_flips == 1) & (die_rolls == 6)
p_a_and_b = np.mean(joint_occurrence)

# Theoretical Multiplication Rule Check
p_independent_product = p_a * p_b

print("🪙 --- INDEPENDENT EVENTS VERIFICATION ---")
print(f"Empirical P(A) [Heads]           : {p_a:.4f}")
print(f"Empirical P(B) [Roll a 6]        : {p_b:.4f}")
print(f"Actual Joint P(A ∩ B) Measured   : {p_a_and_b:.4f}")
print(f"Calculated P(A) * P(B) Product   : {p_independent_product:.4f}")
print(f"Are they independent?            : {np.isclose(p_a_and_b, p_independent_product, atol=0.01)}")
