# # --- Code Example: Indexing & Slicing ---

# text = "Artificial Intelligence"

# # # 1. Indexing Examples
# # first_char = text[0]        # 'A' (First character)
# # space_char = text[10]       # ' ' (Space character)
# # last_char = text[-1]        # 'e' (Last character)
# # second_last = text[-2]      # 'c' (Second to last character)

# # print(f"Indexing: {first_char=}, {last_char=}")

# # 2. Slicing Examples
# substring_word = text[0:10]  # 'Artificial' (Extracts index 0 through 9)
# till_end = text[11:]        # 'Intelligence' (From index 11 to the very end)
# negative_slice = text[-12:-5]  # 'Intelligence' (Counts 12 from the right to the end)

# print(f"Slicing: {substring_word=}")
# print(f"Slicing till end: {till_end=}")
# print(f"negative slice {negative_slice=}")

# # 3. Utilizing the Step Parameter
# every_second_char = text[::2]  # 'Atfca ntllgne' (Steps by 2)
# reversed_text = text[::-1]     # 'ecnegilletnI laicifitrA' (Reverses the string)

# print(f"Step by 2: {every_second_char=}")
# print(f"Reversed: {reversed_text=}")


# --- Code Example: f-strings ---

# model_name = "GPT-4o"
# tokens_processed = 452890
# cost_per_million = 5.00

# # 1. Filling in blanks directly
# summary = f"The model {model_name} successfully processed the request."
# print(summary)

# # 2. Evaluating expressions inside f-strings
# total_cost = (tokens_processed / 1_000_000) * cost_per_million
# cost_report = f"Total Cost for {tokens_processed:,} tokens: ${total_cost:.4f}"
# print(cost_report)

# # 3. Calling methods inside f-strings
# user = "   alex smith   "
# welcome_msg = f"Welcome back, {user.strip().title()}!"
# print(welcome_msg)

# --- Code Example: Text Editing Methods ---

# 1. .split() Example
csv_data = "Python,Data Science,Machine Learning,Generative AI"
skills_list = csv_data.split("/") 
print("Split List:", skills_list) 
# Output: ['Python', 'Data Science', 'Machine Learning', 'Generative AI']

# 2. .join() Example
words = ["AI", "is", "transforming", "industries"]
sentence = " ".join(words)
print("Joined String:", sentence)
# Output: 'AI is transforming industries'

# 3. .strip() Example
dirty_input = "\n\t  user_name_123   \n"
clean_input = dirty_input.strip()
print(f"Raw: '{dirty_input}' -> Cleaned: '{clean_input}'")
# Output: 'user_name_123'

# 4. .replace() Example
raw_template = "Hello [NAME], your verification code is [CODE]."
filled_template = raw_template.replace("[NAME]", "Sarah").replace("[CODE]", "5821")
print("Replaced Template:", filled_template)
# Output: 'Hello Sarah, your verification code is 5821.'
