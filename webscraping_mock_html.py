from bs4 import BeautifulSoup
import requests

mock_html = """
<html>
    <head><title>Learning Store</title></head>
    <body>
        <h1 class="main-title">Available Courses</h1>
        <div class="course-card" id="course-1">
            <h2 class="course-name">Python for Beginners</h2>
            <p class="price">$29</p>
        </div>
        <div class="course-card" id="course-2">
            <h2 class="course-name">Web Scraping 101</h2>
            <p class="price">$49</p>
        </div>
    </body>
</html>
"""
print(type(mock_html))

soup = BeautifulSoup(mock_html, "html.parser")
print(soup)

first_title = soup.find("h1", class_="main-title")
# first_title = <h1 class="main-title">Available Courses</h1>
print(f"First Title Text: {first_title.text}")


all_prices = soup.find_all("p", class_="price")
print("\n--- Listing All Prices ---")
# all_prices = [<p class='price'>$29</p>,<p class ='price'>$49'</p>]
print(all_prices[0].text)
print(all_prices[1].text)
for price in all_prices:
    print(price.text)

# 3. Using CSS Selectors (select) to find course names inside course cards
# The dot (.) means class, and the space means "nested inside"
course_names = soup.select(".course-card .course-name")
print("\n--- Listing Course Names via CSS Selectors ---")
# course_names =['<div class="course-card" id="course-1"><h2 class="course-name">Python for Beginners</h2></div>',]
for course in course_names:
    print(course.text)
