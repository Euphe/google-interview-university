"""
Задача:
Имитировать файловую систему

Есть директории, которые могут содержать файлы и другие директории.

Применим composite. Файлы и директории должны иметь одинаковый интерфейс.
"""

class Composite:
	def open(self):
		raise(NotImplemented())

class File(Composite):
	def __init__(self, name, data):
		self.name = name
		self.data = data

	def open(self):
		print('File {} data: {}'.format(self.name, self.data))

class Directory(Composite):
	def __init__(self, name, children=None):
		self.name = name
		self.children = children or []

	def open(self):
		for child in self.children:
			child.open()

	def list(self):
		print('Dir {}'.format(self.name))
		for child in self.children:
			print('\t{}'.format(child.name))
class FSystem:
	def __init__(self):
		self.root = Directory('root')

	def traverse(self):
		directory = self.root
		while True:
			print('Use open "file" to open a file or directory')
			print('Use create "name" "data" to create a file')
			print('Use create "name" to create a directory')
			print('Use ls to list dir')
			inp = input('Command: ').split(' ')
			if inp:
				if 'open' == inp[0]:
					name = inp[1]
					for child in directory.children:
						if name == child.name:
							child.open()
							if isinstance(child, Directory):
								directory = child
				elif 'create' == inp[0]:
					name = inp[1]
					try:
						data = inp[2]
					except IndexError:
						data = None

					if data:
						#make file
						directory.children.append(File(name, data))
					else:
						new_dir = Directory(name)
						directory.children.append(new_dir)
				elif 'ls' == inp[0]:
					directory.list()
				else:
					print('Invalid input')

fsystem = FSystem()
fsystem.root.children.append(Directory('home'))
fsystem.root.children[0].children.append(File('afile1', 'afile1data'))
fsystem.root.children[0].children.append(File('afile2', 'afile2data'))
fsystem.traverse()