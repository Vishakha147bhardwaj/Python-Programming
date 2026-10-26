import requests
from bs4 import BeautifulSoup

# ==========================================
# 1. WORKING WITH APIs (GET Request with Params)
# ==========================================
print("--- 1. Testing API GET Request ---")
api_url = "https://httpbin.org"
query_params = {"search": "python_tutorials", "limit": 3}
custom_headers = {"User-Agent": "MyScrapingBot/1.0"}

# Execute the GET request
api_response = requests.get(api_url, params=query_params, headers=custom_headers)

print(f"Status Code: {api_response.status_code}")
# if api_response.status_code == 200:
    # Parse JSON data returned by the API
    # data = api_response.json()
    # print(f"Server received our User-Agent: {data['headers']['User-Agent']}")
    # print(f"Server received our Params: {data['args']}\n")


# ==========================================
# 2. WEB SCRAPING WITH BEAUTIFULSOUP
# ==========================================
print("--- 2. Parsing HTML with BeautifulSoup ---")

# Mock HTML data simulating a real web page
mock_html_content = """
<html>
    <head><title>The Developer Hub</title></head>
    <body>
        <h1 id="main-title">Latest Articles</h1>
        <div class="content-box">
            <ul class="article-list">
                <li class="article-item feature" data-id="101">
                    <a href="/blog/python-basics">Mastering Python Basics</a>
                    <span class="author">By Jane Doe</span>
                </li>
                <li class="article-item" data-id="102">
                    <a href="/blog/web-scraping">Web Scraping 101</a>
                    <span class="author">By John Smith</span>
                </li>
                <li class="article-item" data-id="103">
                    <a href="/blog/advanced-apis">Building Advanced APIs</a>
                    <span class="author">By Jane Doe</span>
                </li>
            </ul>
        </div>
    </body>
</html>
"""

# Initialize BeautifulSoup parser
soup = BeautifulSoup(mock_html_content, 'html.parser')

# A. Using find() - Grabs the FIRST matching element
main_heading = soup.find('h1', id='main-title')
print(f"find() result (by ID): {main_heading.text}")

# B. Using find_all() - Grabs ALL matching elements as a list
all_authors = soup.find_all('span', class_='author')
print("\nfind_all() result (by Class):")
for author in all_authors:
    print(f" - Found Author: {author.text}")

# C. Using CSS Selectors with select() and select_one()
# select() uses standard CSS styling syntax ('.' for class, '#' for ID, ' ' for hierarchy)
featured_article = soup.select_one('li.article-item.feature a')
all_links = soup.select('ul.article-list li a')

print(f"\nselect_one() CSS result: Featured URL is '{featured_article['href']}'")
print("select() CSS list result:")
for link in all_links:
    print(f" - Link text: '{link.text}' maps to path: {link['href']}")
