import numpy as np
import operator as op
import copy as cp


class linear_search:
	def __init__(self, initial_coordinates, function, direction, max_error):
		self.initial_coordinates = initial_coordinates
		self.function = function
		#self.max_error = max_error #error
		self.max_error = 0.0000001 #error

		self.direction = direction

		#inicial etas (this will be modified to satisfy f1 >= f2 <= f3)
		self.initial_etas = [-0.0005, 0, 0.0005]

		#initial fs calculados (ele sera modificado)
		self.initial_fs = [0, 0, 0]

		#step for the etas to find their ideal values
		self.step_eta_mult = 1.1

		self.max_iterations = 1000

		self.generate_initial_etas()


	def generate_initial_etas(self):

		for i in range(3):
			self.initial_fs[i] = self.eta_function(self.initial_etas[i])

		#find the ideal values that satisfies eta1 < eta2 < eta3 and f1 >= f2 <= f3

		#f1
		while self.initial_fs[1] > self.initial_fs[0]:
			self.initial_etas[0] = self.initial_etas[0] * self.step_eta_mult #step to eta1
			self.initial_fs[0] = self.eta_function(self.initial_etas[0])

		#f3
		while self.initial_fs[1] >= self.initial_fs[2]:
			self.initial_etas[2] = self.initial_etas[2] * self.step_eta_mult #step to eta 3
			self.initial_fs[2] = self.eta_function(self.initial_etas[2])


	#calculate the f for an eta value
	def eta_function(self, eta):
		x = map(op.add, self.initial_coordinates, [eta * d for d in self.direction])
		return self.function(x)


	#find the minimum value of the specified function
	def min(self):
		etas = self.initial_etas
		fs = self.initial_fs
		eta_4 = self.quadratic_adjustment(etas, fs)

		for i in range(self.max_iterations):
			if eta_4 == None or self.error(etas[1], eta_4) < self.max_error:
				break
			etas, fs = self.update_etas(etas, fs, eta_4)
			eta_4 = self.quadratic_adjustment(etas, fs)

		if eta_4 == None:
			eta_4 = etas[1]

		return map(op.add, self.initial_coordinates, [eta_4 * d for d in self.direction]), eta_4
		

	#find the eta_4
	def quadratic_adjustment(self, etas, fs):

		f_sup = fs[0] * (np.power(etas[1], 2) - np.power(etas[2], 2)) + fs[1] * (np.power(etas[2], 2) - np.power(etas[0], 2)) + fs[2] * (np.power(etas[0], 2) - np.power(etas[1], 2))
		f_div = fs[0] * (etas[1] - etas[2]) + fs[1] * (etas[2] - etas[0]) + fs[2] * (etas[0] - etas[1])
		if f_div == 0:
			return None

		eta_4 = f_sup / (f_div * 2)

		return eta_4

	def update_etas(self, etas, fs, eta_4):

		new_etas = cp.copy(etas)
		new_fs = cp.copy(fs)

		f_4 = self.eta_function(eta_4)
		
		if eta_4 > etas[1]:
			if f_4 > fs[1]:
				new_etas[2] = eta_4
				new_fs[2] = f_4
			else:
				new_etas[0] = etas[1]
				new_fs[0] = fs[1]
				new_etas[1] = eta_4
				new_fs[1] = f_4
		else:
			if f_4 > fs[1]:
				new_etas[0] = eta_4
				new_fs[0] = f_4
			else:
				new_etas[2] = etas[1]
				new_fs[2] = fs[1]
				new_etas[1] = eta_4
				new_fs[1] = f_4

		return new_etas, new_fs

	def error(self, eta_2, eta_4):
		return np.absolute(eta_4 - eta_2)

	def min_yielded(self, n_etapas):
		etas = self.initial_etas
		fs = self.initial_fs
		eta_4 = self.quadratic_adjustment(etas, fs)

		for i in range(n_etapas):
			yield etas, fs, eta_4, map(op.add, self.initial_coordinates, [etas[1] * d for d in self.direction])
			etas, fs = self.update_etas(etas, fs, eta_4)
			eta_4 = self.quadratic_adjustment(etas, fs)
