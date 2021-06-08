import csv

import os
import random
from collections import Counter, OrderedDict

from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    first_name: str
    last_name: str


def load_people():
    people = []
    with open(os.path.join('data', 'randomnames.csv'), 'r') as names:
        names_reader = csv.reader(names, delimiter=' ')
        for row in names_reader:
            people.append(Person(row[0], row[1]))

    return people


def simulate_game(people):
    for p in people:
        people[p] += random.randint(1, 100)
    return



people = load_people()
# print(people)
game = Counter({person: 0 for person in people})
# print(game)
simulate_game(game)
# print(game.most_common(10))

top_ten = game.most_common(10)
by_name = OrderedDict(sorted(top_ten, key=lambda x:x[0].first_name))
print(by_name)