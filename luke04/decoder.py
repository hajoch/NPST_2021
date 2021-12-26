import re
import csv
import numpy as np

file = open('verksted_npst.txt')
reader = csv.reader(file, delimiter=";")
rows = []
for row in reader:
    row[0] = str(row[0]).strip()
    rows.append(row)
del rows[0]

rows.sort(key = lambda rows:rows[2])

result = ''
for row in rows:
    hex_rep = int(row[1], 16)
    result += chr(hex_rep)

pattern = r'[^0-9a-zA-Z{}]'
result = re.sub(pattern, '', result)

print(result)
