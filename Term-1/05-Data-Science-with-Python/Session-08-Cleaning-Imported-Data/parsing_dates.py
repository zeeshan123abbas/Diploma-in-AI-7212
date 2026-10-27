# parsing_dates.py
# Turning text into real dates so we can calculate with them.

import pandas as pd

# 1) Dates stored as text in different styles
orders = pd.DataFrame({
    "order": ["A1", "A2", "A3", "A4"],
    "date_text": ["2026-03-05", "05/03/2026", "March 7, 2026", "2026.03.09"],
})

# 2) Try a list of known formats, one after another, for each text value
#    (%Y = 4-digit year, %m = month number, %d = day, %B = full month name)
known_formats = ["%Y-%m-%d", "%d/%m/%Y", "%B %d, %Y", "%Y.%m.%d"]

def parse_date(text):
    for fmt in known_formats:
        try:
            return pd.to_datetime(text, format=fmt)   # works -> return the date
        except ValueError:
            pass                                      # wrong format -> try the next one
    return pd.NaT                                     # nothing matched -> missing date

orders["date"] = orders["date_text"].apply(parse_date)
print(orders, "\n")
print("Type now:", orders["date"].dtype)

# 3) A single known format: say it exactly with format=
text = pd.Series(["15-01-2026", "28-02-2026"])
dates = pd.to_datetime(text, format="%d-%m-%Y")     # %d day, %m month, %Y 4-digit year
print("\nParsed with format:", dates.dt.date.tolist())

# 4) Bad dates become NaT (Not a Time) instead of crashing
bad = pd.to_datetime(pd.Series(["2026-01-10", "not a date"]), errors="coerce")
print("With a bad value:", bad.tolist())

# 5) Now we can do date maths
orders["weekday"] = orders["date"].dt.day_name()
orders["days_since_first"] = (orders["date"] - orders["date"].min()).dt.days
print("\n", orders[["order", "date", "weekday", "days_since_first"]])
