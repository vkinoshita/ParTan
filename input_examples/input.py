d = 3
x0 = [2, -2, 7]
eps = 0.001
def f(x):
	fx = x[0] ** 2 + 2 * x[1] ** 2 + 3 * x[2] ** 2
	return(fx)
def g(x):
	gx = [2 * x[0], 4 * x[1], 6 * x[2]] 
	return(gx)

def h(x):
	hx = x[0] + x[1] - x[2]
	return (hx)