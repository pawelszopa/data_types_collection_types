import csv
import os
from collections import Counter

with open(os.path.join("data", 'Male_WorldCupPlayers.csv'), 'r', encoding='utf-8') as players:
    reader = csv.reader(players)
    next(reader)  # skip column names

    name_list = []
    for row in reader:
        name_list.append(row[6])

    a = Counter(name_list)
    top_ten = a.most_common(10)

    print(top_ten)