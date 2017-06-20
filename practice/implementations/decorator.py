"""
Задача:
Сделать пицерию.

В меню пицерии различные пиццы. Пиццы создаются комбинациями различных компонентов.

Тесто:
- пышное
- тонкое

Добавки:
- мясо
- помидоры
- сыр

Соусы:
- кетчуп
- майонез

"""

#Применим decorator

class Pizzeria:
	pass

class Component:
	
	def get_description(self):
		return self.__class__.name

	def get_cost(self):
		return self.__class__.cost

class ThinPizza(Component):
	cost = 0.75
	name = 'Thin pizza'

class CrustyPizza(Component):
	cost = 1
	name = 'Crusty pizza'

class Decorator(Component):
	def __init__(self, component):
		self.__component = component

	def get_cost(self):
		return self.cost + self.__component.get_cost()

	def get_description(self):
		return self.name +' + ' + self.__component.get_description()

class Meat(Decorator):
	cost = 0.5
	name = 'Meat'

class Ketchup(Decorator):
	cost = 0.1
	name = 'Ketchup'

class Mayo(Decorator):
	cost = 0.1
	name = 'Mayo'

class PremadeMeatKetchupThinPizza(Component):
	cost = 1.35
	name = 'Meat + Ketchup + Thin pizza'

pizza = Mayo(PremadeMeatKetchupThinPizza())