import re

# text = "Contact support at help@company.com or sales@company.com"
# # Pattern to find the first email address
# email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# match = re.search(email_pattern, text)

# if match:
#     print("Match found!")
#     print(f"Matched text: {match.group()}")    # Output: help@company.com
#     print(f"Position (indices): {match.span()}") # Output: (19, 35)
# else:
#     print("No match found.")


# text = "Order status: Item 1042 is shipped, Item 8823 is processing."
# # Pattern to find all sequences of digits
# digit_pattern = r"\d+"

# all_matches = re.findall(digit_pattern, text)

# print(f"All matched items: {all_matches}") 
# # Output: ['1042', '8823']


text = "Phone numbers: 555-123-4567 and 555-987-6543."
# Pattern to match the phone numbers
phone_pattern = r"\d{3}-\d{3}-\d{4}"

# Replace all phone numbers with a redacted placeholder
redacted_text = re.sub(phone_pattern, "[REDACTED]", text)

print(redacted_text)
# Output: Phone numbers: [REDACTED] and [REDACTED].
