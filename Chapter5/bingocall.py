'''
>>> bingo = BingoCage(range(3))
>>> bingo()
>>> callable(bingo)
True
'''

import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(5))
print(bingo.pick())
print(bingo())