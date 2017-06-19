
"""
Пусть есть три типа мобильных девайсов - Iphone, Android, Windows mobile

Все девайсы имеют Bluetooth

Пусть bluetooth радио могут быть от одного из двух производителей - intel и broadcom

Пусть Intel радио имеют не такой интерфейс, как Broadcom радио.

Получаем

"""
class AbstractBluetoothRadio:
	pass

class BroadcomBluetooth(AbstractBluetoothRadio):
	pass

class IntelBluetooth(AbstractBluetoothRadio):
	pass


class AbstractMobileDevice:
	pass

class Android(AbstractMobileDevice):
	pass

class Iphone(AbstractMobileDevice):
	pass

class WindowsMobile(AbstractMobileDevice):
	pass

"""
Теперь введем операцию: включение bluetooth на мобильном девайсе.
Выглядеть будет примерно так:
def switch_bluetooth_on(MobileDevice, BluetoothRadio)

Как видно эта операция зависит от типа девайса и типа bluetooth радио. 

Получаем матрицу 3 x 2
			Android | Windows Mobile | iPhone
Intel    |    
Broadcom |

В каждой ячейке будет уникальная операция. Например "Intel на Android" или "Broadcom на iPhone"
Мы видим, что здесь необходим double dispatch. Каждая операция зависит от трех вещей: типа операции, класса bluetooth радио и класса мобильного устройства.

Double dispatch подсказывает, что здесь можно применить Visitor.
Visitor позволяет добавить новые виртуальные функции семейству классов не модифицируя сами классы, вместо этого создается visitor, который содержит реализацию всех специализаций виртуальной функции. Visitor получает на вход ссылку на инстанс, и реализует функционал через двойной вызов.

В данном случае виртуальная функция, которую мы хотим добавить - switch_bluetooth_on

Необходимо решить какая из иерархий классов (мобильные устройства или типы радио) является более "стабильной", то есть меньше подвержена изменениям.
Более стабильная иерархия станет "посещаемыми" классами, а менее стабильная станет "посетителями". 
Допустим иерархия устройств более стабильная. 

Так как AbstractMobileDevice становится "посещаемым" классом, метод switch_bluetooth_on является методом "accept", то есть методом отвечающим за прием посетителя.

"""

class AbstractMobileDevice:
	def switch_bluetooth_on(self, blue_tooth_visitor):
		pass

class Android(AbstractMobileDevice):
	def switch_bluetooth_on(self, blue_tooth_visitor):
		blue_tooth_visitor.switch_on(this)

class Iphone(AbstractMobileDevice):
	def switch_bluetooth_on(self, blue_tooth_visitor):
		blue_tooth_visitor.switch_on(this)

class WindowsMobile(AbstractMobileDevice):
	def switch_bluetooth_on(self, blue_tooth_visitor):
		blue_tooth_visitor.switch_on(this)

class AbstractBluetoothRadio:
	pass

class BroadcomBluetooth(AbstractBluetoothRadio):
	pass

class IntelBluetooth(AbstractBluetoothRadio):
	pass

"""
Кажется странным, что мы вызываем, казалось бы, один и тот же код в разных классах мобильных устройств. Однако на самом деле метод switch_on зависит как от класса BluetoothVisitor, так и от класса MobileDevice. Таким образом возможно сделать, что в каждом из трех случаев будет выполнен разный код.
Это нам и требуется - разные алгоритмы включения bluetooth в зависимости от устройства и bluetooth радио.

Теперь нам нужны посетители
"""
class AbstractBluetoothVisitor:
	def blue_tooth_visitor(device):
		pass

class IntelBluetoothVisitor(AbstractBluetoothVisitor):
	intel_radio = IntelBluetooth
	def blue_tooth_visitor(device):
		if type(device) == Android:
			print('Intel over android')
		elif type(device) == Iphone:
			print('Intel over iphone')
		elif type(device) == WindowsMobile:
			print('Intel over WM')


class BroadcomBluetoothVisitor(AbstractBluetoothVisitor):
	broadcom_radio = BroadcomBluetooth
	def blue_tooth_visitor(device):
		if type(device) == Android:
			print('Broadcom over android')
		elif type(device) == Iphone:
			print('Broadcom over iphone')
		elif type(device) == WindowsMobile:
			print('Broadcom over WM')


"""
Теперь операции (включение bluetooth) добавляются к устройствам без модификации классов.
В этом суть философии visitor - добавление операций без модификации классов.

Вопросы:
    Что будет если появится новый девайс?
    А если появится новый производитель блютуса?
    Когда этот паттерн нужно применять?
    Как выбрать какую иерархию классов сделать посетителем, а какую сделать посещаемой?

    Слабо написать другой пример использования Visitor?
"""
