import input
from lib.partan import partan
from lib.penalty import penalty
from lib.output import output

pen = penalty(input.f, input.g, input.h, input.j)

p = partan(input.x0, pen.q, pen.grad_q, input.eps, input.d)
optimal_argument = p.min(error = pen.error)
print 'optimal_argument =', optimal_argument
optimal_value = input.f(optimal_argument)
print 'optimal_value =', optimal_value
s = output.write(optimal_value, optimal_argument)