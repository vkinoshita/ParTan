d = 3
x0 = [20, -2, 7.43]
eps = 0.001
def f(x):
	fx = 100*((x[1] - x[0]**2))**2 + (1 - x[0])**2 + (0.5 * x[2])**2
	return(fx)
def g(x):
	gx = [2*(-1 + x[0]) - 400*(x[1] - x[0]**2)*x[0], 200*(x[1] - x[0]**2), x[2]]
	return(gx)