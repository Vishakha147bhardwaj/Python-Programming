import requests

# Base API endpoint (Fixed to use the valid JSONPlaceholder test site)
BASE_URL = "https://jsonplaceholder.typicode.com"

# ------------------------------------------------------------
# 1. GET Request: Fetching data with query parameters
# ------------------------------------------------------------
print("--- FETCHING DATA (GET) ---")
query_params = {
    "userId": 1
}

# Sends GET to https://jsonplaceholder.typicode.com/posts?userId=1
get_response = requests.get(f"{BASE_URL}/posts", params=query_params)

if get_response.status_code == 200:
    posts = get_response.json()  # Parse response directly into a Python list/dict
    print(f"Retrieved {len(posts)} posts for User ID 1.")
    # Show the first post
    print(f"First Post Title: {posts[0]['title']}\n")
else:
    print(f"GET Request failed with status: {get_response.status_code}")


# ------------------------------------------------------------
# 2. POST Request: Creating a new resource
# ------------------------------------------------------------
print("--- SUBMITTING DATA (POST) ---")
new_post_data = {
    "title": "Learning Web Scraping & APIs",
    "body": "This is a hands-on practical script using Python requests.",
    "userId": 1
}

# Define headers to specify we are sending JSON data
post_headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

# Send POST request with JSON payload
post_response = requests.post(f"{BASE_URL}/posts", json=new_post_data, headers=post_headers)

print(f"Response Status Code: {post_response.status_code}")  # 201 means "Created"
if post_response.status_code == 201:
    print("Resource successfully created on the server!")
    print("Server Response Data:", post_response.json())
