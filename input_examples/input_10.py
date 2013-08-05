d = 4
m = 1
x0 = [1, 3, 10, 2]
eps = 0.001



def f(x):
	fx = x[0]**2 + (2*x[1])**2 + (3*x[2])**2 + (4 * x[3])**2
	return(fx)

def g(x):
	gx = [2*x[0], 4*x[1], 6*x[2], 8*x[3]]
	return(gx)

def h(x):
	hx = [x[0]**2 +x[1] -5*x[2] + x[3]]
	return(hx)

def j(x):
	jx = [[2*x[0], 1, -5, 1]]
	return(jx)