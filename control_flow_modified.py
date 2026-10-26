# # A simulated system log of incoming signal weights
# weights = [120, 45, 300, -15, 180, 999, 220]

# for w in weights:
#     # 1. Error check: Ignore invalid negative values and keep going
#     if w < 0:
#         print(f"Skipping bad data point: {w}")
#         continue  
        
#     # 2. Critical Threshold: Terminate the whole pipeline if an explosion hazard is hit
#     if w == 999:
#         print("CRITICAL FATAL SYSTEM FAILURE. ABORTING PIPELINE IMMEDATELY.")
#         break  
        
#     # 3. Standard Branching
#     if w > 250:
#         print(f"Heavy Cargo: {w}kg")
#     elif w >= 100:
#         print(f"Standard Cargo: {w}kg")
#     else:
#         print(f"Light Cargo: {w}kg")


# # --- RANGE EXAMPLE ---
# # Print an alert message exactly 3 times
# for attempt in range(1, 4):
#     print(f"API Connection Attempt #{attempt}...")


# # --- ENUMERATE EXAMPLE ---
# # Track the exact list index position alongside the data item
# notifications = ["Welcome User", "Verify Email", "Update Profile"]

# for index, msg in enumerate(notifications, start=1):
#     print(f"Task [{index}]: {msg}")


# # --- ZIP EXAMPLE ---
# # Pair related parallel lists together automatically
# users = ["Alice", "Bob", "Charlie"]
# roles = ["Admin", "Developer", "Designer","DatabaseExecutive"]

# for name, title in zip(users, roles):
#     print(f"User: {name} | System Role: {title}")


# A simulated API response containing a list of generated tool queries
api_response = [
    {"query_id": 101, "topic": "Quantum Computing", "status": "completed"},
    {"query_id": 102, "topic": "Stock Predictions", "status": "pending"},
    {"query_id": 103, "topic": "", "status": "failed"},  # Blank topic
    {"query_id": 104, "topic": "Climate Models", "status": "completed"}
]

print("--- Starting Automated Response Processing ---")

for job in api_response:
    # Check for empty data before processing fields
    if not job["topic"]:
        print(f"Alert: Job {job['query_id']} contains no searchable text. Skipping.")
        continue
        
    # Act dynamically based on nested status flags
    if job["status"] == "completed":
        print(f"SUCCESS: Saved analytical report for '{job['topic']}'.")
    elif job["status"] == "pending":
        print(f"QUEUE: Job {job['query_id']} ('{job['topic']}') is still generating...")
    else:
        print(f"FAILURE: Job {job['query_id']} failed on the server side.")
