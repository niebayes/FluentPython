'''
>>> coro_avg = averager()
>>> next(coro_avg)
>>> coro_avg.send(10)
>>> coro_avg.send(30)
>>> coro_avg.send(5)
>>> coro_avg.send(None)
Traceback (most recent call last):
    ...
StopIteration: Result(count=3, average=15.0)

# Illustration for how to fetch returned value from yield
>>> coro_avg = averager()
>>> next(coro_avg)
>>> coro_avg.send(10)
>>> coro_avg.send(30)
>>> coro_avg.send(5)
>>> try:
...     coro_avg.send(None)
... except StopIteration as exc:
...     result = exc.value
>>> result
Result(count=3, average=15.0)
'''


from collections import namedtuple


Result = namedtuple('Result', ['count', 'average'])

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)
