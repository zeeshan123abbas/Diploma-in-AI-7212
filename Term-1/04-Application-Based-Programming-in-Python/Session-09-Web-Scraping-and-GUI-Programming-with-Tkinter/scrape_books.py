# scrape_books.py
# Scrape a real practice website made for learning: https://books.toscrape.com
# It allows scraping. Always check a site's rules before scraping it.
import csv
import time
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (student learning project)"}

def get_page(url):
    """Download a page and return a BeautifulSoup object (or None)."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()            # error for 404, 500 ...
        response.encoding = "utf-8"
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as error:
        print("Could not download:", error)
        return None

def extract_books(soup):
    """Return a list of dictionaries: title, price, rating."""
    books = []
    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]
        price = item.select_one("p.price_color").text
        rating = item.select_one("p.star-rating")["class"][1]   # e.g. "Three"
        books.append({"title": title, "price": price, "rating": rating})
    return books

if __name__ == "__main__":
    soup = get_page(URL)
    if soup:
        books = extract_books(soup)
        print("Books found:", len(books))
        for b in books[:5]:
            print(b)
        # save to CSV for analysis later (pandas in Session 12)
        with open("books.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "price", "rating"])
            writer.writeheader()
            writer.writerows(books)
        print("Saved books.csv")
        time.sleep(1)    # be polite: pause between requests if you fetch more pages
