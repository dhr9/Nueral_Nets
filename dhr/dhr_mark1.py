import numpy as np
import random

class Network():
	
	def __init__(self,sizes) :
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		self.weigths = [np.random.randn(x,y) for x,y in zip(sizes[1:],sizes[:-1])]

	def feedforward(self,a):
		i=1
	def SGD():
		i=1
	def update_mini_batch(self,mini_batch,eta):
		i=1
	def backprop(self,x,y):
		i=1
	def evaluate(self,test_data):
		i=1
def sigmoid(z):
	i=1
def sigmoid_prime(z):
	i=1


b = [2,3,2]
net = Network(b)