import numpy as np

def funct(f):
	return f*f

fv = np.vectorize(funct)

d = [1,2,3,4]

# print d
# v = fv(d)
# print(type(v))
# print(v)

from functools import wraps

class vectorize():
	def __init__(self):
		pass

	def __call__(self,func):
		print "entering vectorize"
		print func.__name__ + " is executing"
		# func(9)
		print "exiting vectorize"
		
		def wrapper(*args):
			print("enter")
			func(*args)
			print("exit")
		return wrapper

@vectorize()
def add(x):
	print(3)
	print(x)

add(2)

# class vectorize() :
#     def __init__(self,color=False) :
#         if color is not False :
#             print color
#     def __call__(self,function) :
#         def wrapper(*args) :
#             print 'entering' + function.__name__
#             function(*args)
#             print 'exiting' + function.__name__
#         return wrapper

# @vectorize(color = 'red')
# def add(x,y) :
#     print(x+y)
