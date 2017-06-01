class HungerMeter(object): #a descriptor for hunger
	def __init__(self):
		self._hunger = 0

	def __get__(self, instance, owner):
		return instance._hunger

	def __set__(self, instance, hunger):
		if hunger < 0:
			hunger = 0
		if hunger > 10:
			hunger = 10

		if hunger >= 9:
			print('{}: Urgently hungry!'.format(instance.name))
		elif hunger >= 6:
			print('{}: Quite hungry!'.format(instance.name))
		elif hunger >= 3:
			print('{}: Slightly hungry'.format(instance.name))
		elif hunger == 0:
			print('{}: Hunger completely sated'.format(instance.name))

		instance._hunger = hunger

	def __delete__(self, instance):
		super().__delete__(self, instance)


class Colonist: #A person settling on an alien planet. Can do actions, get hungry, then eat.
	hunger = HungerMeter()
	def __init__(self, name):
		self.name = name
		self._hunger = 0 

	def do_action(self):
		self.hunger += 1

	def eat(self):
		self.hunger = 0

andrew = Colonist('Andrew')

andrew.do_action()
andrew.do_action()
andrew.do_action()

print(andrew.hunger)

bradley = Colonist('Bradley')
bradley.do_action()
bradley.do_action()
bradley.do_action()
bradley.do_action()
bradley.do_action()
bradley.do_action()

print(bradley.hunger)

andrew.eat()
bradley.eat()

