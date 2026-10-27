# excel_files.py
# Writing and reading Excel (.xlsx) files with pandas.
# Needs:  pip install openpyxl

import pandas as pd

# 1) Two small tables
staff = pd.DataFrame({
    "name": ["Kamran", "Rabia", "Junaid"],
    "department": ["IT", "HR", "IT"],
    "salary": [120000, 95000, 135000],
})
leaves = pd.DataFrame({"name": ["Kamran", "Rabia"], "days": [3, 5]})

# 2) Write both tables into ONE workbook, each on its own sheet
with pd.ExcelWriter("office.xlsx") as writer:
    staff.to_excel(writer, sheet_name="Staff", index=False)
    leaves.to_excel(writer, sheet_name="Leaves", index=False)
print("office.xlsx written with 2 sheets")

# 3) Read one sheet back
staff_back = pd.read_excel("office.xlsx", sheet_name="Staff")
print("\nStaff sheet:\n", staff_back)

# 4) Read ALL sheets: you get a dictionary {sheet name: DataFrame}
all_sheets = pd.read_excel("office.xlsx", sheet_name=None)
print("\nSheet names:", list(all_sheets.keys()))
print("Leaves sheet:\n", all_sheets["Leaves"])
