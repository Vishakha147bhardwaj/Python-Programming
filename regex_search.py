# import re

# email_text = "Hello team, my shipment for ID-8942 hasn't arrived yet. Thanks!"
# # Pattern explanation: Look for 'ID-', then exactly four digits (\d{4})
# pattern = r"ID-\d{4}"
# match = re.search(pattern, email_text)

# if match:
#     print("Found Order ID:", match.group())
# else:
#     print("No Order ID found in this message.")

# import re

# page_text = "Premium Package: $99/mo. Basic Package: $29/mo. Setup fee is $5."
# # Pattern explanation: Look for a literal $, followed by one or more digits (\d+)
# pattern = r"\$\d+"

# all_prices = re.findall(pattern, page_text)

# print(all_prices)

import re

chat_log = "Call client Sarah at 555-123-4567 or email her at sarah@example.com"
# Pattern explanation: 3 digits, dash, 3 digits, dash, 4 digits
phone_pattern = r"\d{3}-\d{3}-\d{4}"

clean_log = re.sub(phone_pattern, "[HIDDEN NUMBER]", chat_log)

print("Privacy-Compliant Log:")
print(clean_log)
