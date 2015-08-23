import numpy as np

class Network():

	def __init__(self,sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]

def print_(array):
	for element in array:
		print(element)

net = Network([2,3])

print(net.sizes)
print(net.num_layers)
print_(net.biases)
print_(net.weights)

