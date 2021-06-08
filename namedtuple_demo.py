import csv
import os.path

data = open(os.path.join('data', 'randomnames.csv'), 'r')
names = [n for n in csv.reader(data)]
people_raw_tuple = [t for t in map(tuple, names)]
person_raw_tuple = people_raw_tuple[0]
print(person_raw_tuple)
