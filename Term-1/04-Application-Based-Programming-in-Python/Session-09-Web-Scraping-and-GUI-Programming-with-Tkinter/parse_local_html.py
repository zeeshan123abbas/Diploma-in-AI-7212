# parse_local_html.py
# Learn BeautifulSoup on a local HTML file first (works offline).
from bs4 import BeautifulSoup

# Step 1: read the HTML file
with open("sample_page.html", encoding="utf-8") as f:
    html = f.read()

# Step 2: parse it into a "soup" object we can search
soup = BeautifulSoup(html, "html.parser")

# Step 3: find ONE element
print("Page title:", soup.title.text)
print("Heading   :", soup.find("h1").text)

# Step 4: find ALL elements with a class
for book in soup.find_all("div", class_="book"):
    title = book.find("h2", class_="title").text
    price = book.find("span", class_="price").text
    link = book.find("a")["href"]          # read an attribute
    print(f"{title:28} {price:10} {link}")

# Step 5: CSS selectors with select()
rows = soup.select("#timings tr")[1:]      # skip the header row
for row in rows:
    cells = [td.text for td in row.find_all("td")]
    print("Timing:", cells)
