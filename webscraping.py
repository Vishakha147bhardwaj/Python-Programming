from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("https://toscrape.com")
rp.read()

# Check if we are allowed to scrape a specific page
can_scrape = rp.can_fetch("*", "https://toscrape.com")
print(f"Allowed to scrape? {can_scrape}")
