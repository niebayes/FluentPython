'''
>>> s = Sentence('The time has come')
>>> s
Sentence('The time has come')
>>> for word in s:
...     print(word)
The
time
has
come
>>> list(s)
['The', 'time', 'has', 'come']
'''


import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
    