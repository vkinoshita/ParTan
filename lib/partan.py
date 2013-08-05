import numpy as np
import math
from linear_search import linear_search
import operator as op
from numpy import array
from numpy import matrix

class partan(object):

	def __init__(self, initial_coordinates, f, g, eps, d):

		self.initial_coordinates = initial_coordinates
		self.f = f
		self.g = g
		self.eps = eps
		self.d = d
		self.max_iterations = 1000

	def norm(self, x):
		norm_vect = [_x * _x for _x in x]
		return np.sqrt(sum(norm_vect))

	def min(self, error = None):
		if error == None:
			error = lambda _x: self.norm(self.g(_x))

		x = self.initial_coordinates

		while error(x) > self.eps:
			ls = linear_search(x, self.f, self.g(x), self.eps)
			p_0, eta_4 = ls.min()

			ls = linear_search(p_0, self.f, self.g(p_0), self.eps)
			p_1, eta_4 = ls.min()

			d = map(op.sub, p_1, x)

			ls = linear_search(x, self.f, d, self.eps)
			x, eta_4 = ls.min()
			print 'x =', x
		return x

	def min2d(self):
		x = self.initial_coordinates

		while self.norm(self.g(x)) > self.eps:
			ls = linear_search(x, self.f, self.g(x), self.eps)
			p_0 = ls.min()

			ls = linear_search(p_0, self.f, self.g(p_0), self.eps)
			p_1 = ls.min()

			d = map(op.sub, p_1, x)

			ls = linear_search(x, self.f, d, self.eps)
			x = ls.min()
		return x


	def min2d_yielded(self):
		x = self.initial_coordinates
		while self.norm(self.g(x)) > self.eps:
			ls = linear_search(x, self.f, self.g(x), self.eps)
			p_0 = ls.min()

			ls = linear_search(p_0, self.f, self.g(p_0), self.eps)
			p_1 = ls.min()

			d = map(op.sub, p_1, x)

			ls = linear_search(x, self.f, d, self.eps)
			x = ls.min()
			yield p_0, p_1, x
