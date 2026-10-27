# lab3_scrape_quotes.py
# Practice: web scraping + regex + CSV (Sessions 06, 07, 09)
# https://quotes.toscrape.com is a practice site made for scraping.
import csv
import re
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
except requests.RequestException as error:
    print("Download failed:", error)
else:
    soup = BeautifulSoup(response.text, "html.parser")
    rows = []
    for q in soup.select("div.quote"):
        text = q.select_one("span.text").get_text(strip=True)
        author = q.select_one("small.author").get_text(strip=True)
        tags = [t.text for t in q.select("a.tag")]
        word_count = len(re.findall(r"\w+", text))      # tokenize with regex
        rows.append({"author": author, "words": word_count, "tags": ";".join(tags), "quote": text})

    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["author", "words", "tags", "quote"])
        writer.writeheader()
        writer.writerows(rows)

    print("Quotes saved:", len(rows))
    shortest = min(rows, key=lambda r: r["words"])
    print("Shortest quote:", shortest["quote"], "-", shortest["author"])
