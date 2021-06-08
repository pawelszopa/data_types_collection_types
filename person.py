class Person:
    first_name: str
    last_name: str

    #     implementacja problematyczna, jesli pole bedzie mutable to hash funkcja sie wywali
    def __hash__(self):
        to_hash = self.last_name
        return hash(to_hash)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{type(self).__name__}(first_name={self.first_name}, last_name={self.last_name}), hash={hash(self)}'

    def __eq__(self, value):
        return hash(self) == hash(value) and type(self) == type(value)
        # return type(self) == type(value) and self.first_name == value.first_name and self.last_name == value.last_name


def is_person_in_dict(first_name: str, last_name: str, the_dictionary: dict):
    return Person(first_name, last_name) in the_dictionary
