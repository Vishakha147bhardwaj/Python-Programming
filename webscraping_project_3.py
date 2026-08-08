import requests
from bs4 import BeautifulSoup

# 1. Define the target URL
url = "https://vishakha-portfolio-eight.vercel.app/"

# 2. Configure request headers
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# 3. Send GET request
response = requests.get(url, headers=headers)

# 4. Validate response
if response.status_code == 200:
    print("Successfully connected to the website!\n")

    # 5. Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # -------------------------------
    # Page Title
    # -------------------------------
    title = soup.find("title")
    if title:
        print(f"Page Title : {title.get_text(strip=True)}")

    # -------------------------------
    # Meta Description
    # -------------------------------
    description = soup.find("meta", attrs={"name": "description"})
    if description:
        print(f"Description : {description.get('content')}")

    print("=" * 60)

    # -------------------------------
    # Name
    # -------------------------------
    name = soup.find("span", class_="name-highlight")
    if name:
        print(f"Name : {name.get_text(strip=True)}")

    # -------------------------------
    # Role
    # -------------------------------
    role = soup.find("p", string=lambda x: x and "Software Engineer" in x)
    if role:
        print(f"Role : {role.get_text(strip=True)}")

    # -------------------------------
    # Introduction
    # -------------------------------
    intro = soup.find(
        "p",
        string=lambda x: x and "Full-Stack Software Engineer" in x
    )
    if intro:
        print(f"\nIntroduction:\n{intro.get_text(' ', strip=True)}")

    print("=" * 60)

    # -------------------------------
    # Social Links
    # -------------------------------
    print("Social Links:")

    social_links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if any(site in href for site in [
            "linkedin.com",
            "github.com",
            "mailto:"
        ]):
            social_links.append(href)

    for link in social_links:
        print(link)

    print("=" * 60)

    # -------------------------------
    # Navigation Menu
    # -------------------------------
    print("Navigation Menu:")

    for button in soup.find_all("button"):
        text = button.get_text(strip=True)

        if text in [
            "Professional",
            "Projects",
            "Experience",
            "Contact"
        ]:
            print("-", text)

else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")