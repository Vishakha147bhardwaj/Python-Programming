# import random

# # Set a seed for reproducibility
# random.seed(42)

# # Simulating a single coin flip
# flip = random.choice(['Heads', 'Tails'])
# print(f"Single Flip Result: {flip}")

# # Simulating 10 coin flips using a list comprehension
# ten_flips = [random.choice(['Heads', 'Tails']) for _ in range(10)]
# print(f"10 Flips Results: {ten_flips}")

# # Counting the outcomes
# heads_count = ten_flips.count('Heads')
# tails_count = ten_flips.count('Tails')
# print(f"Heads: {heads_count}, Tails: {tails_count}")


# import random

# # Simulating a single roll of a 6-sided die
# single_roll = random.randint(1, 6)
# print(f"Single Die Roll: {single_roll}")

# # Simulating rolling two dice simultaneously (e.g., for board games)
# def roll_two_dice():
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     return die1, die2, die1 + die2

# d1, d2, total = roll_two_dice()
# print(f"Rolled a {d1} and a {d2}. Total Sum: {total}")


# import random

# # Exact Probability
# theoretical_p = 1 / 2  # 0.5
# print(f"Theoretical Probability of Heads: {theoretical_p}")

# # Empirical Probability with varying simulation sizes
# def estimate_heads(num_flips):
#     flips = [random.choice(['Heads', 'Tails']) for _ in range(num_flips)]
#     return flips.count('Heads') / num_flips

# print(f"Estimated P(Heads) with 10 flips:    {estimate_heads(10)}")
# print(f"Estimated P(Heads) with 1,000 flips: {estimate_heads(1000)}")
# print(f"Estimated P(Heads) with 100,000 flips: {estimate_heads(100000)}")


import random

# Theoretical
theoretical_seven = 6 / 36
print(f"Theoretical P(Sum = 7): {theoretical_seven:.4f}")

# Simulation
def simulate_dice_sum_seven(trials):
    seven_count = 0
    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            seven_count += 1
    return seven_count / trials

print(f"Simulated P(Sum = 7) with 100 trials:   {simulate_dice_sum_seven(100):.4f}")
print(f"Simulated P(Sum = 7) with 10,000 trials: {simulate_dice_sum_seven(10000):.4f}")
