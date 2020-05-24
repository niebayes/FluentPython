'''
>>> with looking_glass() as what:
...     print('apple', 'banana')
...     print(what)
elppa ananab
54321
>>> what
'12345'
'''


import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield '12345'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
