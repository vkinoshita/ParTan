d = 3
x0 = [3, -2, -10]
eps = 0.001
def f(x):
	fx = x[0]**2 + (0.5 * x[1])**2 + (1.5 * x[2])**2
	return(fx)
def g(x):
	gx = [2 * x[0], x[1], 3 * x[2]]
	return(gx)