"""
https://leetcode.com/problems/min-stack/#/description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""
import operator
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._list = []
        self.min_val = None
        self.min_pos = None

    def set_new_min(self):
        if len(self._list)>0:
            self.min_pos, self.min_val = min(enumerate(self._list), key=operator.itemgetter(1))

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._list.append(x)
        if self.min_val == None or x < self.min_val:
            self.min_val = x
            self.min_pos = len(self._list)-1


    def pop(self):
        """
        :rtype: void
        """
        popped = self._list.pop()
        if popped == self.min_val:
            self.set_new_min()
        return popped
        

    def top(self):
        """
        :rtype: int
        """ 
        if len(self._list) > 0:
            return self._list[len(self._list)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_pos != None:
            return self._list[self.min_pos]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack();
minStack.push(0);
minStack.push(-15);
minStack.push(-1);
minStack.push(10);
minStack.push(-1);
print(minStack.getMin())# -3
print(minStack.pop())# -3
print(minStack.top()) #     --> Returns 0.
print(minStack.getMin())#   --> Returns -2.