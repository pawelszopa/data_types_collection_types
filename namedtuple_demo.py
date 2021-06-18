import csv
import inspect
import os.path
from collections import namedtuple
from collections.abc import Sequence
from typing import NamedTuple

data = open(os.path.join('data', 'randomnames.csv'), 'r')
names = [n for n in csv.reader(data)]
people_raw_tuple = [t for t in map(tuple, names)]
person_raw_tuple = people_raw_tuple[0]
# print(person_raw_tuple)
# print(person_raw_tuple.__class__.__mro__)
# print(inspect.getmro(type(person_raw_tuple)))

# print(isinstance(person_raw_tuple, Sequence))

Person = namedtuple('Person', 'first_name last_name')
# print(inspect.getmro(Person))
person_named_tuple = Person("John", 'Smiths')
# print(person_named_tuple.first_name)
# print(person_named_tuple.last_name)

# print(isinstance(person_named_tuple, Sequence))
# print(person_named_tuple[0])
# print(len(person_named_tuple))
# print(person_named_tuple)

# people_named_tuple = [Person(name[0].split()[0], name[0].split()[1]) for name in names]
# person_named_tuple = people_named_tuple[0]
# print(person_named_tuple)


# print(person_named_tuple == person_raw_tuple)

class NamedTuplePerson(NamedTuple):
    first_name: str
    last_name: str

tpl = ('John', "Smiths")
person_typing_named_tuple = NamedTuplePerson("John", "Smiths")
print(person_typing_named_tuple)

print(person_typing_named_tuple == person_named_tuple)
print(person_typing_named_tuple == tpl)
print(person_named_tuple == tpl)
