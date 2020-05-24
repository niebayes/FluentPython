'''
>>> manager = LookingGlass()
>>> manager
<mirror.LookingGlass object at ...>
>>> monster = manager.__enter__()
>>> monster == '12345'
eurT
>>> monster
'54321'
>>> manager
>... ta tcejbo ssalGgnikooL.rorrim<
>>> manager.__exit__(None, None, None)
>>> monster
'12345'
'''


class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return '12345'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True
