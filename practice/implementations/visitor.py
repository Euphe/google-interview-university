# -*- coding: utf-8 -*-
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

class MobileDevice:
    pass

class Android(MobileDevice):
    pass

class iPhone(MobileDevice):
    pass

class WindowsMobile(MobileDevice):
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
Visitor позволяет добавить новые виртуальные функции семейству классов не модифицируя сами классы, вместо этого создается visitor, который содержит реализацию всех специализаций (частных случаев) виртуальной функции. Visitor получает на вход ссылку на инстанс, и реализует функционал через double dispatch (двойной вызов).

В данном случае виртуальная функция, которую мы хотим добавить - switch_bluetooth_on

Необходимо решить какая из иерархий классов (мобильные устройства или типы радио) является более "стабильной", то есть меньше подвержена изменениям.
Более стабильная иерархия станет "посещаемыми" классами, а менее стабильная станет "посетителями". 
Допустим иерархия устройств более стабильная. 

Так как MobileDevice становится "посещаемым" классом, метод switch_bluetooth_on является методом "accept", то есть методом отвечающим за прием посетителя.

"""

class MobileDevice:
    def switch_bluetooth_on(self, blue_tooth_visitor):
        blue_tooth_visitor.switch_on(self)

class Android(MobileDevice):
    pass

class iPhone(MobileDevice):
    pass

class WindowsMobile(MobileDevice):
    pass

class BluetoothRadio:
    pass

class BroadcomBluetooth(BluetoothRadio):
    pass

class IntelBluetooth(BluetoothRadio):
    pass

"""
Кажется странным, что мы вызываем, казалось бы, один и тот же код в разных классах мобильных устройств. Однако на самом деле метод switch_on зависит как от класса BluetoothVisitor, так и от класса MobileDevice. Таким образом возможно сделать, что в каждом из трех случаев будет выполнен разный код.
Это нам и требуется - разные алгоритмы включения bluetooth в зависимости от устройства и bluetooth радио.

Теперь нам нужны посетители
"""
class BluetoothVisitor:
    def switch_on(self, device):
        pass

class IntelBluetoothVisitor(BluetoothVisitor):
    intel_radio = IntelBluetooth
    def switch_on(self, device):
        if type(device) == Android:
            print('Intel over android')
        elif type(device) == iPhone:
            print('Intel over iPhone')
        elif type(device) == WindowsMobile:
            print('Intel over WM')


class BroadcomBluetoothVisitor(BluetoothVisitor):
    broadcom_radio = BroadcomBluetooth
    def switch_on(self, device):
        if type(device) == Android:
            print('Broadcom over android')
        elif type(device) == iPhone:
            print('Broadcom over iPhone')
        elif type(device) == WindowsMobile:
            print('Broadcom over WM')


"""
Теперь операции (включение bluetooth) добавляются к устройствам без модификации классов.
В этом суть философии visitor - добавление операций без модификации классов.
"""

iphone = iPhone()
broadcom_bluetooth = BroadcomBluetoothVisitor()
intel_bluetooth = IntelBluetoothVisitor()
iphone.switch_bluetooth_on(broadcom_bluetooth)
iphone.switch_bluetooth_on(intel_bluetooth)

"""
Вопросы:
    1. Что будет если появится новый девайс?
    2. А если появится новый производитель блютуса?
    3. Когда этот паттерн нужно применять?
    4. Как выбрать какую иерархию классов сделать посетителем, а какую сделать посещаемой?

    5. Слабо написать другой пример использования Visitor?
"""

"""
1. Добавим новый девайс.
Добавление нового девайса происходит во всех visitor. Получается при изменении посещаемой иерархии надо изменять всех посетителей.
Из-за этого предпочтительнее делать "посещаемой" ту иерархию, которая меняется реже
"""

class Blackberry(MobileDevice):
    pass

class IntelBluetoothVisitor(BluetoothVisitor):
    intel_radio = IntelBluetooth
    def switch_on(self, device):
        if type(device) == Android:
            print('Intel over android')
        elif type(device) == iPhone:
            print('Intel over iPhone')
        elif type(device) == WindowsMobile:
            print('Intel over WM')
        elif type(device) == Blackberry:
            print('Intel over blackberry')


class BroadcomBluetoothVisitor(BluetoothVisitor):
    broadcom_radio = BroadcomBluetooth
    def switch_on(self, device):
        if type(device) == Android:
            print('Broadcom over android')
        elif type(device) == iPhone:
            print('Broadcom over iPhone')
        elif type(device) == WindowsMobile:
            print('Broadcom over WM')
        elif type(device) == Blackberry:
            print('Broadcom over blackberry')

intel_bluetooth = IntelBluetoothVisitor()
device = Blackberry()
device.switch_bluetooth_on(intel_bluetooth)

"""
2. Добавим нового производителя радио.
Добавляем нового visitor. В данном случае мы изменяем только лишь одного (нового) посетителя. В нем мы должны покрыть все девайсы
"""

class SputnikBluetooth(BluetoothRadio):
    pass

class SputnikBluetoothVisitor(BluetoothVisitor):
    sputnik_radio = SputnikBluetooth
    def switch_on(self, device):
        if type(device) == Android:
            print('Sputnik over android')
        elif type(device) == iPhone:
            print('Sputnik over iPhone')
        elif type(device) == WindowsMobile:
            print('Sputnik over WM')
        elif type(device) == Blackberry:
            print('Sputnik over blackberry')

sputnik_radio = SputnikBluetoothVisitor()
device.switch_bluetooth_on(sputnik_radio)

"""
3. Когда этот паттерн нужно применять?

Этот паттерн нужно применять когда имеет место double dispatch - существует две иерархии классов и операция, которая зависит от классов объектов обоих иерархий.

4. Как выбрать какую иерархию классов сделать посетителем, а какую сделать посещаемой?

Ту, что изменяется чаще, сделать постетителем. Ту, что изменяется реже, сделать посещаемой.
Причина - при появлении нового посетителя нужно лишь написать код посетителя. При появлении нового посещаемого класса нужно изменить код всех постетителей.

"""

"""
5. Другой пример использования visitor


Пусть есть солдаты различных типов и оружие разных типов.

Выстрел солдата из оружия зависит от подготовки солдата и типа оружия.
Имеем double dispatch.

Посещаемым классом являются солдаты, а оружие является постетителем.
"""

class Shooter:
    def shoot(self, weapon):
        weapon.make_shot(self)

class Soldier(Shooter):
    pass

class Sniper(Shooter):
    pass

class Weapon:
    def make_shot(self, shooter):
        pass

class AssaultRifle(Weapon):
    def make_shot(self, shooter):
        if isinstance(shooter, Soldier):
            print('Soldier burst fires the assault rifle')
        elif isinstance(shooter, Sniper):
            print('Sniper fires a signle shot from the assault rifle')

class Pistol(Weapon):
    def make_shot(self, shooter):
        if isinstance(shooter, Soldier):
            print('Soldier fires the pistol')
        elif isinstance(shooter, Sniper):
            print('Sniper fires the pistol')
        

class SniperRifle(Weapon):
    def make_shot(self, shooter):
        if isinstance(shooter, Soldier):
            print('Soldier fires sniper rifle inaccurately')
        elif isinstance(shooter, Sniper):
            print('Sniper fires the sniper rifle')

#Shooting range
pistol = Pistol()
assault = AssaultRifle()
sniper_rifle = SniperRifle()

soldier = Soldier()
sniper = Sniper()

soldier.shoot(pistol)
soldier.shoot(assault)
soldier.shoot(sniper_rifle)

sniper.shoot(pistol)
sniper.shoot(assault)
sniper.shoot(sniper_rifle)


