import csv
import os
from collections import defaultdict

with open(os.path.join("data", 'Male_WorldCupPlayers.csv'), 'r', encoding='utf-8') as players:
    reader = csv.reader(players)
    next(reader)  # skip column names

    name_list = []
    for row in reader:
        name_list.append((row[2], row[6]))

    players_by_country = defaultdict(list)
    for name in name_list:
        players_by_country[name[0]].append(name[1])

    print(players_by_country)
