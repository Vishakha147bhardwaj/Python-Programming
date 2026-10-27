import random
import numpy as np

# Replicating the card drawing experiment over many iterations
num_simulations = 100_000
both_red_counter = 0
first_was_red_counter = 0

for _ in range(num_simulations):
    # Resetting the physical deck state: 3 Red (R), 2 Black (B)
    deck = ['R', 'R', 'R', 'B', 'B']
    
    # First Draw (Without replacement)
    first_draw = deck.pop(random.randint(0, len(deck) - 1))
    
    # Second Draw
    second_draw = deck.pop(random.randint(0, len(deck) - 1))
    
    if first_draw == 'R':
        first_was_red_counter += 1
        if second_draw == 'R':
            both_red_counter += 1

# Calculating probabilities
p_first_red = first_was_red_counter / num_simulations
p_both_red = both_red_counter / num_simulations

# If independent, P(Both Red) would equal P(First Red) * P(First Red)
p_independent_assumption = p_first_red * p_first_red

print("🃏 --- DEPENDENT EVENTS SYSTEM STATE ---")
print(f"Measured P(First Draw is Red)     : {p_first_red:.4f}  (Expected: 3/5 = 0.60)")
print(f"Actual Joint P(Both Red)          : {p_both_red:.4f}  (Expected: 3/5 * 2/4 = 0.30)")
print(f"Product if they were Independent  : {p_independent_assumption:.4f}")
print(f"Do independent rules fail here?   : {not np.isclose(p_both_red, p_independent_assumption, atol=0.01)}")
