# Collection Types

## Sequence Type

A collection where contained objects are retrievable by their index. The object can report the number of contained
objects

### Examples

- tuple
- list
- string
- range
- bytes
- bytearray
- memoryview
  **** accessible inside python standard lib

### 2 types of

inheritance abc class

### Abstract base classes

- abc.Sequence
    - tuple
    - str
    - range
    - memoryview
    - abc.MutableSequence
        - list
        - bytearray
    - abc.ByteString
        - bytes
        - bytearray

### Additional sequence types:

1. namedtuple (factory function)
    - function not a type
    - pass type name and attribute names
    - type returned is a tuple with attributes
    - useful for importing/exporting structured data 
        1.1 abc. Sequence <- typing.NamedTuple 
        - enables typical class syntax if used NamedTuple
        - wraps call to factory function
        - explicit syntax for type hints and defaults
        - can add methods
        - can add docstrings
        - useful for tooling
        - inheritable

NamedTuple | Dataclass
:---:|:---:
Immutable/hashable by default | frozen=True to be immutable
Easy load/save structured data | Only creates init method
Implicit equal - Can compare to  raw tuple | enforces type equality
Sortable | Need to implement sorting methods
Iterable over attributes | Convert to iterate (asdict/astuple)
Inheritable| Inheritable

---

## Mapping Type

A collection where contained objects are stored with and retrieved via a key

### Abstract base classes

- abc.Mapping
    - abc.MutableMapping
        - dict

### Key in dict

- Hashable - The keys are stored in a hash table for quick value retrieval
- Immutable - If the key isn't immutable retrieval problematic

### Additional mapping types:

- dziedziczy po dict a dict po mutable mapping

1. defaultdict - jezli chcemy pobrac po kluczu a klucza nie ma i dict wali bledem a deafultdict nie
    - single default value type
    - you provide type/function
    - if key doesn't exist, function called
    - no KeyError
    - useful when aggregating data

2. dict <- Counter
    - value for each key is always an int
    - automatically creates count from sequence
    - most_common is significant
    - sorted by default (but there are quirks)
    - iterator po counterze dziala jak w dict wiec kolejnosc dodawania ma znaczenia
    - jesli chcemy iterowac po counterze wedle __repr__(posortowanego) to musimy dac .most_common()

3. dict <- OrderedDict
    - keeps keys in the order they are added
    - sorted useful when creating from collection
    - doesn't keep sorted order when adding new
    - new imtes always added at the end
    - does keep orded when deleting

---

## Hashing

Converting the value of an object of unknown size to a value of a fixed, immutable size.

1. `__hash__`
2. hash(obj)

### Built-in immutable types:

- hashable
- can be used as keys in mapping types
- can be added to set

## Custom Classes

- hashable by default
- value of id(obj) is the default implementation
- default might be problematic

```python
class Person:
    first_name: str
    last_name: str

    def __hash__(self):
        return id(self)


class CustomPerson:
    first_name: str
    last_name: str

    #     implementacja problematyczna, jesli pole bedzie mutable to hash funkcja sie wywali
    def __hash__(self):
        to_hash = (self.first_name, self.last_name)
        return hash(to_hash)
```

hash table

hash|value
---|---
222|'a'
321|'b'
222 + algorithm|'c'


## Deque - kolejka - first in first out
    - abc.Sequence <- abc.MutableSequence <- deque
    - "Double ended queue" - kolejka z dwoma zakonczeniami
    - can be use as a queue and/or stack!
    - can add elements or remove from both 'ends'
    - can limit number of items (maxlen)
    - 