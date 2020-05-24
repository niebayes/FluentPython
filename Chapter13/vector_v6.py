'''
# ! Refactored __eq__()
# ! Add a set of unary operator and comparison operator

Unary operator tests::

    >>> v1 = Vector([3, 4])
    >>> abs(v1)
    5.0
    >>> -v1
    Vector([-3.0, -4.0])
    >>> +v1
    Vector([3.0, 4.0])


Basic tests of operator ``+``::

    >>> v1 = Vector([3, 4, 5])
    >>> v2 = Vector([6, 7, 8])
    >>> v1 + v2
    Vector([9.0, 11.0, 13.0])
    >>> v1 + v2 == Vector([3+6, 4+7, 5+8])
    True
    >>> v3 = Vector([1, 2])
    >>> v1 + v3  # short vectors are filled with 0.0 on addition
    Vector([4.0, 6.0, 5.0])


Tests of ``+`` with mixed types::

    >>> v1 + (10, 20, 30)
    Vector([13.0, 24.0, 35.0])
    >>> from vector2d_v3 import Vector2d
    >>> v2d = Vector2d(1, 2)
    >>> v1 + v2d
    Vector([4.0, 6.0, 5.0])


Tests of ``+`` with mixed types, swapped operands::

    >>> (10, 20, 30) + v1
    Vector([13.0, 24.0, 35.0])
    >>> from vector2d_v3 import Vector2d
    >>> v2d = Vector2d(1, 2)
    >>> v2d + v1
    Vector([4.0, 6.0, 5.0])


Tests of ``+`` with an unsuitable operand:

    >>> v1 + 1
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'Vector' and 'int'
    >>> v1 + 'ABC'
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'Vector' and 'str'


Basic tests of operator ``*``::

    >>> v1 = Vector([1, 2, 3])
    >>> v1 * 10
    Vector([10.0, 20.0, 30.0])
    >>> 10 * v1
    Vector([10.0, 20.0, 30.0])


Tests of ``*`` with unusual but valid operands::

    >>> v1 * True
    Vector([1.0, 2.0, 3.0])
    >>> from fractions import Fraction
    >>> v1 * Fraction(1, 3)  # doctest:+ELLIPSIS
    Vector([0.3333..., 0.6666..., 1.0])


Tests of ``*`` with unsuitable operands::

    >>> v1 * (1, 2)
    Traceback (most recent call last):
      ...
    TypeError: can't multiply sequence by non-int of type 'Vector'


Tests of operator `==`::

    >>> va = Vector(range(1, 4))
    >>> vb = Vector([1.0, 2.0, 3.0])
    >>> va == vb
    True
    >>> vc = Vector([1, 2])
    >>> from vector2d_v3 import Vector2d
    >>> v2d = Vector2d(1, 2)
    >>> vc == v2d
    True
    >>> va == (1, 2, 3)
    False


Tests of operator `!=`::

    >>> va != vb
    False
    >>> vc != v2d
    False
    >>> va != (1, 2, 3)
    True
'''


from array import array
import math
import reprlib
import numbers
import functools
import operator
import itertools


class Vector:
    typecode = 'd'

    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})' .format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self._components)))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) 
                    and all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a


    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)
    
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
