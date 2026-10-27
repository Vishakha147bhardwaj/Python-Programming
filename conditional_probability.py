import pandas as pd

# Create a simple log of 10 people walked past today
data = {
    'Is_Raining': [True, True, True, True, False, False, False, False, False, False],
    'Has_Umbrella': [True, True, True, False, False, False, False, False, False, True]
}

df = pd.DataFrame(data)

# 1. Total counts
total_people = len(df)                          # 10
rainy_people = df['Is_Raining'].sum()            # 4
rainy_and_umbrella = ((df['Is_Raining'] == True) & (df['Has_Umbrella'] == True)).sum() # 3

# 2. Unconditional Probability: Baseline chance of seeing an umbrella
p_umbrella = df['Has_Umbrella'].mean()

# 3. Conditional Probability: P(Umbrella | Rain)
# Formula: (People with Umbrella AND Rain) divided by (Total People in Rain)
p_umbrella_given_rain = rainy_and_umbrella / rainy_people

print("🌧️ --- UMBRELLA CONDITIONAL PROBABILITY ---")
print(f"Unconditional P(Umbrella) : {p_umbrella:.0%} (Total sample space)")
print(f"Conditional P(Umbrella | Rain) : {p_umbrella_given_rain:.0%} (Filtered to rainy rows only)")
