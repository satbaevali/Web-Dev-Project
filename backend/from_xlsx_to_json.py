"""
Note: If you have any

Instructions:
1. (IF YOU DON'T HAVE IT) INSTALL openpuxl IN CMD/TERMINAL "pip install openpyxl"
2. PLACE EXCEL DATABASE AS "database.xlsx" IN THE SAME FOLDER AS THIS SCRIPT
3. RUN THE FILE
"""

from openpyxl import load_workbook  # install openpyxl with pip
import json

structure = [
    {
        "name": "",
        "author": "",
        "record_id": 0,
        "imprint": "",
        "description": "",
        "series": "series",
        "subjects": [],
        "class": "",
        "isbn": 0,
        "bib_type": "",
        "gmd": "",
        "notes": "",
        "abstract": "",
        "entered": "",
        "updated": "",
        "url": "",
        "other_titles": [],
        "additional_isbns": []
    }
]
REPLACERS = {
    "Title:": "title",
    "Other Titles:": "other_titles",
    "Author:": "author",
    "Record ID": "record_id",
    "Record ID:": "record_id",
    "Edition:": "edition",
    "Description:": "description",
    "Imprint:": "imprint",
    "ISBN:": "isbn",
    "Additional ISBNs:": "additional_isbns",
    "Related URLs:": "related_urls",
    "Subjects:": "subjects",
    "URL:": "url",
    "Series:": "series",
    "Class:": "class",
    "Bib Type:": "bib_type",
    "GMD:": "gmd",
    "Abstract:": "abstract",
    "Notes:": "notes",
    "Entered:": "entered",
    "Updated:": "updated",
}

adapted = []
complete = []

# Opening worksheet, saving each non-empty entry as a list of cells
wb = load_workbook("database.xlsx", read_only=True)
worksheet = wb["Full Resources"]
for row in worksheet.rows:
    values = []
    for cell in row:
        if cell.value is not None:
            if cell.value == "":
                values.append(None)
            else:
                values.append(cell.value)
    if values:
        adapted.append(values)

# Saving list of lists (that represent cells) to a .txt file
adapted.pop(0)
with open("database_line_by_line.txt", "w", encoding="utf-8") as f:
    for row in adapted:
        f.write(f"{row}\n")

# Creating list of dictionaries built from the list of lists
current_book = None
dict_data = {}

for entry in adapted:
    if len(entry) == 1:
        if current_book is not None:
            if current_book.endswith("/"):
                dict_data["title"] = current_book[:-2]
            else:
                dict_data["title"] = current_book
            complete.append(dict_data)
            dict_data = {}
        current_book = entry[0]
    else:
        key = REPLACERS[entry[0]]
        match key:
            case "other_titles" | "subjects" | "additional_isbns" | "related_urls" | "author" | "series":
                dict_data[key] = [x.strip() for x in entry[1].splitlines()]
            case _:
                if entry[1] is not None:
                    dict_data[key] = entry[1].strip()
                else:
                    dict_data[key] = entry[1]

# Saving dictionary to file
with open("database.json", "w", encoding="utf-8") as f:
    json.dump(complete, f, indent=4)
