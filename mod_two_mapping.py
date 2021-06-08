from collections.abc import MutableMapping


class ModTwoMapping(MutableMapping):
    _mapping: dict = {}

    @staticmethod
    def _validate_value(value):
        if value % 2 != 0:
            raise ValueError

    def __delitem__(self, key):
        del self._mapping[key]

    def __getitem__(self, key):
        return self._mapping[key]

    def __setitem__(self, key, value):
        self._validate_value(value)
        self._mapping[key] = value

    def __len__(self):
        return len(self._mapping)

    def __iter__(self):
        return iter(self._mapping)

    def __repr__(self):
        return repr(self._mapping)


