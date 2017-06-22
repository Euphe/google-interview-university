"""
Реализовать дескрипторы, которые бы фиксировали тип атрибута

>>> class Image(object):
...     height = Property(0)
...     width = Property(0)
...     path = Property('/tmp/')
...     size = Property(0)


>>> img = Image()
>>> img.height = 340
>>> img.height
340
>>> img.path = '/tmp/x00.jpeg'
>>> img.path
'/tmp/x00.jpeg'
>>> img.path = 320
Traceback (most recent call last):
  ...
TypeError
"""

class Property(object):

    def __init__(self, value):
        self._type = type(value)
        self._value = value

    def __get__(self, instance, owner=None):
        return self._value

    def __set__(self, instance, val):
        if self._type != type(val):
            raise(TypeError())
        
        self._value = val


    def __delete__(self, instance):
        super().__delete__(self, instance)

class Image(object):
    height = Property(0)
    width = Property(0)
    path = Property('/tmp/')
    size = Property(0)

# img = Image()
# img.height = 340
# print(img.height)
# img.path = '/tmp/anewpath'
# print(img.path)
# img.path = 320

"""

Реализовать базовый класс (используя метакласс), который бы фиксировал тип атрибута

>>> class Image(Object):
...     height = 0
...     width = 0
...     path = '/tmp'
...     size = 0

>>> img = Image()
>>> img.height = 340
>>> img.height
340
>>> img.path = '/tmp/x00.jpeg'
>>> img.path
'/tmp/x00.jpeg'
>>> img.path = 320
Traceback (most recent call last):
  ...
TypeError

"""

class StrictMeta(type):

    def __new__(meta, name, bases, dict_):
        for key, val in dict_.items():
            if not key.startswith('_') and not hasattr(val, '__call__'):
                dict_[key] = Property(val)
        print(dict_)
        return type.__new__(meta, name, bases, dict_)
        
class Image(metaclass=StrictMeta):
    height = 0
    width = 0
    path = '/tmp/'
    size = 0

img = Image
img.height = 340
print(img.height)
img.path = '/tmp/anewpath'
print(img.path)
img.path = 320

"""
I have no idea, havent solved
"""
