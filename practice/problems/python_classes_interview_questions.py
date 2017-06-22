"""
Написать базовый класс Observable, который бы позволял наследникам:

при передаче **kwargs заносить соответствующие значения как атрибуты
сделать так, чтобы при print отображались все публичные атрибуты
>>> class X(Observable):
...     pass
>>> x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
>>> print x
X(bar=5, foo=1, name='Amok', props=('One', 'two'))
>>> x.foo
1
>>> x.name
'Amok'
>>> x._bazz
12
"""

class Observable(object):
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def __repr__(self):
        atribs = [(atrib,  self.__dict__[atrib]) for atrib in self.__dict__.keys() if not '_' == atrib[0]]
        atrib_strs = []
        for atrib, val in atribs:
            atrib_strs.append('{}={}'.format(atrib, repr(val)))

        out_str = '{}({})'.format(self.__class__.__name__, ', '.join(atrib_strs))
        return out_str

class X(Observable):
    pass

x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))

"""
Написать класс, который бы по всем внешним признакам был бы словарем, но позволял обращаться к ключам как к атрибутам.

>>> x = DictAttr([('one', 1), ('two', 2), ('three', 3)])
>>> x
{ 'one': 1, 'three': 3, 'two': 2}
>>> x['three']
3
>>> x.get('one')
1
>>> x.get('five', 'missing')
'missing'
>>> x.one
1
>>> x.five
Traceback (most recent call last):
  ...
AttributeError

"""

class DictAttr(dict):
    
    def __getattr__(self, attr):
        return self[attr]

x = DictAttr([('one', 1), ('two', 2), ('three', 3)])
# print(x)
# print(x['three'])
# print(x.get('one'))
# print(x.one)
# print(x.five)


"""
Пункт 2 с усложнением: написать родительский класс XDictAttr так, чтобы у наследника динамически определялся ключ по наличию метода get_<KEY>.

>>> class X(XDictAttr):
...     def get_foo(self):
...         return 5
...     def get_bar(self):
...         return 12


>>> x = X({'one': 1, 'two': 2, 'three': 3})
>>> x
X: { 'one': 1, 'three': 3, 'two': 2}
>>> x['one']
1
>>> x.three
3
>>> x.bar
12
>>> x['foo']
5
>>> x.get('foo', 'missing')
5
>>> x.get('bzz', 'missing')
'missing'

"""

class XDictAttr(dict):

    def get(self, attr, default=None):
        #return super().get(attr, default)
        try:
            item = self.__getitem__(attr)
        except KeyError:
            item = None

        if item is None:
            return default
        return item

    def __getitem__(self, attr):
        try:
            dict_get = super().__getitem__(attr)
            return dict_get
        except KeyError:
            if 'get_{}'.format(attr) in dir(self):
                return getattr(self, 'get_{}'.format(attr))()
            raise

    def __getattr__(self, attr):
        if self[attr]:
            return self[attr]
            


class X(XDictAttr):
    def get_foo(self):
        return 5
    def get_bar(self):
        return 12

x = X({'one': 1, 'two': 2, 'three': 3})
print(x)
print(x['one'])
print(x.bar)
print(x['foo'])
print(x.get('foo', 'missing'))
print(x.get('bzz', 'missing'))

"""
Написать класс, который регистрирует свои экземпляры и предоставляет интерфейс итератора по ним

>>> x = Reg()
>>> x
<Reg instance at 0x98b6ecc>
>>> y = Reg()
>>> y
<Reg instance at 0x98b6fec>
>>> z = Reg()
<Reg instance at 0x98ba02c>
>>> for i in Reg:
...     print i
<Reg instance at 0x98b6ecc>
<Reg instance at 0x98b6fec>
<Reg instance at 0x98ba02c>


"""

class RegBase(type):
    def __iter__(self):
        return self.classiter()

class Reg(metaclass=RegBase):
    __current = 0
    __instances = []

    def __init__(self):
        self.__instances.append(self)

    def __del__(self):
        self.__instances.remove(self)

    @classmethod
    def classiter(cls):
        return iter(cls.__instances)


x = Reg()
y = Reg()
z = Reg()

for i in Reg:
    print(i)