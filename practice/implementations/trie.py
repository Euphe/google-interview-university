"""

Trie data structure implementation

"""

class TrieNode:
	def __init__(self, letter, terminal=False, children=None):
		self.letter =  letter
		self.children = children or {}
		self.terminal = terminal

	def get_words(self, path=[]):
		path = path + [self.letter]
		
		words = []
		if self.terminal:
			words.append(''.join(path))

		for child in self.children.values():
			words += child.get_words(path)

		return words

	def __str__(self):
		return self.letter

class Trie:
	def __init__(self, root_nodes=None):
		self.root_nodes = root_nodes or {}

	def insert(self, word):
		root = None
		letters = list(word)
		if not letters[0] in self.root_nodes.keys(): #check if root node exists for first letter of word
			self.root_nodes[letters[0]] = TrieNode(letters[0])
		root = self.root_nodes[letters[0]]

		#iterate over word letters
		curnode = root
		for i, letter in enumerate(list(word)):
			if i == 0:
				continue

			if not letter in curnode.children.keys():
				curnode.children[letter] = TrieNode(letter)

			curnode = curnode.children[letter]
		curnode.terminal = True

	def search(self, word):
		root = None
		letters = list(word)
		if not letters[0] in self.root_nodes.keys():
			return None

		root = self.root_nodes[letters[0]]
		#iterate over word letters
		curnode = root
		for i, letter in enumerate(list(word)):
			if i == 0:
				continue
			if not letter in curnode.children.keys():
				return None
			curnode = curnode.children[letter]

		return True

	def all_words_starting_with(self, pref):
		letters = list(pref)
		if not letters:
			words = []
			for node in self.root_nodes.values():
				words += node.get_words()
			return words

		if not letters[0] in self.root_nodes.keys():
			return []

		curnode = self.root_nodes[letters[0]]
		
		path = [letters[0]]

		words = []
		for i, letter in enumerate(list(pref)): #iterate over prefix letters and move down the tree
			if i == 0:
				continue
			if not letter in curnode.children.keys():
				return words
			curnode = curnode.children[letter]
			path.append(letter)
		print('curnode', str(curnode))
		
		words += curnode.get_words(path[:-1])
		print('prefix path', path)	
		return words


words = ['alpha', 'alz']

trie = Trie()

for word in words:
	trie.insert(word)

print(trie.all_words_starting_with('al'))
				



