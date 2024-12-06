#!/biin/python3

import sys

filename = sys.argv[1]


import datetime

def getdate(s):
    today = datetime.datetime.today()
    month = today.month
    year = today.year
    try:
        if float(s) > 6 and month < 6:
            year -= 1
        [month, day] = s.split(".")
        return datetime.datetime(year, int(month), int(day)).strftime("%F")
    except:
        return ""


with open(filename, 'r', encoding='utf-8') as file:
    raw = file.read()


import bs4

cooked = bs4.BeautifulSoup(raw, 'html.parser')
tables = cooked.find_all('table')

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['td'])
        if len(cells) >= 3:
            cell_content = cells[2].string
            if cell_content and (date := getdate(cell_content)):
                url = "https://nik-nul.github.io/news/" + date
                new_a = cooked.new_tag('a', href=url)
                new_a.string = cell_content
                cells[2].clear()
                cells[2].append(new_a)


with open(filename, 'w', encoding='utf-8') as file:
    file.write(str(cooked))