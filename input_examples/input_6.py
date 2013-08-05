d = 2
x0 = [10, -10]
eps = 0.001

def f(x):
	fx = (x[0])**2 + (0.5 * x[1])**2 + 50
	return(fx)

def g(x):
	gx = [- 2 * x[0], x[1]]
	return(gx)