import numpy as np    
import random
import scipy.special
from defs import *

class Nnet:
	def __init__(self,num_input,num_hidden_neurons,num_output):
		self.num_inputs =num_input
		self.num_hidden = num_hidden_neurons
		self.num_outputs = num_output
		self.weights_input_hidden = np.random.uniform(-0.5,0.5,size=(self.num_hidden ,self.num_inputs))
		self.weights_output_hidden = np.random.uniform(-0.5,0.5,size=(self.num_outputs,self.num_hidden))
		self.activation_function = lambda x : scipy.special.expit(x)


	def get_output(self,inputs):
		inputs = np.array(inputs, ndmin=2).T

		input_to_hidden = np.dot(self.weights_input_hidden,inputs)

		output_of_hidden =self.activation_function(input_to_hidden)

		inputs_to_outlayer =  np.dot(self.weights_output_hidden,output_of_hidden)
		
		output = self.activation_function(inputs_to_outlayer)
		
		return np.max(output)
		
	def mutate_weights(self):
		 Nnet.mutate_matrix(self.weights_input_hidden)
		 Nnet.mutate_matrix(self.weights_output_hidden)

	def mix_weights(self,nnet1,nnet2):
		self.weights_input_hidden = Nnet.mix_matrices(nnet1.weights_input_hidden,nnet2.weights_input_hidden)
		self.weights_output_hidden = Nnet.mix_matrices(nnet1.weights_output_hidden,nnet2.weights_output_hidden)
		
	def mix_matrices(mat1,mat2):
		num_rows = mat1.shape[0]
		num_columns = mat1.shape[1]
		new_mat = np.random.rand(num_rows ,num_columns)
		total_elements = mat1.size
		num_indicies = total_elements - int(total_elements*MAX_MIXING_PERCENTAGE)


		change_idx = np.random.choice(np.arange(total_elements),num_indicies,replace=False)
	
		for r in np.arange(num_rows):
			for c in np.arange(num_columns):
				index = r*num_columns + c
				if index in change_idx:
					new_mat[r][c]=mat2[r][c]
				else :
					new_mat[r][c]=mat1[r][c]
		#print('new matrix:\n ', new_mat)
		return new_mat

	def mutate_matrix(arr):
		for x in np.nditer(arr,op_flags=['readwrite']):
			if random.random() < MUTATION_RATIO:
				x[...]= np.random.random_sample() - 0.5





