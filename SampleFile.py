from z3 import *

x = Int('x')
y = Int('y')
s = Solver()
s.add(x + y > 5)
s.add(x < 3)
print(s.check())
print(s.model())