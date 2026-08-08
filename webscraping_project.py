import requests
from bs4 import BeautifulSoup

# 1. Define the target URL
url = "https://toscrape.com"

# 2. Configure request headers to mimic a real web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 3. Send GET request
response = requests.get(url, headers=headers)

# 4. Validate the response status code
if response.status_code == 200:
    print("Successfully connected to the website!")
    
    # 5. Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 6. Extract the page title using find()
    page_title = soup.find("title").text.strip()
    print(f"Page Title: {page_title}\n" + "="*40)
    
    # 7. Extract all quote containers using find_all()
    # Looking for <div class="quote">
    quote_elements = soup.find_all("div", class_="quote")
    # quote_elements  = [<div class='quote'><span class='text'>hey everyone</span><a href ="youtube.com">youtube link</a></div>,]
    
    for quote in quote_elements:
        # Extract the text inside <span class="text">
        text = quote.find("span", class_="text").text
        # text = hey everyone
        # Extract the author inside <small class="author">
        author = quote.find("small", class_="author").text
        
        # Extract tags using CSS Selectors (select returns a list)
        tag_elements = quote.select("div.tags a.tag")
        # tag_elements =[<a href='' class="">vgjnvf</a>,<a href='fhvgkvfm'class =''>rgtbhgr</a>]
        tags = [tag.text for tag in tag_elements]
        # tags=[vgjnvf,rgtbhgr]
        # Print structured output
        print(f"Quote: {text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(tags)}")
        print("-" * 40)
else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")
