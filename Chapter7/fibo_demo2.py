import functools
from time import perf_counter

from clockdeco import clock

cnt = 0
@functools.lru_cache()
@clock
def fibonacci(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    t0 = perf_counter()
    print(fibonacci(10))
    print('counter =',cnt)
    print('time elapsed =',perf_counter() - t0)