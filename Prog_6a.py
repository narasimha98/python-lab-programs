#Create a class called MyStack which supports push, pop and display operations.
#   Implement the stack class using a list. Specify the upper bound of the size while creating the stack object.
#   Provide exception handling mechanism for stack overflow and stack underflow.

class StackFull(Exception) :
	def __init__(self) :
		self.msg = 'stack is full'
	def __str__(self) :
		return self.msg

class StackEmpty(Exception) :
	def __init__(self) :
		self.msg = 'stack is empty'
	def __str__(self) :
		return self.msg


class MyStack :
	# assumed that the size is not negative
	def __init__(self, size = 10) :
		self.mylist = [ ]
		self.size = size
	def push(self, elem) :
		l = len(self.mylist)
		if l < self.size :
			self.mylist.append(elem)
		else:
			raise StackFull()
	def pop(self) :
		if len(self.mylist) == 0 :
			raise StackEmpty()
		else:
			return self.mylist.pop()

s = MyStack(3)
#  what follows could be menu driven
try:
	s.push(11)
	s.push(22)
	s.push(33)
#	s.push(44)

	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())
except Exception as e :
	print(e)



