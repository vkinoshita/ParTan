d = 3
m = 1
x0 = [-2.6, 2, 2]
eps = 0.001

def f(x):
	fx = (x[0] - x[1]) ** 2 + (x[1] -x[2]) ** 4
	return(fx)

def g(x):
	gx = [2 * (x[0] - x[1]), -2 * (x[0] - x[1]) + 4 * (x[1] - x[2]) ** 3, - 4 * (x[1] - x[2]) ** 3]
	return(gx);

def h(x):
	hx = [x[0] * (1 + x[1] ** 2) + x[2]**4 - 3]
	return(hx);

def j(x):
	jx = [[1 + x[1] ** 2, 2 * x[0] * x[1], 4 * x[2] ** 3]]
	return(jx);