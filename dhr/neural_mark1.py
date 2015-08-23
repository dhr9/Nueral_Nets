import numpy as np

def print_(array):
	for element in array:
		print(element)

class Network():

	def __init__(self,sizes):
#-------CRAP--------------------------------------
		self.num_layers2 = 3
		self.sizes2 = [2,3,1]
		self.biases2 = [[1,2,3],[4,5]]
		self.weights = [[[1,2],[3,4],[5,6]],[[7,8,9],[10,11,12]]]
#--------------------------------------------------
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]

	def feedforward(self,a):
		for b,w in zip(self.biases,self.weights):
			a = sigmoid_vec(np.dot(w,a)+b)
		return a


def sigmoid(z):
		return z

	sigmoid_vec = np.vectorize(sigmoid)


net = Network([2,3,1])

print(net.sizes)
print(net.num_layers)
print_(net.biases)
print(net.biases2)
print("----------")
print_(net.weights)

a = [10,20,30]

net.feedforward(a)