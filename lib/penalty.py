import numpy as np

class penalty:
	def __init__(self, f, g, h, j):
		self.u = 50
		self.beta = 1.01
		self.f = f
		self.g = g
		self.h = h
		self.j = j
		self.first_iteration = True

	#equation that will take the penalty
	def alpha(self, x):
		h_s = self.h(x)
		h_sum = sum([h ** 2 for h in h_s])
		return h_sum  * self.u

	#equation q = f + sum h
	def q(self, x):
		return self.f(x) + self.alpha(x)

	#gradient of q
	def grad_q(self, x):
		j_s = self.j(x)
		h_s = self.h(x)

		len_h = len(h_s)

		grad_j_2 = []
		for i in range(len_h):
			grad_js = []
			for j in j_s[i]:
				grad_js.append(2 * self.u * h_s[i] * j)
			grad_j_2.append(grad_js)

		sum_grad_j = [0 for h in h_s]
		for grad_j in grad_j_2:
			sum_grad_j = sum_grad_j + np.array(grad_j)

		direction = np.array(self.g(x)) + sum_grad_j
		direction = direction.tolist()

		self.u = self.u * self.beta
		return direction

	def error(self, x):
		if self.first_iteration == True:
			self.first_iteration = False
			return 10000
		else:
			return np.sqrt(self.alpha(x))
