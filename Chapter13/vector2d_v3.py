from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x , self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})' .format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)

    def angle(self):
        return math.atan2(self.y, self.x)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2))

    print(v1.__dict__)
    print(v1._Vector2d__x)

    try:
        v1.x = 2.              # Error
        print(v1)
    except:
        print('Oops! An error occurred')
    v1.__x = 2.            # Doesn't change
    print(v1)
    v1._Vector2d__x = 2.   # changed
    print(v1)