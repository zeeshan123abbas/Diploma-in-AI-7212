# pdf_files.py
# Writing a simple PDF and reading its text back.
# Needs:  pip install pypdf matplotlib

import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"] = 42      # store real text in the PDF (searchable)
import matplotlib.pyplot as plt
from pypdf import PdfReader

# ---------- PART 1: WRITE a one-page PDF report with Matplotlib ----------
lines = [
    "Monthly Sales Report",
    "Karachi: 520 orders",
    "Lahore: 410 orders",
    "Islamabad: 260 orders",
]
page = plt.figure(figsize=(8.27, 11.69))      # A4 size in inches
for i, text in enumerate(lines):
    size = 20 if i == 0 else 14               # bigger font for the title
    page.text(0.1, 0.9 - i * 0.05, text, fontsize=size)
page.savefig("report.pdf")
plt.close(page)
print("report.pdf written")

# ---------- PART 2: READ text from the PDF with pypdf ----------
reader = PdfReader("report.pdf")
print("Number of pages:", len(reader.pages))

first_page_text = reader.pages[0].extract_text()
print("\nText found on page 1:")
print(first_page_text)

# ---------- PART 3: use the text ----------
for line in first_page_text.splitlines():
    if "orders" in line:
        city, count = line.split(":")
        print(f"{city.strip()} has {count.strip()}")
