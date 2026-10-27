# character_encoding.py
# Text is stored as bytes. The ENCODING is the rule that maps bytes to letters.

import pandas as pd

# 1) Encode and decode a string with Urdu text
text = "Café - کراچی"
as_bytes = text.encode("utf-8")
print("Text:", text)
print("UTF-8 bytes:", as_bytes)
print("Number of characters:", len(text), " Number of bytes:", len(as_bytes))
print("Decoded back:", as_bytes.decode("utf-8"))

# 2) Decoding with the WRONG encoding gives garbage (called "mojibake")
print("Wrong decoding:", as_bytes.decode("latin-1"))

# 3) Save a CSV in an older encoding (cp1252 is common for files from old Windows/Excel)
df = pd.DataFrame({"product": ["Café latte", "Crème brûlée"], "price": [450, 600]})
df.to_csv("menu_cp1252.csv", index=False, encoding="cp1252")

# 4) Reading it as UTF-8 fails...
try:
    pd.read_csv("menu_cp1252.csv", encoding="utf-8")
except UnicodeDecodeError as error:
    print("\nUTF-8 failed:", str(error)[:60], "...")

# 5) ...but reading with the correct encoding works
menu = pd.read_csv("menu_cp1252.csv", encoding="cp1252")
print("Read with cp1252:\n", menu)

# 6) Best practice: save your own files as UTF-8
menu.to_csv("menu_utf8.csv", index=False, encoding="utf-8")
print("Saved menu_utf8.csv in UTF-8")
