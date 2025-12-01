import csv

def load_texts(filename):
    id_to_rows = {}
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            if not row or not row[0].startswith("haiku_"):
                continue
            id_ = row[0].replace("haiku_", "")
            text_rows = row[1:]
            id_to_rows[id_] = text_rows
    return id_to_rows

def load_titles(filename):
    id_to_title = {}
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            id_ = row[0]
            title_str = " ".join(row[1:]).strip()
            id_to_title[id_] = title_str
    return id_to_title

def print_md_table(texts, titles):
    for id_, haiku_rows in texts.items():
        title = titles.get(id_, f"Unknown ({id_})")
        # Escape html entities if needed
        haiku_md = "<br>".join(haiku_rows)
        print("<p align=\"center\">\n")
        print(f"| **{title}** |")
        print("|:--:|")
        print(f"| {haiku_md} |\n")
        print("</p>\n")
        print("---\n")
        
if __name__ == "__main__":
    texts = load_texts('text/w_texts.txt')
    titles = load_titles('text/w_titles.txt')
    print_md_table(texts, titles)
