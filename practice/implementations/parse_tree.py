"""

Parse tree to parse math expressions, based on binary trees.

If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
If the current token is a number, set the root value of the current node to the number and return to the parent.
If the current token is a ')', go to the parent of the current node.

"""
import operator
from binary_tree import BinaryTree

class ParseTree:
    def __init__(self):
        self.root = None

    def parse_expression(self, expr):
        tokens = list(expr)

        self.root = BinaryTree('n/a')
        parent_stack = []

        node = self.root
        parent_stack.append(node)
        for token in tokens:
            print(token)
            print('parent node:', parent_stack[0] if len(parent_stack) > 0 else '')
            print('current node:', node)
            if token == '(':
                
                node.insert_left('n/a')
                parent_stack.append(node)
                print(node, parent_stack)
                node = node.left_child 
            elif token == ')':
                parent = parent_stack.pop()
                node = parent
            elif token in ['+', '-', '/', '*']:
                node.cargo = token
                node.insert_right('n/a')
                parent_stack.append(node)
                node = node.right_child
            else:
                node.cargo = int(token)
                parent = parent_stack.pop()
                node = parent
            print('current node now:', node)

    def evaluate(self, tree):
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

        left_child = tree.left_child
        right_child = tree.right_child

        cargo = tree.cargo

        if left_child and right_child:
            return opers[cargo](self.evaluate(left_child), self.evaluate(right_child))
        else:
            return cargo
        
    def printexp(self, tree): #inorder
        sVal = ""
        if tree:
            sVal = '(' + self.printexp(tree.left_child)
            sVal = sVal + str(tree.cargo)
            sVal = sVal + self.printexp(tree.right_child)+')'
        return sVal

parse_tree = ParseTree()

expression = '(0+(4*5))'
parse_tree.parse_expression(expression)

print(parse_tree.evaluate(parse_tree.root))

print(parse_tree.printexp(parse_tree.root))