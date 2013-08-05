import input
from lib.partan import partan
from lib.penalty import penalty
from lib.output import output

p = partan(input.x0, input.f, input.g, input.eps, input.d)
optimal_argument = p.min()
print 'optimal_argument =', optimal_argument
optimal_value = input.f(optimal_argument)
print 'optimal_value =', optimal_value
s = output.write(optimal_value, optimal_argument)