import requests

# 1. Sending a GET Request with Parameters and Headers
url = "https://httpbin.org"
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
custom_params = {
    "search": "laptop", 
    "page": 2
}

response = requests.get(url, headers=custom_headers, params=custom_params)

print("--- GET REQUEST ---")
print(f"Status Code: {response.status_code}") # Outputs 200 if successful
print(f"Final URL: {response.url}") # Note how params are automatically attached to the URL


# 2. Sending a POST Request with Data
post_url = "https://httpbin.org"
login_data = {
    "username": "learner123", 
    "password": "securepassword"
}

post_response = requests.post(post_url, headers=custom_headers, data=login_data)

print("\n--- POST REQUEST ---")
print(f"Status Code: {post_response.status_code}")
